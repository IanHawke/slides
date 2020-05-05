# Script for lectures at ICTS

## Lecture 1

### The goal

For many of us studying numerical relativity and relativistic hydrodynamics the motivation is gravitational waves. The goal was to observe these and use them to tell us about gravity, relativity, and the physics of extreme objects.

With the detection of black hole mergers in 2015, and neutron star mergers from 2017, the goal is now reality. The object now is to squeeze the maximum possible information from these observations, through better modelling. Full, quantitative modelling of neutron star mergers needs numerical simulation, which is going to be the focus of these lectures.

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

### The shortcut

Let's look at a simulation using a single perfect fluid with magnetic field. This simulation is from Bruno Giacomazzo's group. It ignores dissipation, viscosity, heat transport, magnetic resistivity, superfluidity, superconductivity, the elastic crust of the neutron star, and any radiation transport. It includes full general relativity, models the star as a hot fluid, and adds an ideal electromagnetic field.

Initially the stars inspiral due to the emission of gravitational waves. Around $15$ms after the start of the simulation the stars merge. At this point things get messy. When the stars smash into each other a shock propagates through the merged object, massively increasing the temperature. At the same time the magnetized material "slips" past its companion, winding up the total magnetic field in a dynamo effect. The remnant tries to settle down, with some material expelled from the system. But the object is too massive to support itself, and at around $30$ms the core collapses to a black hole. Most of the dense matter is rapidly swallowed into the black hole, leaving a small fraction at larger radius to settle into a disk. It's believed that the kilonova occurs when this remaining matter collapses back on the black hole.

We see that we need to model the fluid interior and the vacuum exterior. We need to model the shock as the stars smash together, and the resulting jump in temperature. We need to model the small scale structure in the interior as the magnetic fields wind up, forming the precursor to the jet. And we need to do this on top of evolving the spacetime, tracking any black holes that might appear.

See also https://www.youtube.com/watch?v=UQCfo5L3ShQ (https://arxiv.org/abs/1809.11161, Radice et al) or https://www.youtube.com/watch?v=Dyn9KbB_zeo (Dietrich et al)

**Break at this point**: a bit over 25 minutes to here. Include David's video as well.

## Lecture 2
