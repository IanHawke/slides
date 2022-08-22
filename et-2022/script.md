# Numerical methods in GR

## Abstract

The "best" numerical methods depend on the model being simulated, the accuracy needed, and the resources available. This talk will survey the methods currently used across the field, particularly those available through the Einstein toolkit. The links for the next generation of simulations between numerical methods, models of the matter and spacetime, and near-future computing hardware will also be explored.

## Script

### Opening

The best numerical method takes a model and returns an approximation to an observable, within a given error, using the minimum amount of resources.

So there's no *general* best numerical method, as it depends on the model, and also the type of resources available to you.

The Einstein Toolkit was designed for models linked to general relativity, and for observables such as gravitational waves. The size of the given error is set by the detectors, such as LIGO. The size of the problems we deal with, thanks to the complexity of GR and relativistic matter, combined with the small errors required, means that we usually need to use HPC levels of resources.

### PDEs

The equations of motion we typically deal with have a number of features that we need to capture. Let's start from Einstein's Field Equations.

We know that the wave equation is a good approximation for weak gravity - that's why they're called gravitational waves in the first place.

Equally, on the matter side, we know that stress-energy conservation leads to four balance laws, where the equations are first order and the matter terms appear in total derivatives.

Most interesting matter systems can't be described by just these four equations of motion. There are two other features that we typically see. Particle species can be pushed around in advection form. And reactions can change the proportion of different particle species, and this typically appears as a source term in relaxation form.

### MoL

Most cutting edge problems require combining all of these different types of behaviour and more. Cactus and the ETK solve this *multiphysics* issue by modularity - each weakly coupled part of the model, such as solving the spacetime, or the hydrodynamics, or the radiation, is dealt with inside its own code module or *thorn*. However, at the numerical level we still need to sort out how the models interact.

The standard approach in the field is semi-discretization. We take spacetime in a coordinate system split into time and space. We introduce a discrete representation of space: for example, a grid of points on which we know the values of all the fields of interest. We also introduce an approximation to any spatial derivatives in the model at these points. This converts the PDEs that describe the model into ODEs for the coefficients of the spatial discretization. In our example here, the ODEs give the time evolution of the values of the fields at the grid points.

Solving ODEs is well-understood, particularly when the state vector does not change too quickly. Introduce a timestep - the finite discrete gap between points in time where the field values are known. Then use, for example, finite differencing approaches and Taylor's theorem to explicitly write the unknown future field value in terms of the current known values. The solution of the ODE is then found iteratively, with the approximation error being proportional to some power of the timestep. This encodes the order of accuracy of the method.

Within the ETK the `MoL` (method of lines) thorn implements semi-discretization and a range of ODE solvers. The weak coupling between models relies on storing core field values is base thorns such as `ADMBase` or `HydroBase`.

### Finite Differencing

Finite differencing is one of the simplest methods to understand and implement. We represent the field by its values at grid points. We pick a point where a derivative is needed. Using neighbouring points, we fit a polynomial that interpolates the values. The derivative of the interpolating polynomial then approximates the true derivative, with the error proportional to some power of the grid spacing.

The more points used in the approximation, the more it costs, but the more accurate the approximation is. The accuracy of a numerical method is often plotted by taking a known solution and showing how the error changes with the grid spacing, or equivalently with the number of points. This is necessary to show that the method is behaving as expected, that the error is converging to zero as expected, and so in more complex cases the error can be approximated. We show that here and see the huge improvement as the order of accuracy is improved by using more points.

However, it's more relevant to check how the error varies with the resources, which here will be the time taken. We still see a significant improvement with the higher order methods, but it's qualitatively slightly different.

### Dissipation and dispersion

The error I've shown so far is the total error for a known solution. That's not always useful. For gravitational wave purposes the amplitude and phase of the wave, and how it varies with frequency, is more important, as that's much more relevant for parameter estimation from detected signals. We can look at the errors for single Fourier mode solutions. We see that the higher the damping of the amplitude is the key impact on the wave, and decreases rapidly both with grid resolution and, more importantly, with the order of the scheme. However, the phase error is also significant and, more disturbingly, increases with the frequency of the mode much more than the damping does. If you care about phase accuracy - and observing pipelines can be extremely sensitive to it - then high resolution and high order schemes are both crucially important.

For finite difference schemes and simple linear equations (advection here, but wave equations are similar), we can estimate how the phase error depends on the resolution, frequency, and the length of the signal needed. For LIGO accuracy, for waves generated within neutron stars over a period of a second, this gives a minimum numerical resolution of 10 metres with a second order scheme, rising to nearly 800 metres for a sixth order scheme. The former is roughly the highest ever used in GR simulations; the latter is vaguely practical. However, for next generation detectors it's quite possible we'll care about higher frequencies and better phase errors. This gives a minimum resolution below one metre for second order schemes, which is totally impractical.

### Spectral

As higher order methods are better, but use more points, what happens if we use all the data available when computing the approximate derivative? This is essentially a spectral method. Most practical spectral methods do not use the field represented in terms of its values at specific points. Instead the field is represented using modes, or the coefficients of a basis function expansion. Either way, the derivative is represented by a dense matrix which multiplies the state vector of coefficients, whose size is now the number of *degrees of freedom* (if using point values this is number of gridpoints; if using modes, the number of modes).

We see that the approximation to the derivative itself converges incredibly quickly. Finite difference methods converge in a power law fashion; spectral methods converge geometrically, or exponentially. However, when coupled to the time evolution the time solver limits the gain. The cost also depends on the number of modes used. Spectral methods still remain the best, although the technical effort to implement them from scratch is a lot higher (particularly in the nonlinear case) than simple finite differences.

The ETK uses spectral methods to construct initial data in some cases, such as the `TwoPunctures` thorn which does it directly, or via the use of the `LORENE` package. However, the ETK isn't really set up to do evolutions using spectral methods, as there's no thorns implementing an evolution scheme that I know. The `SpEC` code is the best-known solver in the field, which solves for the spacetime.

### Discontinuous data

So why use anything other than spectral methods? There are two reasons. The first comes from matter models, where we expect generically the formation of shocks. This holds because we can take a generic stress-energy tensor, contract with the coordinate basis tetrad, and manipulate stress-energy conservation to get a system of balance laws. If the flux - that is, the term inside the total spatial derivative - is a nonlinear function of the conserved variables - that is, the term inside the time derivative - then generically there will be some initial data that will steepen until the solution is discontinuous and a shock forms. For gravitational wave purposes this is a strong and crucial feature near merger.

Sticking with the linear advection equation, we can see what happens when we use the methods so far with initial data that is either C0 or C1. We remember that we are differentiating the interpolating polynomial. However, when the target data has low differentiability, this interpolation leads to Gibbs' oscillations. We see that the approximation to the derivative is wildly inaccurate. The higher the order of the interpolating polynomial, the worse the oscillations get. Increasing grid resolutions may make the oscillations more localised to the points where differentiability is reduced, but does not change the amplitude of the oscillations, meaning the approximation to the derivative gets worse.

Crucially this means that the finite differencing solution does not converge to the correct result. Spectral methods suffer from exactly the same problems, and the effective high order makes the problems qualitatively worse.

### HRSC schemes

As soon as we are dealing with discontinuous data the original *strong* form of the differential equation does not make sense, as the spatial derivative does not exist at the shock. Instead we integrate over a control volume to get the *weak* form, where the time derivative of the integral average is given by the flux through the boundary of the control volume. In a numerical method we make the control volume be a computational cell. In this *finite volume* form we represent the field not by values at points but by average values within cells. The numerical method would then compute fluxes at cell boundaries.

There are two steps needed. We have to go from the average data to some data at the cell boundaries, which can then be used to compute the intercell flux. We can reconstruct the fields to the cell boundaries and compute fluxes from them; or we can compute the cell averaged fluxes, and reconstruct them; or we can do something in between.

The reconstruction methods are built into a number of ETK-based codes, but are not provided as generic routines. The simplest slope-limited methods, which are second order at best, can be found in `GRHydro`, `IllinoisMHD` and `Spritz`. They also contain higher-order methods such as PPM, but these are not generic and will only apply to hydrodynamics without significant work. More generic WENO reconstruction methods are used in `Spritz` and particularly `WhiskyTHC`, which would be easier to re-purpose for a new model.

The standard approach, taken by `GRHydro`, `IllinoisMHD` and `Spritz` is to reconstruct the fields and then find the flux using the solution to the Riemann Problem in some approximation. The Riemann Problem sets up piecewise constant initial data that is discontinuous at one point and asks how it evolves in time and can, in principle, be solved exactly in most interesting cases. However, the computational cost means it is more practical, in an evolution code, to approximate the solution, or to get the intercell flux directly.

The alternative of approximating the flux and reconstructing that is used by `WhiskyTHC`. The advantage of this approach is that it more readily extends to high-order methods. The disadvantage is that you have less control over the physicality of the reconstruction - near the neutron star surface, for example, it can be very hard to know if the reconstruction is effectively giving a negative density or pressure.
