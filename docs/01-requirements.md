# 1. Requirements

## 1.1 Operating system

ToPNoise has been tested on **Ubuntu 24.04 LTS, on 64-bit PCs (x86_64 / amd64)**. Later Ubuntu releases may also be used provided that the packages required by the installation script are available.

To check your operating system and architecture, open a terminal and type:

```bash
lsb_release -ds
uname -m
```

**Expected result**: the first command prints Ubuntu 24.04 LTS, a 24.04 point release, or a later Ubuntu release, and the second prints `x86_64`.

> **Windows users**: Ubuntu running inside Windows using WSL2 can also be used. It has been tested only briefly: the containers and the module windows start, but no full calculation has been checked.

## 1.2 Disk space

At least **10 GB of free disk space** is required for the ToPNoise installation. Additional disk space is required for calculation results. Depending on the calculation, the results of a full study can require several gigabytes.

## 1.3 Computing power

The ToPNoise calculations are computationally demanding and can take from minutes to hours. We recommend having at least **8 CPU cores** and **64 GB of RAM**. More computational power will reduce computation time.

## 1.4 Display

The ToPNoise launcher and the four modules use graphical interfaces and therefore require access to a display.

To check that a display is available, type:

```bash
echo $DISPLAY
```

**Expected result**: a value such as `:0`.

> [!WARNING]
> **TODO:** Remove the appendix on remote access until remote connection support is implemented and documented.

## 1.5 Internet connection

An internet connection is required during the installation to download the required system packages and the ToPNoise container images.

## 1.6 Administrator rights

Administrator rights (`sudo`) are required during the installation to install the necessary system packages.
