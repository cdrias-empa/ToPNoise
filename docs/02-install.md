# 2. Installation

## 2.1 Download ToPNoise

Open the ToPNoise repository on GitHub, click **Code**, and select **Download ZIP**.

Extract the downloaded ZIP file somewhere inside your Linux home directory.

The extracted folder is initially called `ToPNoise-main`. Rename it to `ToPNoise`.

Open a terminal and move to the folder where you extracted ToPNoise:

```bash
cd /path/to/ToPNoise
```

All commands in the following sections are run from the ToPNoise folder.

## 2.2 Install Singularity and the required system programs

The script `setup/install_singularity_linux.sh` installs Singularity and the system programs required to run ToPNoise.

Run:

```bash
bash setup/install_singularity_linux.sh
```

The script uses `sudo` to install the required system packages and may therefore ask for your password.

## 2.3 Download the container images

The four ToPNoise modules are distributed as Singularity container images (`.sif`). These images contain the dependencies required by each module and are not included in the ToPNoise source code.

Download them with:

```bash
bash setup/download_images.sh
```

The script creates the `images` folder and downloads the four container images from the latest ToPNoise GitHub release.

The Boundary Element image is distributed in two parts. The script downloads both parts, joins them automatically into `topnoisebem.sif`, and removes the temporary files afterwards.

**Expected result**: the script finishes with:

```text
ToPNoise container images downloaded successfully.
```

The `images` folder should contain:

```text
images/
├── MultiSleeperModel.sif
├── WheelToolbox.sif
├── topnoisebem.sif
└── Postprocessing.sif
```

If you already have the four container images, place them directly in the `images` folder and skip the download step.

If the installation and download complete without errors, continue to [chapter 3](03-first-launch.md) to start ToPNoise for the first time.
