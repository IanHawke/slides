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
