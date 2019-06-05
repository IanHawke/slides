# Summary of the discussion

## Recap of the session

A lot of the discussion really took place in the questions of the talks. A quick summary of those:

* Shibata: Inspiral phase is well under control, if sufficient resolution used (few do). Need <100m grid size for 0.1rad accuracy. For NS binaries, there remain numerical issues at merger, especially with magnetic fields. Now considers it likely that going beyond ideal (M)HD is needed for post-merger phase. NS/BH works fine.
* Nagar: EOB pipeline well tested for BBHs. There are numerical issues that need acknowledging to ensure sufficient accuracy for the inspiral, but this can be done.
* Hinderer: Similar to Nagar, but looks at NS/BH. Here there are more issues as mass ratio and spin effects likely to be more important, and this isn't what EOB is well-tuned to, so more high-accuracy high-physics-input numerical simulations are needed to validate.
* Palenzuela: Non-ideal MHD for multi-messenger. Shows that the numerics can be done, but emphasizes the number of assumptions that go into getting the emitted luminosity (to do it properly you'd need at least a full reaction network calculation).
* Giacomazzo: Impact of (ideal) magnetic fields are currently small when "physical" field strengths used; eg 10% shift in frequencies in remnant (see Bauswein), although needs higher resolution to check this.
* Bauswein: post-merger GW frequencies are robustly linked to EOS.

## Discussion

The discussion session covered two main areas.

1. Numerical accuracy as shown by the code comparison study of Radice et al, which Tim Dietrich spoke to. This re-emphasized the control of the inspiral phase (whilst noting the need for sufficient resolution to capture it to 0.1rad accuracy) and the lack of control of the post-merger phase. There were comments about initial data issues and eccentricity, but much of the discussion was around post-merger issues and what could be said: "very little", seemed to be the conclusion.
2. The need for EOB or similar effective waveforms for the inspiral phase, and how to get them from matching to simulations. There was a push for a Matter-NINJA effort to get the numerical groups to start providing the right information for data analysis - this was pushed both by data analysis people and some involved in the numerical BBH effort, who said it had been extremely helpful. The code comparison effort above is a step in this direction; the question is how many groups want to be involved. There were two particular dissenters: some NR people (particularly Shibata) had other physics drivers and wouldn't spend the time, and some EOB people (particularly Nagar) thought the pipeline set up in the BBH case would work without change, and that many numerical waveforms would just confuse matters: only one "best" waveform was needed. No clear conclusion was reached.
