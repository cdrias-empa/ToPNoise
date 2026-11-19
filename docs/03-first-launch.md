# 3. First launch

**Checklist for this chapter**

- [ ] I have started the launcher from a terminal opened inside the desktop.
- [ ] The window called `ToPNoise` shows four buttons.
- [ ] Each of the four buttons opens a terminal window and the window of its module.
- [ ] I know where to read the messages of a module.

## 3.1 Start the launcher

Open a terminal, go to the `ToPNoise` folder, and start the launcher:

```bash
cd ~/ToPNoise
bash run.sh
```

**Expected result**: a window called **ToPNoise** opens, with the subtitle *Tool for the Prediction of Railway Noise* and four buttons.

![The ToPNoise launcher](images/03-01-launcher.png)

*Figure 3.1 — The launcher. The four buttons start the four modules (the numbers are those of section 3.2).*

Keep the terminal in which you typed `bash run.sh` open. It shows the messages of the launcher, and closing it closes the launcher.

If the window does not open, see chapter 9.

## 3.2 The four buttons

| Number in Figure 3.1 | Button | Module | Chapter |
|---|---|---|---|
| 1 | **Multi-Sleeper Model** | Vibration of the track | [4](04-track.md) |
| 2 | **Wheelset FE** | Vibration of the wheelset | [5](05-wheelset.md) |
| 3 | **Boundary Element** | Sound radiation | [6](06-bem.md) |
| 4 | **Post-processing** | Contact force, rolling noise, pass-by | [7](07-postprocessing.md) |

Each button does two things:

1. it opens a **terminal window** (xterm), and
2. in this terminal, it starts the module inside its container. The window of the module appears a few seconds later.

You can start one module at a time or several, and leave the launcher open while you work.

## 3.3 Try the four modules

Click each button once to check that the module opens.

1. Click **Multi-Sleeper Model**. A terminal window opens, then the window of the module.
2. Close the window of the module, then the terminal window that was opened with it.
3. Do the same with **Wheelset FE**, **Boundary Element** and **Post-processing**.

**Expected result**: for each button, a terminal window and a module window appear. No calculation is started: the modules only wait for your inputs.

> **The terminal window of a module must stay open while you use the module.** It is also the place where the module writes its messages, including its error messages. When a module does not behave as expected, read the last lines of its terminal window first.

<!-- TODO(fix pending G2): the Boundary Element module needs the ToPNoise folder as an argument, and a folder `runtime` inside it. The launcher of version 1.0.0-beta passes neither, so this module stops at once with "TopNoise root directory was not provided by the launcher". Remove this comment when the launcher passes the folder and the folder is created automatically. -->

<!-- TODO(fix pending G6): the Post-processing module does not start if the user has installed Python packages (numpy, h5py…) with `pip install --user` for Python 3.12: they hide the packages of the container. The terminal shows `ImportError … h5py` or `numpy.dtype size changed`. Remove this comment when the images (or the launcher) isolate the containers from `~/.local`. -->

<!-- TODO(fix pending G1): the launcher of version 1.0.0-beta mounts /mnt/results, which must exist on the computer, otherwise no module starts. Remove this comment when the launcher no longer requires it. -->

## 3.4 What the launcher creates

The modules store their working queues in a folder called `runtime` inside the `ToPNoise` folder. You do not need to open it, and you can delete it when no module is running: it is created again when needed.

<!-- TODO(fix pending B8): the Boundary Element module does not create `runtime` itself. Check the statement above once the launcher or the module creates it. -->

## 3.5 Close everything

Close the module windows first, then the terminal windows of the modules, then the launcher window. The terminal in which you typed `bash run.sh` becomes free again.
