# Open Astrophysics Bookshelf exercises

The [Open Astrophysics Bookshelf](https://open-astrophysics-bookshelf.github.io/) contains a range of material for self-study, largely focused on numerical simulations for astrophysics. By and large the material is aimed at Newtonian problems. However, a lot of the key techniques carry over, so there's a lot worth looking at. The [Introduction to Computational Astrophysical Hydrodynamics](http://bender.astro.sunysb.edu/hydro_by_example/CompHydroTutorial.pdf) is the crucial text for our purposes.

There are two sets of codes associated with the key notes. Both are in Python.

1. [hydro_examples](https://github.com/python-hydro/hydro_examples) are standalone codes in one spatial dimension. Good for initial tests and checking that you understand the methods and their underlying behaviour.
2. [pyro](https://github.com/python-hydro/pyro2) is in two spatial dimensions. Covers a range of standard problems, but there's a lot of extensions you can make.

# Exercises

You can choose exercises to match your level of confidence and expertise.

## Never implemented an evolution code

Look at Chapter 4 of the notes, on the advection equation. Look at examples codes from [hydro_examples](https://github.com/python-hydro/hydro_examples). Check that you understand what the code is doing, and that you can extend it. Can you add initial data? Can you change boundary conditions? Do you know how to check convergence, and what it means?

## Done a simple advection code

Look at chapters 6 (Burgers) and 8 (Euler) of the notes and compare to examples from [hydro_examples](https://github.com/python-hydro/hydro_examples). Are you clear where shock capturing is important? Can you grasp the difference between scalar (Burgers) and system (Euler) cases? What's the difference in performance on capturing shocks versus contacts? How would this extend to more complex systems?

## Done second order HRSC codes

Look at the WENO schemes at the end of chapters 5, 6 and 7. Compare against the [hydro_examples](https://github.com/python-hydro/hydro_examples). Can you see how the code works? How would you change it to make it more efficient? Can you see the potential problems with moving to modelling neutron stars?

## Done a range of one dimensional problems

Look at the [pyro](https://github.com/python-hydro/pyro2) code. Test the advection problems and be sure you know how it works. How would you implement your own system? Can you implement, say, special relativistic hydrodynamics within pyro? Could you do Newtonian MHD?

## Done a range of HRSC methods on multiple models in more than one dimension

Take a look at [this branch of the notes](), end of chapter 5, for a detailed outline of Discontinuous Galerkin methods, and [this branch of the example codes]() for implementations for advection, Burgers and hydrodynamics. Ensure that you understand it and implement it on a new system. Can you work out how to extend it to higher dimensions?
