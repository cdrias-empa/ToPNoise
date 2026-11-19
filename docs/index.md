# ToPNoise — step-by-step guide

ToPNoise (**To**ol for **P**rediction of railway **N**oise) is an open-source framework for predicting railway rolling noise. It combines finite-element models of the track and of the wheelset, a boundary-element model for the sound radiation, and a post-processing module that turns the results into rolling-noise spectra and pass-by signals.

This guide takes you from a computer without ToPNoise to a complete rolling-noise calculation. Each chapter starts with a short checklist of what you must have done before moving on.

## What you need to know

- **Finite elements and railway engineering**: you should know what a frequency response function (FRF), a modal analysis, and wheel–rail roughness are. The guide explains the tools, not the theory.
- **A terminal**: the installation uses a few commands, which the guide gives in full. No Linux administration knowledge is needed beyond typing them.

## How the tools fit together

ToPNoise is made of four modules. Each one is a graphical application, started from one window (the launcher).

| Module | What it computes | Main results |
|---|---|---|
| **Multi-Sleeper Model** (chapter 4) | Vibration of the track (rail, pads, sleepers, ballast) under a force at the wheel–rail contact | Contact FRFs of the track, vibration of the rail and the sleepers |
| **Wheelset FE** (chapter 5) | Vibration of the wheelset under a force at the contact | Contact FRFs of the wheel, vibration of the wheel surface |
| **Boundary Element** (chapter 6) | Sound radiated by the rail, the sleepers and the wheel | Sound pressure at receivers, per newton of contact force |
| **Post-processing** (chapter 7) | Wheel–rail contact force, rolling noise, train pass-by | Noise spectra and signals at the receivers |

The modules are used in this order, because each one needs the results of the previous ones:

```
 Multi-Sleeper Model --> vibration of rail and sleepers -----+
                                                              |
 Wheelset FE ----------> vibration of the wheel surface -----+
                                                              v
                                                     Boundary Element
                                                              |
                                              acoustic transfer functions
                                                              |
 Multi-Sleeper Model --> contact FRFs of the track -----------+
 Wheelset FE ----------> contact FRFs of the wheel -----------+
 Roughness of rail and wheel --------------------------------+
                                                              v
                                                      Post-processing
                                                              |
                                        contact force, rolling noise, pass-by
```

## Checklist for the whole guide

Tick the boxes as you go.

- [ ] **Chapter 1 – Requirements**: your computer meets the requirements.
- [ ] **Chapter 2 – Installation**: Singularity and the other programs are installed, and the four container images are downloaded.
- [ ] **Chapter 3 – First launch**: the launcher opens, and the four modules start.
- [ ] **Chapter 4 – Track**: the Multi-Sleeper Model has produced the track results.
- [ ] **Chapter 5 – Wheelset**: the Wheelset FE module has produced the wheel results.
- [ ] **Chapter 6 – Boundary Element**: the acoustic transfer functions are computed.
- [ ] **Chapter 7 – Post-processing**: the contact force, the rolling noise and the pass-by are computed.
- [ ] **Chapter 8 – Worked example**: you have reproduced the complete example.

## Contents

1. [Requirements](01-requirements.md)
2. [Installation](02-install.md)
3. [First launch](03-first-launch.md)
4. [Track: Multi-Sleeper Model](04-track.md)
5. [Wheelset: finite-element model](05-wheelset.md)
6. [Radiation: Boundary Element](06-bem.md)
7. [Post-processing: contact force, rolling noise, pass-by](07-postprocessing.md)
8. [Worked example](08-end-to-end.md)
9. [Troubleshooting](09-troubleshooting.md)
10. [Appendix: remote access](appendix-remote.md)

## Conventions used in this guide

- Commands you type in a terminal are shown in grey boxes, like this:

  ```bash
  ls
  ```

- **Expected result** boxes tell you what you should see. If you see something different, stop and check chapter 9.
- Names written like `this` are file names, folder names, or text in a window.
