# 2. Installation

**Checklist for this chapter**

- [ ] I have downloaded ToPNoise and extracted it in my home directory.
- [ ] I have installed Singularity, `xterm` and PyQt5 with the installation script.
- [ ] I have downloaded the four container images into the `images` folder.
- [ ] The four checks of section 2.4 give the expected result.

Open a terminal for all the commands of this chapter. In a graphical desktop, look for an application called *Terminal*.

## 2.1 Download ToPNoise

1. Open the ToPNoise page on GitHub in your web browser.
2. Click **Code**, then **Download ZIP**.
3. Move the downloaded file to your home directory and extract it. In the file manager, right-click the file and choose *Extract here*. In a terminal, type:

   ```bash
   cd ~
   unzip ToPNoise-main.zip
   ```

   If the terminal answers `unzip: command not found`, install the program first with `sudo apt install unzip`.

4. The extracted folder is called `ToPNoise-main`. You can rename it; the rest of this guide calls it `ToPNoise`:

   ```bash
   mv ToPNoise-main ToPNoise
   cd ~/ToPNoise
   ```

**Expected result**: the command `ls` shows the files `README.md` and `run.sh`, and the folders `setup` and `toolboxlauncher`.

> **All the commands in the rest of this guide are typed from the `ToPNoise` folder**, unless the text says otherwise.

## 2.2 Install Singularity and the other programs

The script `setup/install_singularity_linux.sh` installs Singularity, `xterm`, PyQt5 and the other programs of section 1.5.

```bash
bash setup/install_singularity_linux.sh
```

- The script asks for your password (administrator rights), and downloads and installs packages. This takes a few minutes.
- If it asks `Do you need to install Go (programmation laguange) ?[y/n]`, answer `n`.

<!-- TODO(fix pending G4): the script runs `sudo apt-get install -y singularity-container`; this package is not available on Ubuntu 22.04, and the script does not stop when a command fails. Rewrite this section once the installation of Singularity is fixed, and remove the question about Go if it is removed from the script. -->

**Expected result**: the script ends with the line `Installation of singularity completed`, and no error message appears before it.

## 2.3 Download the container images

The four modules are distributed as **container images**: large files (`.sif`) that contain each module with all the software it needs. They are not part of the ZIP file.

```bash
bash setup/download_images.sh
```

The script creates a folder called `images` and downloads four files into it. The download is about 6.9 GB, so it can take a long time.

| File | Module | Size |
|---|---|---|
| `MultiSleeperModel.sif` | Multi-Sleeper Model | about 2.0 GB |
| `WheelToolbox.sif` | Wheelset FE | about 1.9 GB |
| `topnoisebem.sif` | Boundary Element | about 2.6 GB |
| `Postprocessing.sif` | Post-processing | about 0.4 GB |

The image of the Boundary Element module is too large to be stored as one file on the download page. The script downloads it in two parts, `topnoisebem.sif.part1` and `topnoisebem.sif.part2`, joins them into `topnoisebem.sif`, and deletes the two parts.

<!-- TODO(fix pending G5): the download URLs of the script currently return HTTP 404 (no release is published). Publish the release, and make the script resume an interrupted download (`wget -c`), check the free disk space, and check the files with checksums. -->

### If you already have the files

If you received the images by another way, put the four `.sif` files into the folder `~/ToPNoise/images` (create it with `mkdir -p images`). If the Boundary Element image came in two parts, join them yourself and delete the parts:

```bash
cd ~/ToPNoise/images
cat topnoisebem.sif.part1 topnoisebem.sif.part2 > topnoisebem.sif
ls -l topnoisebem.sif
```

The size of `topnoisebem.sif` must be exactly the sum of the sizes of the two parts. When it is, delete the parts:

```bash
rm topnoisebem.sif.part1 topnoisebem.sif.part2
cd ~/ToPNoise
```

## 2.4 Check the installation

Type these four commands, one after the other, from the `ToPNoise` folder.

**Check 1 — Singularity is installed**

```bash
singularity --version
```

**Expected result**: a line such as `singularity-ce version 3.8.1`. The version must be 3.8 or later.

**Check 2 — the programs of the launcher are present**

```bash
python3 -c "import PyQt5" && which xterm
```

**Expected result**: a line such as `/usr/bin/xterm`, and no error message from Python.

**Check 3 — the four images are in place**

```bash
ls -lh images
```

**Expected result**: exactly four `.sif` files and no `.part` file. The command `ls -lh` shows sizes in binary units, so they look slightly smaller than in section 2.3: about `1.9G` for `MultiSleeperModel.sif`, `421M` for `Postprocessing.sif`, `1.8G` for `WheelToolbox.sif` and `2.4G` for `topnoisebem.sif`.

**Check 4 — the four images can be started**

```bash
for m in MultiSleeperModel WheelToolbox topnoisebem Postprocessing; do
  singularity exec images/$m.sif true && echo "$m: OK"
done
```

**Expected result**: four lines, `MultiSleeperModel: OK`, `WheelToolbox: OK`, `topnoisebem: OK` and `Postprocessing: OK`. Starting each image can take a few seconds.

If one check fails, see chapter 9. Otherwise, go to [chapter 3](03-first-launch.md).

<!-- TODO: replace these four checks by the script `setup/check_setup.sh` once it exists (it should also check the display and the free disk space). -->
