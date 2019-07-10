# Numerical Hydrodynamics in GR

Some notes for the Southampton Summer School, July 2019.

## Key differences with vacuum

Carsten has introduced numerical vacuum relativity. First I want to highlight the differences in principle when moving to the matter models.

#### Can't do the "right thing"

In vacuum we have Einstein's field equations that we believe to be "correct" at all relevant scales. Ignoring modified gravity, we take the continuum Einstein equations as being the "right" thing to do and assume we want to get this continuum solution.

In the matter case we know that we're approximating particles, and depending on the problems we want to tackle we have to think more or less about the particulate nature of what we're doing. Electromagnetic and neutrino emission require thinking harder about the individual particles involved; the bulk motion of the huge number of particles that go into a neutron star allow us to average over them, leading to a fluid approximation. When we take a numerical approximation the scales at which the model "fails" are much larger - still currently well below what we can simulate, but not so far out of reach that we should forget them.

Note that this necessarily means that we're throwing away the "correct" physics at the smallest scales. We have to incorporate these effects through closure relations. This comes in many forms. The equation of state, for example, links macro-scale observables based on micro-scale physics. In simulations, we'll also have to include effects like viscosity in similar ways through "sub-grid" models.

#### Variety of relevant models

With vacuum there's there are a few models used: full GR, approximations like CFC, and Newtonian gravity (maybe with modified potentials). However, it's now possible to use the full theory in most cases without approximation.

In the matter case there's a huge range of physical effects to consider, leading to a huge range of potential models that could be included. Starting from hydrodynamics, we can add magnetic fields through MHD or up to more complex EM couplings including, for example, resistivity, and we can add elasticity to model the crust, neutrinos to model cooling, and multifluids to model effects like superfluids or superconductivity. The list goes on. This makes the parameter space to cover horribly large, and parameter extraction in principle much harder.

#### Form of solutions

In vacuum the solutions are generically smooth, although there's some loss of regularity near singularities in the gauges currently used.

For matter it is *generic* that discontinuities will form. This is "obvious" when you think about neutron star mergers or supernovae: at the most dynamic points in their evolution, shocks will form. This puts restrictions on the numerical methods that we can use, and forces us to think carefully about the mathematical foundations of the solutions and the numerics.

Discontinuities have been used to emphasize the importance of having the equations of motion in conservation law form. We'll come back to why in a second, but we should note that there's no reason to assume that the equations we care about are conservative in the sense we want: the vacuum equations aren't, and the most general multifluid equations aren't either. However, we'll always have conservation of *total* stress-energy-momentum.

### Summary

* Complex, interlinked models.
* Conservation laws will apply, but may need some additional non-conservative equations.
* Micro/meso-scale effects need including through closure relations.

## Conservation laws

#### Stress-energy

Start from conservation of total stress energy,
$$
  \nabla_a T^{ab} = 0.
$$
To get this into a form we can solve numerically, choose a tetrad $\{ e_a^{(j)} \}$: four orthonormal vectors. Typically these will be associated with the computational coordinates, so you can loosely think of them as $\partial_t, \partial_x$ and so on, but they generalize to more complex coordinate systems. Contract our conservation equation with a tetrad vector to get
$$
\begin{aligned}
  && \nabla_a \left( T^{ab} e_b^{(j)} \right) &= - T^{ab} \partial_a e_b^{(j)},
  \implies && \frac{1}{\sqrt{-g}} \partial_a \left( \sqrt{-g} T^{ab} e_b^{(j)} \right) &= - T^{ab} \partial_a e_b^{(j)}.
\end{aligned}
$$
We can rewrite this final equation by multiplying through the metric determinant and splitting off the time derivative to get the *balance law form*
$$
  \partial_t {\bf q} + \partial_i {\bf f}^{(i)}( {\bf q} ) = {\bf s}( {\bf q} ).
$$
The crucial feature is that the spatial derivatives ($\partial_i$) are in total derivative form. If there were no source terms (${\bf s} \equiv {\bf 0}$) then this would be a classical *conservation law*. In GR the source terms are geometric. In numerical methods theory we can (mostly!) focus on the principal part and ignore the source term when discussing shocks and other key features.

However, the stress-energy tensor only gives us four equations. Essentially it gives equations of motion for the total linear momentum and the total energy. For hydrodynamic models we also expect to need *at least* one more equation for the density of the fluid. In more general cases we'll need equations for the electromagnetic fields, for individual constituents, for elastic stresses, and so on. Some of these naturally give conservation or balance law forms - for example, ideal and resistive MHD and ideal elasticity can be written this way - but more complex models won't.

#### Shocks

To show why shocks form we move away from relativity for a second and consider the two toy models, both conservation laws, which result from linearizing hydrodynamics in different ways. First look at the advection equation, where the "density" $q$ is advected to the right at a constant speed $v$:
$$
  \begin{aligned}
    && \partial_t q + \partial_x (v q) &= 0, \\
    \implies && \partial_t q + v \partial_x q &= 0.
  \end{aligned}
$$
Here the flux is $f = v q$ and the speed with which information moves is $\partial_q f = v$, as expected. We can draw a characteristic diagram in the $x-t$ plane showing the information moving to the right with speed $v$.

Now move on to Burger's equation,
$$
  \begin{aligned}
    && \partial_t q + \partial_x \left( \tfrac{q^2}{2} \right) &= 0, \\
    \implies && \partial_t q + q \partial_x q &= 0.
  \end{aligned}
$$
This approximates the acoustic modes in a fluid, driven by the fluid pressure. Here the flux is $f = q^2 / 2$ and the speed with which information moves is $\partial_q f = q$: it depends on the value of the solution itself. We can imagine putting down initial data like $q_0 \sim \sin(x)$. The information at the origin does not move, and nor does that at $x = \pi$. However, the information between $x=0$ and $x=\pi$ moves to the right, as $q > 0$, whilst that between $x=\pi$ and $x=2\pi$ moves to the left, as $q < 0$. Drawing a characteristic diagram we see that the characteristics *cross*.

## Reading list

This is a very incomplete list of sources I regularly use.

#### Reviews

* [Font, Numerical Hydrodynamics and Magnetohydrodynamics in General Relativity, Living Review](https://doi.org/10.12942/lrr-2008-7). Last updated in 2008 but crucial background.
* [Marti & Müller, Grid-based Methods in Relativistic Hydrodynamics and Magnetohydrodynamics, Living Review](https://doi.org/10.1007/lrca-2015-3). SR only but updated in 2015.
* [Balsara, Higher-order accurate space-time schemes for computational astrophysics—Part I: finite volume methods, Living Review](https://doi.org/10.1007/s41115-017-0002-8). Very methods heavy. Cutting edge but not easy going.

#### Theses

* [Radice, Advanced Numerical Approaches in the Dynamics of Relativistic Flows](https://www.astro.princeton.edu/~dradice/downloads/thesis.pdf). From 2013, touches on a number of important technical details.

#### Books

* [Leveque, Finite Volume Methods for Hyperbolic Problems, CUP](https://www.cambridge.org/core/books/finite-volume-methods-for-hyperbolic-problems/97D5D1ACB1926DA1D4D52EAD6909E2B9). No astrophysics but one of the standard numerical methods texts.
* [Hesthaven, Numerical Methods for Conservation Laws: From Analysis to Algorithms, SIAM](https://epubs.siam.org/doi/book/10.1137/1.9781611975109). Still no astrophysics and even more mathematical-technical, but goes deep into methods like Discontinuous Galerkin and spectral elements which may be the future direction of the field.
* [Rezzolla & Zanotti, Relativistic Hydrodynamics, OUP](https://global.oup.com/academic/product/relativistic-hydrodynamics-9780198528906). From 2013, its focus is on hydrodynamics, not MHD. Lots of detail.
* [Alcubierre, Introduction to 3+1 Numerical Relativity, OUP](https://global.oup.com/academic/product/introduction-to-31-numerical-relativity-9780199656158). From 2012, its focus is really vacuum relativity, but introduces hydrodynamics well from that viewpoint.
