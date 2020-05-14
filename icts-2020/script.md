# Script for lectures at ICTS

## Lecture 1

### The goal

For many of us studying numerical relativity and relativistic hydrodynamics the motivation is gravitational waves. The goal was to observe these and use them to tell us about gravity, relativity, and the physics of extreme objects.

With the detection of black hole mergers in 2015, and neutron star mergers from 2017, the goal is now reality. The object now is to squeeze the maximum possible information from these observations, through better modelling. Full, quantitative modelling of neutron star mergers needs numerical simulation, which is going to be the focus of these lectures.

Talk through GW170817 in more detail at this point, particularly the seconds gap between GW peak and GRB.

### The problem

The objects we're trying to model are compact. The single observation of neutron stars in gravitational waves has matched expectations from theoretical calculations and is comparable to observations in other bands: for example, the NICER observations of isolated neutron stars give similar numbers. For our purposes we need the neutron stars' mass, which is slightly more than our sun; we need their radii, which is around 10 to 15 km; and we need information on how the matter reacts to being pushed around. This final point, usually encoded in a single function called the equation of state, is something we still don't know well.

### The problem with the problem

We want to do numerical simulations, or evolutions, involving neutron stars. A neutron star contains a bit more matter than our sun. Our sun contains roughly $10^{60}$ elementary particles in it.

To do a practical numerical simulation we're going to need to use a computer. The current fastest computer in the world, Summit, can do around $10^{18}$ floating point operations per second. The total world computing power is uncertain, but probably not above $10^{25}$ FLOPs.

Clearly we're not going to be able to do an evolution of every individual particle within a neutron star.

### Hydrodynamics

If we can't treat each particle separately, we'll have to average over them in some way. The hydrodynamics approximation averages over them all. Our $10^{60}$ separate particles, each with their own positions, velocities, and properties, are averaged to give a *single* (vector) field. At each point in spacetime this field will describe the number density of particles, and the direction in which they flow.

This averaging process gives us a small set of differential equations to solve. With some standard approximations, it actually reduces to *five* PDEs (on top of those describing the evolution of the spacetime). This makes the numerical simulation practical. However, it has also thrown away (or compressed) a lot of physics.

It also means that there is a crucial difference of principle and of scale between *vacuum* relativity and relativistic *hydrodynamics*. In the vacuum case we have Einstein's field equations which, in principle, hold on all scales within our simulations and models. In hydrodynamics, however, our model and description breaks down on certain scales. We must keep in mind that as computer power and numerical accuracy increases our results may *not* get better, as we may hit the limitations of our models.

### Practicalities

Now we have a starting point for our simulation. We're going to solve a set of PDEs within a domain: a box that we'll put around the neutron stars. Within this box we'll evolve the spacetime and the matter, and extract observable signatures like gravitational waves and emissions in the electromagnetic spectrum. We'll do this by splitting the box into small pieces - grid cells, or points, or elements - and replacing the PDE with discrete approximations that can be solved on a computer. The smaller the small pieces, the more accurate the solution, but the more computer time and memory we need.

So, what's our minimum requirements?

First, let's look at the gravitational waves detected from GW170817. These were detected in the hundreds to thousands of Hz. As the waves travel at the speed of light we can convert the frequencies to a wavelength, suggesting that the gravitational wavelength here is around $10^6$m. So, our computational box needs to be big enough to fit in a gravitational wavelength. In fact, it should be big enough to fit in multiple wavelengths, so we can cleanly extract the wave far from both the source - that is, far from the neutron stars - and also far from the artificial boundaries of our box. So our minimum requirement is that the box should be around $10^7$m to a side.

Next, let's think about the size of the grid cells. We're going to use a hydrodynamic model of the star. In a fluid model like this, information travels back and forth in waves. The numerical accuracy depends both on how accurately we capture the amplitude of the waves, and how accurately we capture their phase. A back of the envelope calculation tells us how many grid cells we need to use to capture a wave of wavelength the size of a neutron star (whose diameter is around $25$km) oscillating say $30$ times (which captures roughly the last $10$ orbits) to around $1$% accuracy, giving a grid cell size of around $10^2$m.

Finally, let's think about how many steps we have to take. When evolving forward in time we can think about the simulation in relativistic terms. Take a grid cell at a fixed time and think about its *past domain of dependence*: that is, which grid cells (at some previous time) could possibly affect the value of this cell? This suggests that the maximum timestep we can take is roughly the grid cell size divided by the speed of light, which is roughly $10^{-6}$s.

Putting this all together, we need a grid of roughly $10^{15}$ cells to solve a merger with reasonable accuracy. To solve for around $1$s - and remember that the GRB after GW170817 was detected a few seconds after the peak gravitational wave amplitude - we need to take $10^6$ timesteps. Combining this, we're looking at updating a small cell at least $10^{20}$ times. That's a lot of work.

Now, no current simulation evolves for a full second. However, simulations do evolve for up to around $100$ms, and do typically use resolutions around $100$m, and sometimes considerably finer. We need to consider what physics we can capture within a model on these scales, what behaviour we should expect, and how we can simulate that numerically.

### Multimessenger

The description so far has concentrated on the inspiral phase and gravitational waves. However, GW170817 was seen in the EM spectrum as well - or at least the post-merger signal was. In fact, our expectations even from the most extreme scenarios are that no current gravitational wave detectors will be able to see anything much after merger. We'll need detailed numerical models of the matter as well as the spacetime to predict the EM and neutrino emission from the messy post-merger situation.

### The shortcut

Let's look at a simulation using a single perfect fluid with magnetic field. This simulation is from Bruno Giacomazzo's group. It ignores dissipation, viscosity, heat transport, magnetic resistivity, superfluidity, superconductivity, the elastic crust of the neutron star, and any radiation transport. It includes full general relativity, models the star as a hot fluid, and adds an ideal electromagnetic field.

Initially the stars inspiral due to the emission of gravitational waves. Around $15$ms after the start of the simulation the stars merge. At this point things get messy. When the stars smash into each other a shock propagates through the merged object, massively increasing the temperature. At the same time the magnetized material "slips" past its companion, winding up the total magnetic field in a dynamo effect. The remnant tries to settle down, with some material expelled from the system. But the object is too massive to support itself, and at around $30$ms the core collapses to a black hole. Most of the dense matter is rapidly swallowed into the black hole, leaving a small fraction at larger radius to settle into a disk. It's believed that the kilonova occurs when this remaining matter collapses back on the black hole.

We see that we need to model the fluid interior and the vacuum exterior. We need to model the shock as the stars smash together, and the resulting jump in temperature. We need to model the small scale structure in the interior as the magnetic fields wind up, forming the precursor to the jet. And we need to do this on top of evolving the spacetime, tracking any black holes that might appear.

See also https://www.youtube.com/watch?v=UQCfo5L3ShQ (https://arxiv.org/abs/1809.11161, Radice et al) or https://www.youtube.com/watch?v=Dyn9KbB_zeo (Dietrich et al)

**Break at this point**: a bit over 25 minutes to here. Include David's video as well. (Didn't have the multimessenger slide, so add 5 minutes)

### Conservation

We now know the outlines of our problem. We want a model of matter, coupled to GR, that we can write as a set of PDEs. This model will encode the detailed physics we're interested in, at the level we can simulate with our given resources. But before we try and be specific, let's look at what we can say in general.

We know the field equations require total stress energy conservation: the divergence of $T^{ab}$ is zero. We can use this to get *four* equations of motion. The most useful form for our purposes is to use the standard identity for the 4-divergence of a vector, which can be written as the *partial* 4-divergence of that vector, weighted by the metric determinant. To get from the stress-energy, which is a two-tensor, to a vector, we contract the free index with one member of a *tetrad*, which is a set of orthonormal (in our case) vectors that we can link to the coordinates. This then allows us to write stress energy conservation as four PDEs, one for each member of the tetrad.

The key point is that the only derivatives of the matter appear in total divergence form. The term on the right-hand-side which isn't in this form only involves derivatives of the tetrad, which can be written as derivatives of spacetime quantities. We write this abstractly in *balance law form*: all derivatives of the matter are total derivatives, but these *fluxes* must balance off against the *source terms* which come from the geometry.

If we simplify to Minkowski space in standard Cartesian coordinates then the source terms vanish and these balance laws reduce to the *conservation laws* for energy-momentum. However, we need to be careful of this interpretation (locally): if we write Minkowski spacetime in *spherical* coordinates then there will be source terms, but that certainly does not mean that energy-momentum is being transferred between the matter and the spacetime.

### Conservation laws and shocks

We see that *generically* the matter will obey conservation laws. We expect the fluxes ${\bf f}$ to depend *nonlinearly* on the conserved variables ${\bf q}$. This immediately tells us something very important.

The simplest conservation law is the advection equation, where the solution is propagated to the right with constant speed $v$. For a nonlinear conservation law we can *locally* approximate it as an advection-like equation, where the solution propagates with speed $\partial_q f$. This means the propagation speed depends on the data. Depending on the form of the flux function, some gradients will steadily get steeper, and some will get shallower. In the absence of dissipation (and crucially the generic total energy-momentum equations have no dissipative terms) these steepening effects will lead to discontinuities: a generic *shock* will form.

### Shocks and Uniqueness

From the conservation law form we can integrate over a small region of spacetime (see the exercises) to find the *Rankine-Hugoniot* conditions, telling us how fast the shock travels. It's important to note that this depends on the form of the flux function.

However, this highlights how important the form of the equations of motion is. Take the example of Burgers equation where the flux function is quadratic. This is equivalent, when solutions are differentiable, to a PDE where the local advection velocity is given by the data $q$ itself. However, this isn't unique. The conservation laws at the bottom are *all* equivalent to this non-conservative form of Burgers equation for positive $n$. Crucially, they all have different shock speeds, so different solutions in the discontinuous case.

For our purposes this means that when the shock forms as the neutron stars merge, and as it propagates around in the post-merger state, it will be *essential* that we have the correct form of the conserved variables and the fluxes. If we use the wrong conservative form then we will get the wrong solution. If we use the non-conservative form then we need to explicitly include a dissipative term and take appropriate limits, which is hard. If the model can't be phrased in a balance law form, getting correct shock forms will be complex.

### Euler equations

Total stress-energy conservation gives us four equations. When we talk about a standard ideal fluid it depends on more information. We'll need the number density: the number of particles within a local volume. We'll need its velocity, which is three bits of information making up a unit 4-vector. And we'll need a variable describing the internal energy, or temperature: essentially, how much variation there is at the micro-scale that we've averaged over to get our hydrodynamics description.

This is five independent quantities. So, in addition to the four PDEs we get from stress-energy conservation, we'll need one more. We get this by assuming that particles are neither created nor destroyed, so the particle number flux is conserved. This gives us $\nabla_a (\rho u^a) = 0$. Using the same identity for total divergence as in the stress-energy case, we can use this to write the *continuity equation* as a PDE in conservation law form.

We can then write down the stress-energy tensor for the fluid. There is the total energy piece which moves with the flow. Then there is the isotropic pressure piece which acts normal to the flow. Plugging this into the conservation laws and adding the continuity equation gives us five PDEs for *six* quantities. To close the system we need to connect the thermodynamic variables: the density, internal energy, and pressure. We do this through the *equation of state*, which we can take to be a function giving pressure (and other quantities) in terms of density and internal energy, or density and temperature.

Before we move on we should talk about more complex *mixture* models. The equation of state describes the microscopic interactions between the particles. In the model we've talked about so far we haven't made any allowance for the differences between particles: we've only cared about how many there are, through the number density. This is too simplistic in many cases. Many equations of state really care about the *relative proportions* of the different particles involved. For example, many care about the *lepton fraction* $Y_e$, which is (roughly) the fraction of particles that are electrons.

The simplest mixture models are formed by imposing that each individual type of particle is also conserved, and that they all move with the same velocity. We then get the equivalent of the continuity equation for each species, which can be seen as an equation for the species fraction, say $Y_e$. The equation of state can then be extended to depend on these species fractions. In more complex mixture models we can allow particle *species* creation and destruction by adding source terms, provided the total number of particles stays fixed. This can require some care, as the particle interactions can impact on the energy-momentum.

### Newtonian limit

It's useful to compare the resulting equations of motion to various limits. This is particularly true when developing numerical methods, algorithms and codes, and it allows us to test in simpler situations where it's easier to debug.

The particular limit we're most interested in is the Newtonian limit, where the speed of light is very large compared to the fluid velocities, and pressures (for example) are small. The Newtonian limit is particularly useful to us as there's a long and successful history of building simulation codes in academia and industry, and we can (and still do) use the experience and methods of this huge community.

The Newtonian equations in $1+1$ Cartesian coordinates have the following conservation law form. The continuity equation is first, essentially advecting the density along with the flow. The momentum equation is next. The momentum is advected, but there's also a contribution from the gradient of the pressure. The total energy equation is last, which again shows advective-like behaviour. If we were to investigate the speeds of propagation, which is one of the exercises, then we wouldn't be surprised that one is precisely the *advective velocity* $v$. The other speeds of propagation are the *acoustic velocities* which are $v \pm c_s$, where $c_s$ is the *speed of sound*. The sound speed depends only on the thermodynamic quantities and is given by the equation of state. In simple cases it's roughly the square root of the ratio of the pressure to the density.

### Up to relativity

To see how useful a model the Newtonian model will be to us, first look at the equations in special relativity. That is, take the GR equations in Minkowski spacetime in standard Cartesian coordinates. We see that they're directly comparable to the Newtonian limit.

We can see the additional relativistic effects in red. In the continuity equation we see the appearance of the *Lorentz factor*, which is linked to the velocity, and appears here because of length contraction or time dilation effects. The Lorentz factor is one when velocities are small but diverges as the velocity approaches the speed of light. This is a purely kinematic effect, exactly mirroring standard SR results on length contraction.

In the momentum equation we also see the Lorentz factor coming in. However, we also see the density term is modified by the appearance of the *specific enthalpy* $h$. This comes in because of mass-energy equivalence in relativity: the internal energy of the fluid has its own contribution to the mass.

The kinematic modifications here leave the *qualitative* form of the conservation laws the same, but modify the *quantitative* details. Possibly the most important for numerical work is the speeds of propagation. As you would expect in relativity the speeds have to be below the speed of light. One speed remains the advective velocity $v$. The acoustic velocities now use the *relativistic addition formula*, dividing the Newtonian formula by $1 \pm v c_s$. The appearance of the enthalpy in contributions to the mass also modifies the speed of sound.

Finally we look at the equations in full general relativity. These equations look much more complex, but should contain few surprises based on our previous discussions. First, from the form of the general energy-momentum conservation laws, we expect to get terms relating to the determinant of the metric. The difference between the *spatial* metric determinant which appears in the time derivative, and the *total* metric determinant appearing in the spatial divergence, is a factor of the lapse. This can be thought of as making the dimensions match up. The geometric source terms we have already discussed; they're very messy but, along with the metric determinants, result from the spacetime curvature. The other difference to note is the way the velocity is modified by the shift vector. This results from the $3+1$ decomposition, so the fluid velocity now has a piece related to the way coordinates move relative to our spatial slice.

The conceptual issues from the transition from SR to GR are (at least in terms of the matter) small. The *practical* implementation issues are, however, substantial. The speeds of propagation become much more complex to write down. The relation between conserved and primitive variables becomes steadily more complex as we move from Newtonian to relativity. More care is required in dealing with the variables: see that both covariant and contravariant components of the velocity appear in the fluxes, for example. However, many of the key *conceptual* points can be illustrated and tested in a Newtonian setting and Newtonian codes.

### MHD

Before we move on to talking about *how* we simulate these PDEs, I want to note how the electromagnetic fields can be included in our models.

When we talked about mixture models we mentioned how we could distinguish different types of particles moving together. Going beyond just the fluid properties, we can also consider the charge of the particles. At any point, the total charge current is the sum over all species of their number current times their charge. This charge current acts as a source for the Maxwell equations. The Maxwell equations result from total charge conservation.

All of this can be expressed in terms of the Faraday tensor. This gives a term which adds on to the stress-energy tensor, modifying the conserved variables and fluxes in our generic conservation equations. In addition, the Faraday tensor can be written in terms of electric and magnetic fields, and in these terms the Maxwell equations can be written in balance law form with the current as a source.

The problem is that a lot of dynamics is acting on *very* short length and time scales. This makes the evolution of the full Einstein-Euler-Maxwell system very expensive, as we need - for stability - to take tiny timesteps. It is typical to make additional assumptions to restrict the impact of the small scale behaviour, and to enforce *ideal* conditions where there is no resistance to the charge current. In this case a simplified Ohm's law allows us to replace the electric field with the cross product of the magnetic and velocity fields, allowing us to drop the evolution equation for the electric field completely.

We now have *eight* PDEs: the continuity equation for total particle number, the generic energy-momentum balance laws, and the three equations for the magnetic field. We have an equation of state closing the system, and constraints on the magnetic field following from Maxwell's equations. The evolution equations are practically more complex than in the hydrodynamic case, but conceptually similar. The constraint equation, however, causes conceptually new problems, as we'll see later.

**Natural place for break 2** Around 44 minutes for this section!

### The isolated neutron star

Now we have equations of motion that we can, in principle, solve. Before doing so we need to check we having all the conditions required to solve a set of PDEs. The crucial things we need to think about are (1) do we know the domain on which we're going to solve; (2) do we know the boundary conditions we're going to impose; (3) do we know the relationships between all the variables involved in the problem?

We discussed the domain when talking about the practical requirements at the start: a box big enough to hold multiple gravitational wavelengths. That means it will be many orders of magnitude bigger than our neutron star. That makes the boundary conditions we're going to impose deceptively easy: at the edge of the box there's no matter, and never will be any matter, so we can "just" set it to be vacuum.

This is where we should realize that the vast majority of the box will be vacuum, maybe with some propagating EM waves. This is problematic, not for the boundary conditions themselves, but for the equations of motion. All our fluid conserved variables contain the density, which vanishes outside of the star. This means the equations degenerate in this vacuum region. This makes the surface of the neutron star in particular tricky to handle, and the boundary between a region that's mathematically well described by our equations, and one that's not.

A range of analytical and numerical tricks, modifications and fixes have been suggested. The simplest, and still widely used, trick, is to introduce an *atmosphere*. This purely numerical trick replaces vacuum with a low density region that is left to evolve freely. Any point or region where the density, pressure or energy gets too low is reset to this atmosphere value.

Whilst simple and (reasonably) robust, the physical implications of adding an atmosphere remain worrying. Experiments have shown that the impact of accreting this atmosphere onto the neutron star are negligible, and its interaction with the outer boundaries is also not a problem. However, its interaction with low density matter expelled in the merger process, particularly with magnetic fields, or in regions of high temperature, could have a significant impact on the observables. This is somewhere we must improve.

### C2P: Relating the variables

The final topic to explore before we work out how to solve our PDEs is to relate the different variables that appear in our equations of motion. We have a number of different classes of variables. The *primitive* variables are any minimal set of variables that could, in principle, be observed. Typically in hydrodynamics we would think of density, velocity, and (say) internal energy. The *conserved* variables are those actually evolved. Here that's something like the density, momentum, and energy. The *auxilliary* variables are other quantities that are useful to compute for analysis or simplicity, such as the enthalpy or Lorentz factor. The *fluxes* and *sources* finish the description of the equations of motion, and are usually a combination of primitive, conserved, and auxilliary variables.

In the Newtonian case there are closed-form analytic expressions relating all variables, except those that need the equation of state. There is minimal cost in converting between any sets of variables, but minimising the number of times the equation of state is called is useful for computational performance.

In the relativistic cases things change drastically. There are closed-form analytic expressions to go from the primitive to the auxilliary and conserved variables. However, it is very rare to have closed-form expressions that compute the primitive variables from the conserved variables. So, given initial values for all variables we can cheaply update the conserved variables using the equations of motion. It is then a complex, expensive process to recover the primitive and auxilliary variables that we need in order to compute the fluxes and sources to update to the next step.

The typical approach is to write the relation between the conserved and primitive variables as a nonlinear implicit algebraic equation. Standard algorithms for solving these are known: when it can be written in terms of a single variable, as in the hydrodynamic case, then algorithms like bisection and Newton-Raphson can be used.

Interestingly, when more physics is added in a *minimally coupled* fashion, the conversion does not get more complicated. You can see this from the stress-energy tensor. Minimal coupling essentially means the new physics is added in, meaning the new terms are added in to the conserved variables. Separating these terms that are linearly combined is possible in, for example, Einstein-Euler-Maxwell.

*However*, this is not true in MHD. In using Ohms law to eliminate the electric field we strongly couple the Euler and Maxwell parts of the system, through "E equals v cross B". The MHD system becomes a multi-dimensional root-find, which is much more expensive and much less robust. There are available codes based on lengthy papers for doing this inversion: I strongly recommend relying on them.

### Summary of lecture 1

We have
* talked about what's practical on physical and computational resource grounds;
* motivated the hydrodynamic description;
* written balance law PDEs from stress-energy conservation;
* looked at how the remaining equations of motion can be found;
* discussed remaining implementation issues including the atmosphere and converting between variables.

In the next lecture we'll outline the numerical methods needed to solve these equations of motion.

## Lecture 2

### Welcome back

In the first lecture I wanted to emphasize the modelling approximations and limitations of what goes in to a numerical simulation. These come from physical and resource limitations. They lead us to consider the most important features of our models, and so what aspects we need to model in what order. The key points from the first lecture were that
* conservation and balance laws are generic features of matter simulations;
* these lead to shocks, and these shocks do appear in mergers;
* using techniques from Newtonian CFD is a good place to start, but we need to consider issues specific to NSs and relativity, like artificial atmospheres, and the more complex equations of motion.

Today's lecture is going to be a deep dive into the numerical methods. We'll look at the standard techniques used in the field. The exercises associated with these lectures ask you to implement and test some of these techniques: that's the best way of getting to grips with the difficulties, limitations, costs, and complexities.

### Balance laws

The general form of the equations of motion of relativistic matter can be framed as here. Some quantity is evolved using its flux, ${\bf f}$, additional non-conservative terms that push the matter around through the matrix $A$, a second order diffusive derivative operator with dissipation matrix $D$, and a source term ${\bf s}$ that typically represents exchange of "stuff" to other parts of the model. In the most complex cases the functional form of the matrices, sources or fluxes can depend not only on nonlinear algebraic operators of the evolved vector ${\bf q}$, but even on nonlocal operators. An example would be radiation transport where the optical depth is needed.

However, this is far more complicated than is generally needed for NS mergers, particularly through the inspiral stage. In these stages we are dominated by the flux terms. In the standard models (hydrodynamics, maybe including EM fields through the MHD approximation) we can write the equations in conservation law form. And, when radiation transport can be neglected, we can assume that the source terms are given in an algebraic form.

This means we can concentrate on the fluxes. From a mathematical and implementation point of view the most important terms are the *principle part* with the highest derivatives, so we will (for now) look at the conservation law form and the numerical methods needed for that.

### Characteristics

As a quick recap, remember that for the advection equation (where the flux is a constant *velocity* $v$ multiplying the quantity $q$) we can define characteristics: lines, of slope $v$, along which the solution is unchanged. We can use this locally for nonlinear problems like Burgers equation: with a general flux $f$, the characteristic speed is $\partial_q f$. This only makes sense away from discontinuities.

When we extend to the system case it's easiest to consider the linear problem first. When the flux is defined by a linear system, ${\bf f} = A {\bf q}$, then we can change variables to get the solution. A crucial aspect of the conservation laws is that they are *hyperbolic*: the essential consequence of this for now is that $A$ will be diagonalizable. This means we can define and work with the *characteristic variables* ${\bf w} = L {\bf q}$, where $L$ is the matrix of left eigenvectors. The characteristic variables obey *uncoupled* advection equations, with the advection velocity being $\lamba_i$, the eigenvalues of the matrix $A$. So we can use the solution from the advection equation: each characteristic variable propagates unchanged with a fixed speed. We can then find the solution for ${\bf q}$ by transforming back using the matrix of right eigenvectors.

Locally, in smooth regions, we can see how this would work in the nonlinear case. The Jacobian matrix $J = \partial_{\bf q} {\bf f}$ plays the role of $A$. The characteristic variables can therefore be defined pointwise, noting that the eigenvalues and eigenvectors are going to vary with space. These are then propagated forward and recombined, in principle. In practice the re-combination is difficult, as the correct eigenvectors to use depend on the new data in ways that can be hard to disentangle.

However, the viewpoint of using characteristics is fundamental to a lot of numerical algorithms. Whilst the full procedure outlined here is just about never done, the information is always useful to interpret how the algorithm is working.

### Wave types

From the characteristic point of view we can distinguish different generic types of behaviour. If we start from simple initial data, such as the piecewise constant data illustrated on the left, then there's typically three different outcomes. For complex systems we'll see them all, and some more!

The first type of behaviour, on the left, is where the characteristics separate. This leads to a continuous spreading of the data. In hydrodynamics this is referred to as a *rarefaction wave*: the material is rarefied as it expands.

The second type of behaviour, on the right, is where the characteristics converge. This leads to a discontinuity, even when the initial data is smooth, as discussed in the first lecture. This is a shock, and typically is associated with a jump in all variables. Specifically in the hydrodynamic case we would see entropy and temperature increase through the shock wave, whereas across any other wave they would remain constant.

The final type of behaviour, in the middle, is where the characteristics move parallel to each other, maintaining the jump in the initial data. These *linear* waves are associated with jumps in material properties, or rotations of vector properties. In hydrodynamics these are the *contact waves*, and are associated with the advective velocity. The nonlinear waves are associated with the acoustic waves.

In MHD there is a more complex wave structure. There is still a central linear contact wave, but each nonlinear acoustic wave splits into two nonlinear "fast" and "slow" waves separated by a linear wave across which the EM fields can rotate. This additional complexity in the wave structure is harder to resolve numerically.

**Just under 20 minutes to this point**

### Grids and approximations

On to numerical approximation. We want to solve *continuum* partial differential equations on a computer. The solution, $q(x)$, needs - in principle - an infinite amount of information. That's because the continuum solution could, in principle, take totally different unpredictable values at every separate point $x$. This way of thinking is clearly useless when working with a computer with a finite amount of working memory.

Instead we consider ways of approximating the solution $q(x)$. There are essentially three that are used in the field.

The first is the point value approximation, used in *finite differencing*. In this case the domain is discretized into points, and we assume that we know (or want to compute) the value of the solution at each of these points. The solution is *not* known between the points. When we want to link the solution at different points - for example, when approximating a derivative - we have to impose the general behaviour of the solution between those points. For example, if we interpolate between points using a straight line then the derivative is the slope of this line.

The second approach is to split the domain into *cells*, and within each cell to store the average value. This is the *finite volume* approach. In this case some information is known at every point in spacetime: the average value near that point. However, the exact value is known *nowhere*. Again, to get the value of the solution at a specific point we have to impose the general behaviour of the solution. When restricted to a given cell this behaviour has to be consistent with the average value within that cell. The finite volume approach implicitly "smears out" the local behaviour of the solution, which is exactly what we want when dealing with discontinuous solutions like shocks.

The final approach has links to the finite volume approach, but is more often referred to as a *finite element* method. Instead of storing the average value of the solution within a cell, the *moments* of the solution with respect to some function basis are stored. Typically the zeroth moment would be the cell average of the solution, the first moment linked to its derivative, the second to its curvature and so on. This is fundamental to the *Discontinuous Galerkin* method that HP will talk about later. So far this hasn't been used much for relativistic matter simulations, for reasons we'll get to later.

### Fluxes and telescoping

To see the implications of the finite volume approach, where we split the domain into cells, let's use Gauss, or Stokes, to integrate our conservation law over the domain. We see that the integral over all space leads to all the spatial derivatives disappearing. The equation becomes an ODE, where the time derivative of the integral average of the solution over the domain is given by the surface integral of the flux through the domain.

This is the *weak form* of the conservation law. We'll talk about weak forms more generally later. Crucially, the weak form is used to remove spatial derivatives from the solution (which might be discontinuous). This allows us to talk about discontinuous solutions, like shocks, with confidence that the mathematics will work out.

We see that we're still not at a point where we can solve this equation. The ODE is defined by the surface integral of the flux. Evaluating this flux over the boundary of the domain requires knowing the solution at the boundary of the domain. But we don't know the solution there: we only know the integral average within the domain.

This brings us to the fundamental step in numerical methods for conservation laws. We need a prescription for computing this boundary flux. Once we have that, we can solve the ODE using standard methods.

To be concrete, let's reduce our domain down to one spatial dimension. We split the domain into cells. We label the cells with an integer $i$, and given the cell centre the coordinates $x_i$. The interfaces between the cells and the boundaries of each little subdomain. We label the coordinates of these interfaces with "half integers", so the boundaries of cell $i$ are at $x_{i-1/2}$ and $x_{i+1/2}$. We then write the ODE explicitly, showing that the average solution $\hat{q}_i$ within cell $i$ evolves due to the flux into the cell through the left interface at $i-1/2$ and the flux out of the cell through the right interface at $i+1/2$. Note that "into" and "out of" are conventions without physical meaning here, associated with assuming the material flows from left to right: the flux could be negative, meaning the material is flowing from right to left.

There is a central result from writing the conservation law in this form. If we have a discrete algorithm that updates in this fashion then it is conservative *at the discrete level*. To see this, imagine summing up all the integral averages in all the cells. This would give the integral average over the entire domain at that time. Now imagine doing this at a later time, after the solution has been updated using the flux differencing form here. Each internal cell interface has a flux that is used twice: the flux through the interface at $i+1/2$ is used to update cell $i$ and cell $i+1$. As each update has different signs, the internal contributions cancel out. This *telescoping* effect means the total integral average is only changed by what comes in through the boundaries of the full domain. Total conservation is retained. This is essential to ensure the Rankine-Hugoniot conditions are satisfied at the discrete level and any shock propagates at the correct speed.

### Computing the intercell flux

We're now at the point where describing our algorithm boils down to computing the flux through a single cell interface. We'll look at *Godunov's method* and variants as a starting point.

In Godunov's method we assume the solution is piecewise constant. That is, within each cell the value of the solution is the integral average. This gives us the value of the solution everywhere *except* at the cell interfaces, where there are two values that, in general, won't agree. We need to take these values and get the intercell flux.

To do this, think about the characteristics. For example, think about the advection equation. If the advection velocity $v$ were positive then the solution at the cell interface would always be given by the value to the left of the interface. More generally, if the characteristic speed is positive, the value of the solution at the interface is given by the solution to the left. From this we can compute the flux.

In the system case this is more complex. For a linear system we can convert to characteristic variables. The eigenvalues tell us which characteristic variables propagate to the right, meaning we should use the solution to the left of the interface, and vice-versa. This gives us the characteristic variables at the interface, from which we can convert back to get the solution, and hence the flux.

In the nonlinear case this gets yet more complex. In this most general case we are looking for a solution to the *Riemann problem*: what's the solution of the PDEs when the initial data is piecewise constant? This can be hard to compute exactly: in most relativistic cases it's impractical. It can be approximated using some, or all, of the characteristic information as in the linear system case. In relativity people often use simple approximations, as computing the characteristic information needed for more complex approximations is expensive.

### Approximate Riemann Solvers

As an example of a simple approximation we look at the HLLE method. This assumes that there are two characteristic waves and that the solution jumps discontinuously across both. So the approximate solution will have three states: the initial left and right states (either side of the interface), and a central state. If the characteristic speeds have the same sign then the solution along the interface is given by one of the initial states, and everything is straightforward. If they have different signs then the solution along the interface is given by the intermediate state. This can be found by imposing conservation across each wave, leading to a simple formula for the intermediate state: from this the intercell flux follows.

The HLLE method has some nice properties. It's fairly cheap to compute, especially if simple approximations to the characteristic speeds are used. It's not specific to one model. It's linked to *positivity preservation*: quantities like density that should be positive will remain positive, when HLLE is used in a particular way.

However, HLLE has its problems. In particular, linear waves (like contact discontinuities) tend to be smeared out very badly. For MHD this can be a serious problem, as there's more linear waves.

More complex approximations either work to ensure better behaviour when the waves aren't discontinuities, or to ensure better capturing of the linear waves. For hydrodynamics this helps but isn't essential in many cases: for MHD it's often needed.

**About 40 minutes to this point, so slightly over 20 minutes for this section**

### Dimensions, costs, and accuracy

We now have an algorithm that will work. Godunov's method assumes the solution is constant within each cell, and computes the intercell flux using an approximate Riemann Solver. This can be extended to two or three dimensions by solving a Riemann problem for each cell face.

However, the algorithm isn't very accurate. This wouldn't matter if we could throw computing power at it, but as we've seen we're going to be limited in the size of the grid cells we can use. We measure the accuracy by how quickly the error reduces as we reduce the grid size. If the error scales as the cell size $\Delta x$ to some power $p$ then we say the method is $p^{\text{th}}$ order accurate. Godunov's method is first order accurate: if we reduce the cell width $\Delta x$ by a factor of 2 then we reduce the error by a factor of 2.

Unfortunately, reducing the cell width by a factor of 2 does not mean the computational cost goes up by a factor of 2. In three space dimensions we have to reduce the grid size in each direction. The CFL stability limit discussed in the first lecture implies we also have to reduce the time step by a factor of 2. So the computational cost goes up by a factor of 16.

So, for cost and efficiency reasons we want to improve the order of accuracy. If we get up to fourth order then the accuracy will scale linearly with the computational cost, which would be great. Unfortunately, increasing the order of accuracy is hard, and it's hard for a crucial, physical reason: shocks.


### Monotonicity, Gibbs oscillations, and Godunov's theorem

A different visual way of thinking about Godunov's method (in one dimensions, at least) is the *Reconstruct, Evolve, Average* framework. We start with the cell average solution: within each cell the solution is constant. This is the *reconstruction* step: going from our cell averages to an assumed form for the solution everywhere. We compute the intercell fluxes. Locally, this approximately advects our solution at a certain speed. We now have a (roughly) piecewise constant solution that isn't aligned with the cell boundaries. This is the *evolve* step. To get back to our cell averages, the *average* step takes the cell average within each cell of our new solution.

In principle, most of these steps are exact. The averaging step is exact. The evolve step needs doing with some ODE solver, but that can be done to high accuracy. The evolve step also needs the computation of the intercell flux, but it's possible in simple situations to do that exactly. It's the reconstruction step that introduces the first order approximation. By enforcing that the solution is piecewise constant we significantly reduce the accuracy of the method.

To improve this, we need to improve the reconstruction. The next step up would be to use piecewise linear reconstruction: assuming the solution is a straight line, not necessarilly flat, within each cell. Then up to quadratic functions and higher order. This would give the improved accuracy we seek. Unfortunately it also introduces other problems when the true solution is discontinuous.

Here's a standard discontinuous function: it's piecewise constant with one jump. If we look for a Fourier series representation of this function then the partial sum gives us a representation that oscillates around the true solution. These oscillations are concentrated near the discontinuity.

There are three obvious ways to get around this. First, split the domain into smaller cells. However, we see that there's no scale to the true solution, so these oscillations will still appear. They'll get squeezed closer to the discontinuity, but their magnitude won't reduce.

Second we could include more terms in the partial sum. The result is the same as changing the cell size: the oscillations get squeezed closer to the discontinuity without getting smaller.

Finally, we could change the function basis. Instead of using a Fourier series we could expand in standard polynomials, or Legendre polynomials, or something else. This doesn't help either: these oscillations are a generic feature.

These *Gibbs oscillations* will destroy our numerical accuracy. They don't converge with resolution: typically they blow up in a few iterations. Most depressing is Godunov's theorem. It asks when the solution might be *monotone*: that means, when the solution lies between the minimum and maximum of the original solution. Godunov's theorem says that a linear algorithm that is monotone *must* be first order accurate.

We have one loophole left by Godunov's theorem. It only applies to *linear* methods: that is, methods where the algorithm essentially does the same thing everywhere, ignoring the values and form of the data. The past 50 years and more of CFD has focused on better ways of *locally modifying* the algorithm based on the values and form of the solution itself, to avoid Gibbs oscillations.

It's this nonlinearity that makes numerical methods for matter models so much more complex and expensive than numerical methods for smooth solutions (such as the spacetime). It's typical for the computational cost of the matter evolution to be greater than that of the spacetime evolution, even though we're usually evolving far fewer variables, sometimes by an order of magnitude.

### Slope limiting

The first nonlinear scheme to look at is slope limiting. We're still doing a reconstruct-evolve-average method. So we'll reconstruct our solution within each cell based on the cell averages within this cell and its neighbours. Then we'll compute the intercell flux, evolve, and average to get new cell averages. The new step is that the reconstruction within each cell will be piecewise linear, not piecewise constant.

We can approximate the slope inside each cell by forward, backward or central differencing. Central differencing uses more information and will be the most accurate in smooth regions. However, if we use two cells across a shock then we'll get oscillations. So what we want to do is compare the three different possible slopes. When it looks like we're in a smooth region we choose the slope from central differencing. When it looks like we're not in a smooth region we use piecewise constant reconstruction: the slope is zero. Then we want some smooth transition between the two extremes.

The easiest check for possible shocks or problems is to look for when forward and backward differencing gives slopes with different signs. The simplest approximate slope that works is to look just at the forward and backward (or upwind and downwind) slopes, and choose the *minmod* slope. That is, if the two slopes have different signs, the slope is set to zero. If they have the same sign, we choose the slope with smallest magnitude.

Minmod slope limiting combined with a higher-order ODE solver will work to give better than first order accuracy. Unfortunately it's not *much* better until we get to high resolution: the exercises give examples of this. Better slope limiters are available, but even the best won't do better than second order accuracy, a long way from the fourth order or better that we want.

### Finite difference methods

Trying to move to even higher order methods is complicated by an issue that our focus on one dimension has hidden to now: the computation of the intercell flux. Remember, in our finite volume approach, the cell average is updated by the surface integral of the flux over the cell boundary. Once we move to higher order reconstruction methods the solution, and hence the flux, varies over the surface of the cell. This means we can't evaluate it at a single point, as in one dimension: instead we must evaluate it at multiple points and approximate the surface integral.

The most efficent way of approximating an integral in general is Gauss quadrature, where approximating the integrand at $k$ points in each dimension gives us $(2 k - 1)^{\text{th}}$ order accuracy. For second order accuracy we need only one point - this is the midpoint rule. With two points we get third order accuracy, and with three points we get fifth order accuracy. However, this is per dimension: to get fifth order accuracy in three dimensions, where each cell face is two dimensional, we will need to reconstruct to 25 points on each face and solve 25 separate Riemann problems per face. The computational cost and complexity goes up very rapidly.

For this reason, high order finite volume methods are rare (although most methods in the field are finite volume methods, they aim for high absolute accuracy with second order convergence). To get higher accuracy, the standard approach in the field is to use finite differences.

In finite difference methods we still write the update formula *as if* we were computing intercell fluxes. This form, with its telescoping property, is necessary to get shock speeds correct. However, we're now interpreting these $f_{i \pm 1/2}$ terms differently. We don't need these terms to approximate the intercell fluxes, as in finite differences there are no cells, only the values of the solution at the central point. Instead we allow these half-integer terms to be anything, provided the difference $(f_{i+1/2} - f_{i-1/2})/(\Delta x)$ approximates the derivative of $f$ to the appropriate order. As everything is interpreted at the *grid point*, we automatically get the accuracy associated with the order of approximation of the derivative.

This appears to be wonderful. By directly dealing with the flux and not going through the solution we are bypassing all the issues with cells, intercell fluxes, and Riemann problems. Unfortunately this simple approach also throws away all the characteristic information and so is horribly unstable. By differencing simply without checking which direction the information is travelling in, we introduce Gibbs-like oscillations that rapidly kill the simulation.

So the standard approach is to use *flux splitting*. We compute the full flux at the grid point, $f(q_i)$. We then split it into two pieces, $f^{(\pm)}$, one of which travels to the left, and one of which travels to the right. This encodes some of the characteristic information. We then use a suitably upwinded reconstruction method on the split fluxes to get their values at the half-integer locations. Finally, we recombine the split fluxes to get the terms needed in the update formula.

The slide shows a simple flux splitting approach which, like the HLLE method, only uses some of the characteristic information. This sort of finite differencing approach is used by codes like Radice's WhiskyTHC to get the current most accurate simulations.

### Discontinuous Galerkin

There are two key computational problems with the higher order methods we've described to now.

The first is waste. The reconstruction used in both finite difference and finite volume methods takes a limited amount of information about the solution - the cell averages, or the point values - and produces a form of the solution everywhere, usually as a piecewise polynomial. This form is then used to compute some terms, such as the intercell fluxes, and then all the high order information is thrown away. We only store the values of the solution or its cell average.

The second problem is communication. To get enough information for a high-order approximation to the solution we need to look not just at the cell and its immediate neighbours, but to every further neighbouring cells. In general, we need to look at $k$ neighbours on either side to get $(2 k - 1)^{\text{th}}$ order accuracy. This is a real issue for big simulations on modern supercomputers.

As a quick digression. Simulations have essentially four things that can slow them down. The first is how fast it does operations: the FLOP count. The second is how much memory it has. The third is how fast results can be saved to disk. As the fourth, when we split the calculation across multiple processes, is how fast the different bits of the simulation communicate with each other.

On modern and near-future machines the main problem is communication speed. High order finite volume and finite difference schemes communicate too much information with cells too far away from themselves. This stops our simulations using the computational power available.

One answer to both these issues is to use a Discontinuous Galerkin method. HP will cover this in his talk on vacuum, so here I'll just touch on the features important to hydrodynamics.

First we have to revisit the weak form. In DG and other finite element methods we take the equations of motion, multiply by a *test function* $\phi$, and integrate by parts. This moves the spatial derivatives from the solution (which might be discontinuous) to the test function (which we can choose to be sufficiently differentiable).

We then expand the solution and the test function in terms of some function basis: think of Fourier Series, or Legendre polynomials. We're going to store the *modes*: the coefficients of the solution with respect to the function basis expansion. We end up with evolution equations for the modes, but these are *coupled* through the mass matrix and stiffness vector. These matrices and vectors can be pre-computed. We see there is a term that looks like the standard boundary flux, for which we'll need something like a Riemann solver.

DG methods don't have the communication or waste problems seen in finite volume or finite difference methods. They only couple a cell to its neighbours through the intercell flux. The high order reconstruction is automatic thanks to the mode information stored in each cell, which is evolved, not discarded between steps.

However, standard DG methods will produce Gibbs oscillations at shocks, as energy is shifted to higher modes. In order to avoid these oscillations it's necessary to limit the solution, as in slope limiting, without reducing the accuracy (too much). This is hard to do without introducing coupling between the neighbouring cells. Getting this step correct is going to be crucial for making DG methods work in relativistic matter models.

### MHD

In this final part of the lecture we need to look at the extra steps needed to evolve MHD, which is the main model for current simulations. The problem with MHD is not the flux terms, which can be evolved with the exact same techniques as we've discussed. The problem is not with the source terms (unless we include resistive effects). The problem is with the "div B" constraint, $\nabla \cdot {\bf B} = 0$.

Constraints are a fact of life in numerical relativity. They're useful as an independent measure of the accuracy of our simulation. However, some constraints, when violated, can destroy the simulation accuracy. It's been known for decades (even before Brackbill and Barnes did their key investigation) that MHD simulations violating the div B constraint would rapidly fail.

There are essentially two types of approach to solving this problem. We can modify the evolution equations so that the constraint violations are kept "small", by damping and propagating these constraints away. Alternatively, we design our numerical scheme so that the constraints are zero at the discrete level.

Constraint damping is the simplest approach. In essence, it works by adding additional terms, proportional to the constraint itself, so that the evolution equation for the constraint has its time derivative evolved by a term proportional to the constraint itself. Choosing the proportionality constant to be negative means the constraint is exponentially damped. To avoid feedback at specific points it's typical to add additional terms so that the constraint violations propagate as a wave equation.

The main advantage of constraint propagation is its simplicity. Adding one or two equations of motion for the constraints and a couple of extra source terms is easy to implement. The disadvantages can be substantial. It requires hand-tuning a parameter, the damping time. Its mathematical status is dubious - there's some results suggesting the modified system isn't properly well posed. The interaction of the violations with grid boundaries, particularly AMR grid boundaries, can be very messy. And finally, it's not clear how small the constraint violations need to be to not cause problems.

The preferred method now is to enforce the constraint at the discrete level. The favourite method at the moment is to *not* evolve the magnetic field directly, but instead to evolve the *vector potential* ${\bf A}$. We can always compute the magnetic field from the curl of the vector potential, and because the divergence of a curl automatically vanishes, this enforces the constraint.

The vector potential is not unique: by modifying the *EM* gauge we can change its value. This means different choices for the evolution equation for the vector potential can be made. As with constraint damping, it turns out that propagating the vector potential is better than trying to fix it for simplicity. This means the preferred method is to use a Lorenz (or generalize Lorenz) gauge.

It's useful to note that the vector potential must be continuous, as the magnetic field must be $C^0$, and the magnetic field goes like a derivative of the vector potential. So standard methods can be applied to the vector potential, or even methods that work for $C^1$ functions. However, in order to cleanly get the magnetic fields from the vector potential, and to get the terms needed for evolving the vector potential itself, its typical to discretely locate the vector potential at different locations to the other variables. Specifically, when thinking of the problem in finite volume form, the vector potential is stored at cell *edges*.

### Summary

The flux conservative form that we saw in the first lecture is essential for building numerical methods that deal with shocks correctly. Once that's in place we can improve are method by carefully considering how and where we are representing which variables. I think it's really important to learn the finite volume approach as a way of thinking about the key concepts. However, I also think that the medium to long term future of the field is moving towards finite difference or DG type methods, inspired by finite volume concepts.

For MHD and other models including EM fields it's important that the constraints that follow from Maxwells equations are imposed. When implementing a new code I always first reach for constraint damping methods due to their simplicity. However, it's definitely true that the most accurate and useful codes available now are using methods that enforce the constraints at the discrete level. Combining high order accuracy with constraint enforcement is a challenge.

## Lecture 3
