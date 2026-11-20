# 2. Installation

## 2.1 Download ToPNoise

Open the ToPNoise repository on GitHub, click **Code**, and select **Download ZIP**.

Extract the downloaded ZIP file somewhere inside your Linux home directory.

The extracted folder is initially called `ToPNoise-main`. Rename it to `ToPNoise`.

Open a terminal and move to the folder where you extracted ToPNoise:

```bash
cd /path/to/ToPNoise
```

All commands in the following section are run from the ToPNoise folder.

## 2.2 Install ToPNoise

Run the installation script:

```bash
bash setup/install_singularity_linux.sh
```

The script installs Singularity and the system programs required to run ToPNoise. It uses `sudo` and may therefore ask for your password.

**Expected result**: the installation finishes with:

```text
Installation of singularity completed
```

Then download the four ToPNoise container images:

```bash
bash setup/download_images.sh
```

The script creates the `images` folder and downloads the container images from the latest ToPNoise GitHub release.

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

If the installation completes without errors, continue to [chapter 3](03-first-launch.md) to start ToPNoise for the first time.
