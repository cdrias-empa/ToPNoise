# 1. Requirements

**Checklist for this chapter**

- [ ] My computer runs Ubuntu or Debian Linux, 64-bit (x86_64).
- [ ] I have at least 10 GB of free disk space for the installation, and more for my results.
- [ ] I have a graphical desktop (a screen, or a remote desktop).
- [ ] I have administrator rights (`sudo`) for the installation of a few system programs.
- [ ] I will install ToPNoise and keep my results in my **home directory**.

## 1.1 Operating system

ToPNoise runs on **Linux systems based on Debian or Ubuntu, on 64-bit PCs (x86_64 / amd64)**.

To find out which system you have, open a terminal and type:

```bash
lsb_release -ds
uname -m
```

**Expected result**: the first command prints the name of your distribution (for example `Ubuntu 22.04.3 LTS`), and the second prints `x86_64`.

<!-- TODO(fix pending G4): state the Ubuntu / Debian versions that the installer supports. The apt package `singularity-container` exists on Ubuntu 24.04 and later, not on 20.04 and 22.04. All the packages of the script resolve on 24.04 (simulated with apt); the script itself has not been run on 24.04, and the images have not been tried with SingularityCE 4.1.1. -->

> **Windows users**: Ubuntu running inside Windows (WSL2, with its graphical support) can be used. It has been tried only briefly: the containers and the module windows start, but no full calculation has been checked.

## 1.2 Disk space

| What | Size |
|---|---|
| The four container images | about 6.9 GB |
| Extra space needed while the images are downloaded | about 2.6 GB |
| **Free space needed for the installation** | **at least 10 GB** |
| Your calculation results | depends on the calculation; the results of a full study can need several gigabytes |

Check your free space with:

```bash
df -h ~
```

The column `Avail` is the free space on the disk that holds your home directory.

## 1.3 Computing power

ToPNoise runs calculations that can take from minutes to hours.

- The **Multi-Sleeper Model** is the most demanding: its window states that the **RAM** used can reach **15 GB or more**, and its default memory limit is 32 000 MB of RAM per job. It also runs several jobs at the same time, one for each frequency band.
- The Boundary Element module starts several calculation processes at the same time. Its default settings (15 processes for the rail, 9 for the sleepers, 20 for the wheel) suit a powerful computer. On a laptop, you must lower them (chapter 6).

<!-- TODO: measure the memory needed by one BEM calculation, and give the minimum RAM. -->
<!-- TODO(fix pending B7): the BEM default numbers of processes may exceed the memory of a workstation. -->


## 1.4 A graphical desktop

The four modules are graphical applications, so the computer needs a desktop with a screen. The launcher uses the X11 display system. On a modern Linux desktop that uses Wayland, X11 programs work through the compatibility layer called XWayland, which is normally installed.

To check that your session has a display, type:

```bash
echo $DISPLAY
```

**Expected result**: a short text such as `:0`. If the line is empty, your terminal has no access to a display; use a terminal opened from the desktop, or see the [appendix on remote access](appendix-remote.md).

## 1.5 Programs that must be installed

The installation script (chapter 2) installs these programs for you. They are listed here so that you know what is on your computer.

| Program | Used for |
|---|---|
| **Singularity** (SingularityCE 3.8 or later) | Runs the four modules in containers: each module comes with all the software it needs, so nothing else has to be installed |
| **Python 3** with **PyQt5** | Runs the launcher window |
| **xterm** | Each module is started in a terminal window, which stays open and shows its messages |
| **wget** | Downloads the images |

## 1.6 Where to install ToPNoise

> **Install ToPNoise in your home directory**, for example in `~/ToPNoise`, and choose output folders inside your home directory too.

The modules run in containers. A container sees your home directory, but not the other disks of the computer. A folder outside your home directory (a second disk, `/data`, a USB drive…) is invisible to the modules: they report that the folder does not exist, or they lose the files when they close.

<!-- TODO(fix pending G3): either document this as a permanent requirement, or have the launcher mount the ToPNoise folder explicitly. -->

## 1.7 Administrator rights

You need `sudo` once, during the installation, to install the system programs of section 1.5. You do not need it to run ToPNoise.
