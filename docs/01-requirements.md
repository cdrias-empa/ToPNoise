# 1. Requirements

**Make sure that:**

- your computer runs Ubuntu 24.04 LTS or a later Ubuntu release, 64-bit (x86_64);
- you have at least 10 GB of free disk space for the installation, and additional space for calculation results;
- you have a graphical desktop;
- you have administrator rights (`sudo`);
- ToPNoise is installed in your home directory.

## 1.1 Operating system

ToPNoise has been tested on **Ubuntu 24.04 LTS, on 64-bit PCs (x86_64 / amd64)**. The same installation procedure can be used on later Ubuntu releases provided that the `singularity-container` package is available.

To find out which system you have, open a terminal and type:

```bash
lsb_release -ds
uname -m
```

**Expected result**: the first command prints Ubuntu 24.04 LTS, a 24.04 point release, or a later Ubuntu release, and the second prints `x86_64`.

> **Windows users**: Ubuntu running inside Windows (WSL2, with its graphical support) can be used. It has been tried only briefly: the containers and the module windows start, but no full calculation has been checked.

## 1.2 Disk space

| What | Size |
|---|---|
| The four container images | about 6.9 GB |
| Extra space needed while the images are downloaded | about 2.6 GB |
| Free space needed for the installation | at least 10 GB |
| Your calculation results | depends on the calculation; the results of a full study can need several gigabytes |

> [!WARNING]
> **TODO:** Give a rough estimation of how much space is needed for a given standard case.

## 1.3 Computing power

The ToPNoise calculations are computationally demanding and can take from minutes to hours. We recommend having at least **8 CPU cores** and **64 GB of RAM**. More computational power will obviously reduce computation time.

## 1.4 Display

The ToPNoise launcher and the four modules use graphical interfaces and therefore require access to a display.

To check that a display is available, type:

```bash
echo $DISPLAY
```

**Expected result**: a value such as `:0`.

> [!WARNING]
> **TODO:** Remove the appendix on remote access until remote connection support is implemented and documented.

## 1.5 Programs that must be installed

The installation script (chapter 2) installs these programs for you. They are listed here so that you know what is on your computer.

| Program | Used for |
|---|---|
| **Singularity** | Runs the four modules in containers, which include the software dependencies required by each module |
| **Python 3** with **PyQt5** | Runs the launcher window |
| **xterm** | Each module is started in a terminal window, which stays open and shows its messages |
| **wget** | Downloads the images |

## 1.6 Where to install ToPNoise

> **Install the ToPNoise folder inside your Linux home directory**

The modules run inside Singularity containers. The home directory is directly accessible from the containers and can therefore be used to store input and output data. If the data are stored at another location, for example on a second disk or in another local directory, the launcher can make one selected folder available to all ToPNoise modules. This folder is mounted inside the containers as `/mnt/shared`.
