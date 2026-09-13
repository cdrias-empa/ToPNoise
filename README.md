# ToPNoise

ToPNoise (**To**ol for **P**rediction of railway **N**oise) is an open-source framework for predicting railway rolling noise.

It uses the [RailTrackModellingToolbox](https://github.com/jcugnoni-heig/RailTrackModellingToolbox) to compute the structural response of the track. The resulting vibration fields of the rail and sleepers are then used in a Boundary Element (BE) calculation with [Bempp-cl](https://github.com/bempp/bempp-cl).

ToPNoise provides a graphical user interface that brings together the structural, acoustic, and post-processing tools required for the rolling-noise calculation.

## Modules

ToPNoise is organized into four main modules.

### 1. Structural Response of the Track

The structural response of the track is calculated using the Multi-sleeper FE model from the [RailTrackModellingToolbox](https://github.com/jcugnoni-heig/RailTrackModellingToolbox).

It is a large-scale 3D structural model of a railway track with an arbitrary number of sleepers. Frequency-dependent dynamic substructuring is used to efficiently evaluate the vibration response of the rail and sleepers in detail.

The model also allows undersleeper pads to be included.

### 2. Structural Response of the Wheels

The structural response of the wheels is calculated using a finite-element model implemented with *Code_Aster*.

The 3D model includes three types of wheelsets with their detailed geometries.

### 3. Noise Radiation

The acoustic radiation from the vibrating railway components is calculated using the Boundary Element Method with [Bempp-cl](https://github.com/bempp/bempp-cl).

The vibration responses obtained from the structural models are used as input to the acoustic calculation.

### 4. Rolling-Noise Post-processing

The post-processing module calculates the wheel-track interaction and combines the structural and acoustic results to obtain the rolling-noise response.

It uses the wheel and track frequency-response functions to calculate the wheel-rail contact forces and applies these forces to the acoustic responses obtained from the Boundary Element calculations.

## Installation

ToPNoise is currently intended for Linux systems based on Debian/Ubuntu on x86_64/amd64 architecture.

The individual ToPNoise modules are distributed as Singularity container images and are launched through the main ToPNoise graphical interface.

### 1. Download ToPNoise

Download the repository from GitHub using **Code → Download ZIP**, then extract the archive.

After extraction, open a terminal in the `ToPNoise` directory.

### 2. Download the container images

From the `ToPNoise` directory, run:

```bash
bash setup/download_images.sh