# Multifluid talk

## Title slide

Thank you, and thank you for this opportunity to speak. The work here involves a number of analytical and physical modelling steps, led by Greg Comer and Nils Andersson, and also numerical implementation and simulation, led by Kiki Dionysopoulou. I'll outline both.

## Motivating movie

So, our motivation is better modelling of neutron stars, such as binary inspiral and merger as shown by this movie by Kiki.  In particular, how complex does the model need to be for multimessenger astronomy, where we want self-consistent calculations of both gravitational wave *and* electromagnetic signals. In the movie here a nonlinear GRMHD simulation is shown, including resistivity. It's the problem of going beyond ideal MHD, but doing it in a consistent and general fashion, that I'll focus on here.

## MHD is not enough

Most state-of-the-art nonlinear simulations are using ideal MHD, with few examples such as Palenzuela and collaborators or Dionysopoulou and collaborators going further by including a phenomenological resistivity. This is a problem: whilst the NS core and exterior are both expected to satisfy the MHD assumptions, it's for rather different regions. Matching interior and exterior to get a self-consistent simulation that would allow us to extract EM signals remains a serious problem. Equally, whilst resistive and dissipative terms are expected to be small on average, their *local* impact can be significant, and on important parts of the dynamics. Dionysopoulou, for example, has shown significant changes on post-merger dynamics due to resistivity.

## State of the art

To go beyond ideal MHD there are essentially two directions one can go. The first, as pioneered by Palenzuela and Dionysopoulou in full nonlinear GR, is to take the full nonlinear GRMHD equations and add a resistive term. This has the major advantage of conceptual simplicity and continuity with existing code, although the presence of stiff source terms in the equations somewhat negates that. You can also tailor your phenomenological resistivity to mitigate problems when transitioning from interior to exterior. However, it's unclear exactly what underlying microphysics is being included in this case.

Sticking with single fluid MHD, a more motivated model has been derived by Khanna, Gammie and collaborators. This starts from the Israel-Stewart model and closes the higher order moments in the gradient expansion by linking fluid terms to the magnetic field. Here, it's much clearer what the physics input is. However, this model is very much tailored towards particular physical problems - accretion onto a black hole in a fixed background spacetime - and it's not clear how to extend it to cover the neutron star case.

A qualitative alternative is the multifluid approach. Here each individual particle species (electrons, protons, neutral carriers) have their own, individual fluid velocities. Interactions between the different "fluids" specify the microphysics input. The charge current is naturally given by sum of the "fluid" currents of charged species, and combined with Maxwell's equations a complete system should follow. In the best case there's no need to specify Ohm's law or the behaviour of heat, as both should follow from the equations of motion.

The closest to realizing this complicated goal is the work on *SR* multifluid plasmas, led by Amano and collaborators and Barkov and collaborators. Again, this is aimed at modelling plasmas for accretion-type problems. They evolve the equations for both charged species, but use a phenomenological resistivity and heat model to close the system.

That leaves the bottom right half of the table free: a multifluid, self-consistent model in full GR.

## Formulation

To get our GR formulation we start from an action principle: this will ensure consistency. The master function for the action - essentially the equation of state - will be specified in terms of the "n squareds": the magnitudes of the number currents and their cross products, and also a vector potential. The number currents are related to a volume form on a reference space: this constrains the variations of the number current. Varying with respect to the number currents gives the "fluid" equations of motion; varying with respect to the vector potential gives Maxwell's equations. The conjugate momenta - the mu's - need not be aligned with their number currents. This is the entrainment effect, where the species interactions encoded in the equation of state "drag" the fluid in a different direction.

This is all standard steps in deriving relativistic hydro. The key step, found by Andersson and Comer, is how the reference spaces interact. The volume element on the reference space is attached to the flow for the associated fluid, and "measures" the number of particles in that fluid element. To model microphysical interactions, we can make either the mapping to the reference space or the volume element itself depend on the reference spaces of other fluids: formally the coefficients of the volume element on space X depend on the coordinates of space X and also other spaces Y. Working this through the variational analysis gives additional terms in the equations of motion, which take the form of dissipation, resistivity and particle creation. In particular, the dissipation and resistivity terms are *in principle* given by the equation of state and the reference space volume elements (although this is unlikely to be useful in a practical calculation).

## Equations of motion

Here are the explicit equations of motion in a high level form. Each separate species is labelled with an "X" which could be electrons, protons, heat, or some other neutral carrier. The continuity equation gains a particle creation term. Euler's equation relates the force applied to the fluid element to the "rocket term" - the momentum gained or lost when particles are created - and the resistivity on the right hand side. The Lorentz force is already included in the force term as the conjugate momenta - the mu's - includes a term from the vector potential. Maxwell's equations are unchanged.

At this stage we could write down a phenomenological closure by specifying what the particle creation rates - the Gamma's - and the resistivity are. This is essentially what Amano, and Barkov, and co have done: it's possible to check that by restricting to flat space and simplifying the equation of state this formalism reduces to their equations, once their choice of resistivity is made. However, the variational calculation and the link to the reference spaces gives additional information that can be used as constraints. In particular, we can use these constraints to check how "inaccurate" simulations with phenomenological approaches are.

Some of the consequences of these constraints are high level but with an obvious physical interpretation. For example, the resistivity terms are given by velocity differences: suitably projected, this ensures there's no resistance when the fluids move together. The equations of motion directly link particle creation and resistivity as the force term is orthogonal to its own current: as we'd usually expect the particle creation rate to be observable and hence specifiable in our model, this constrains one degree of freedom in the resistivity. By adding obvious physical constraints - that the model must be invariant under changes in EM gauge, and imposing the second law of thermodynamics - we can then constrain the coefficients of the velocity differences in the resistivity. In particular, they must be symmetric and non-positive.

These constraints immediately restrict the type of models that make sense. In particular, two fluid models without heat or particle creation can't have non-trivial resistivity. Also, models that are linearized in velocity differenes can't have particle creation. Suitable limits of more complex models do give reasonable interpretations - treating heat as an additional fluid where there is entropy creation, but where that term is small compared to the bulk entropy, is one approach.

## The code

The code that Kiki implemented is a simplification of the full model. In particular, the equation of state has no entrainment, leading to partial pressures. The results I'll show here also use the phenomenological resistivity term to allow comparison to Barkov's results, or to ideal MHD. Based on the Einstein Toolkit, it's a 3d nonlinear code which can use explicit or IMEX time integrators and high order energy-stable WENO reconstruction. On smooth, 1d tests we get convergence at the expected orders - 2nd, 3rd or 5th depending on the method used - whilst in most "realistic" simulations we get 2nd order convergence.

We start with a comparison to ideal MHD: the standard Orzag-Tang problem. On the left half of each plot you see the ideal MHD result, and on the right that from the multifluid code. We're clearly getting the expected ideal limit.

The next test is again special relativistic - it's a drift-kink instability. This shows the growth of a genuinely multifluid instability, with the associated magnetic field given by the arrows. Of particular importance for our work is how it captures the shocks that form by the end of the simulation, and how this result matches with tests by Barkov.

Finally, we look at the collapse of a neutron star to a black hole, and the associated EM emission. This scenario was investigated by Dionysopoulou and collaborators with their phenomenological resistive code. That calculation showed that charge neutrality held to high accuracy globally, and that much of the EM emission was generated close to the horizon. Using the multifluid constraints it's possible to check the *local* violation of charge neutrality with this model, and in the regions where the EM signal is generated this can be significant. We can apply the multifluid code to this problem as well, and it successfully evolves through collapse to horizon formation, whilst retaining local charge neutrality. Work to look at the impact on the emitted EM signals is ongoing.

## Conclusions

In summary, GR multifluids may be complex, but it is practical and possible to simulate strong field scenarios beyond standard GRMHD.
