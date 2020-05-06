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

## Lecture 2
