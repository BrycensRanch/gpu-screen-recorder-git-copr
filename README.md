![](https://dec05eba.com/images/gpu_screen_recorder_logo_small.png)

# GPU Screen Recorder
This is a screen recorder that has minimal impact on system performance by recording your monitor using the GPU only,
similar to shadowplay on windows. This is the fastest screen recording tool for Linux.

This screen recorder can be used for recording your desktop offline, for live streaming and for nvidia shadowplay-like instant replay,
where only the last few minutes are saved.

This is a cli-only tool, if you want an UI for this check out [GPU Screen Recorder GTK](https://git.dec05eba.com/gpu-screen-recorder-gtk/) or if you prefer a ShadowPlay-like UI then check out [GPU Screen Recorder UI](https://git.dec05eba.com/gpu-screen-recorder-ui/).

Supported video codecs:
* H264 (default)
* HEVC (Optionally with HDR)
* AV1 (Optionally with HDR. Not currently supported on NVIDIA if you use GPU Screen Recorder flatpak)
* VP8
* VP9

Supported audio codecs:
* Opus (default)
* AAC

## Note
This software works on X11 and Wayland on AMD, Intel and NVIDIA.
### TEMPORARY ISSUES
1) screen-direct capture has been temporary disabled as it causes issues with stuttering. This might be a nvfbc bug.
2) Videos are in variable framerate format. Use MPV to play such videos, otherwise you might experience stuttering in the video if you are using a buggy video player. You can try saving the video into a .mkv file instead as some software may have better support for .mkv files (such as kdenlive). You can use the "-fm cfr" option to to use constant framerate mode.
3) FLAC audio codec is disabled at the moment because of temporary issues.
### AMD/Intel/Wayland root permission
When recording a window or when using the `-w portal` option under AMD/Intel no special user permission is required,
however when recording a monitor (or when using wayland) the program needs root permission (to access KMS).\
This is safe in GPU Screen Recorder as the part that needs root access has been moved to its own small program that only does one thing.\
For you as a user this only means that if you installed GPU Screen Recorder as a flatpak then a prompt asking for root password will show up when you start recording.
# Performance
On a system with a i5 4690k CPU and a GTX 1080 GPU:\
When recording Legend of Zelda Breath of the Wild at 4k, fps drops from 30 to 7 when using OBS Studio + nvenc, however when using this screen recorder the fps remains at 30.\
When recording GTA V at 4k on highest settings, fps drops from 60 to 23 when using obs-nvfbc + nvenc, however when using this screen recorder the fps only drops to 58.\
GPU Screen Recorder also produces much smoother videos than OBS when GPU utilization is close to 100%, see comparison here: [https://www.youtube.com/watch?v=zfj4sNVLLLg](https://www.youtube.com/watch?v=zfj4sNVLLLg).\
GPU Screen Recorder has much better performance than OBS Studio even with version 30.2 that does "zero-copy" recording and encoding, see: [https://www.youtube.com/watch?v=jdroRjibsDw](https://www.youtube.com/watch?v=jdroRjibsDw).\
It is recommended to save the video to a SSD because of the large file size, which a slow HDD might not be fast enough to handle. Using variable framerate mode (-fm vfr) which is the default is also recommended as this reduces encoding load. Ultra quality is also overkill most of the time, very high (the default) or lower quality is usually enough.
## Note about optimal performance on NVIDIA
NVIDIA driver has a "feature" (read: bug) where it will downclock memory transfer rate when a program uses cuda (or nvenc, which uses cuda), such as GPU Screen Recorder. To work around this bug, GPU Screen Recorder can overclock your GPU memory transfer rate to it's normal optimal level.\
To enable overclocking for optimal performance use the `-oc` option when running GPU Screen Recorder. You also need to have "Coolbits" NVIDIA X setting set to "12" to enable overclocking. You can automatically add this option if you run `sudo nvidia-xconfig --cool-bits=12` and then reboot your computer.\
Note that this only works when Xorg server is running as root, and using this option will only give you a performance boost if the game you are recording is bottlenecked by your GPU.\
Note! use at your own risk!
# VRR/G-SYNC
This should work fine on AMD/Intel X11 or Wayland. On Nvidia X11 G-SYNC only works with the -w screen-direct-force option, but because of bugs in the Nvidia driver this option is not always recommended.
For example it can cause your computer to freeze when recording certain games.

# Installation
If you are running an Arch Linux based distro then you can find gpu screen recorder on aur under the name gpu-screen-recorder (`yay -S gpu-screen-recorder`).\
If you are running another distro then you can run `sudo ./install.sh`, but you need to manually install the dependencies, as described below.\
You can also install gpu screen recorder ([the gtk gui version](https://git.dec05eba.com/gpu-screen-recorder-gtk/)) from [flathub](https://flathub.org/apps/details/com.dec05eba.gpu_screen_recorder), which is the easiest method
to install GPU Screen Recorder on non-arch based distros.\
If you install GPU Screen Recorder flatpak, which is the gtk gui version then you can still run GPU Screen Recorder command line by using the flatpak command option, for example `flatpak run --command=gpu-screen-recorder com.dec05eba.gpu_screen_recorder -w screen -f 60 -o video.mp4`. Note that if you want to record your monitor on AMD/Intel then you need to install the flatpak system-wide (like so: `flatpak install flathub --system com.dec05eba.gpu_screen_recorder`).

## Unofficial install methods
The only official ways to install GPU Screen Recorder is either from source, AUR or flathub. Other sources may be out of date and missing features or may not work correctly.\
If you install GPU Screen Recorder from somewhere else and have an issue then try installing it from one of the official sources before reporting it as an issue.\
If you still prefer to install GPU Screen Recorder with a package manager instead of from source or as a flatpak then you may be able to find a package for your distro.\
Here are some known unofficial packages:
* Debian/Ubuntu: [Pacstall](https://pacstall.dev/packages/gpu-screen-recorder)
* Nix: [NixOS wiki](https://wiki.nixos.org/wiki/Gpu-screen-recorder)
* openSUSE: [openSUSE software repository](https://software.opensuse.org/package/gpu-screen-recorder)
* Fedora: [Copr](https://copr.fedorainfracloud.org/coprs/brycensranch/gpu-screen-recorder-git/)

# Dependencies
GPU Screen Recorder uses meson build system so you need to install `meson` to build GPU Screen Recorder.

## Build dependencies
These are the dependencies needed to build GPU Screen Recorder:

* libglvnd (which provides libgl, libglx and libegl)
* vulkan-headers
* ffmpeg (libavcodec, libavformat, libavutil, libswresample, libavfilter)
* x11 (libx11, libxcomposite, libxrandr, libxfixes, libxdamage)
* libpulse
* libva (and libva-drm)
* libdrm
* libcap
* wayland-client
* wayland-egl

## Runtime dependencies
There are also additional dependencies needed at runtime depending on your GPU vendor:

### AMD
* mesa
* vaapi (libva-mesa-driver)

### Intel
* mesa
* vaapi (intel-media-driver/libva-intel-driver/linux-firmware, depending on which intel iGPU you have)

### NVIDIA
* cuda runtime (libcuda.so.1) (libnvidia-compute)
* nvenc (libnvidia-encode)
* nvfbc (libnvidia-fbc1, when recording the screen on x11)
* xnvctrl (libxnvctrl0, when using the `-oc` option)

## Optional dependencies
When compiling GPU Screen Recorder with portal support (`-Dportal=true`, which is enabled by default) these dependencies are also needed:
* libdbus
* libpipewire (and libspa which is usually part of libpipewire)

# How to use
Run `gpu-screen-recorder --help` to see all options and also examples.\
There is also a gui for the gpu screen recorder called [GPU Screen Recorder GTK](https://git.dec05eba.com/gpu-screen-recorder-gtk/).\
There is also a new alternative UI for GPU Screen Recorder in the style of ShadowPlay called [GPU Screen Recorder UI](https://git.dec05eba.com/gpu-screen-recorder-ui/).
## Recording
Here is an example of how to record your monitor and the default audio output: `gpu-screen-recorder -w screen -f 60 -a default_output -o ~/Videos/test_video.mp4`.
Yyou can stop and save the recording with `Ctrl+C` or by running `killall -SIGINT gpu-screen-recorder`.
You can see a list of capture options to record if you run `gpu-screen-recorder --list-capture-options`. This will list possible capture options and monitor names, for example:\
```
  window
  DP-1|1920x1080
```
in this case you could record a window or a monitor with the name `DP-1`.
## Streaming
Streaming works the same as recording, but the `-o` argument should be path to the live streaming service you want to use (including your live streaming key). Take a look at `scripts/twitch-stream.sh` to see an example of how to stream to twitch.
## Replay mode
Run `gpu-screen-recorder` with the `-c mp4` and `-r` option, for example: `gpu-screen-recorder -w screen -f 60 -r 30 -c mp4 -o ~/Videos`. Note that in this case, `-o` should point to a directory.\
If `-df yes` is set, replays are save in folders based on the date.
The file path to the saved replay is output to stdout. All other output from GPU Screen Recorder are output to stderr.
You can also use the `-sc` option to specify a script that should be run (asynchronously) when the video has been saved and the script will have access to the location of the saved file as its first argument.
This can be used for example to show a notification when a replay has been saved, to rename the video with a title that matches the game played (see `scripts/record-save-application-name.sh` as an example on how to do this on X11) or to re-encode the video.\
The replay buffer is stored in ram (as encoded video), so don't use a too large replay time and/or video quality unless you have enough ram to store it.
## Controlling GPU Screen Recorder remotely
To save a video in replay mode, you need to send signal SIGUSR1 to gpu screen recorder. You can do this by running `killall -SIGUSR1 gpu-screen-recorder`.\
To stop recording send SIGINT to gpu screen recorder. You can do this by running `killall -SIGINT gpu-screen-recorder` or pressing `Ctrl-C` in the terminal that runs gpu screen recorder. When recording a regular non-replay video this will also save the video.\
To pause/unpause recording send SIGUSR2 to gpu screen recorder. You can do this by running `killall -SIGUSR2 gpu-screen-recorder`. This is only applicable and useful when recording (not streaming nor replay).\
## Simple way to run replay without gui
Run the script `scripts/start-replay.sh` to start replay and then `scripts/save-replay.sh` to save a replay and `scripts/stop-replay.sh` to stop the replay. The videos are saved to `$HOME/Videos`.
You can use these scripts to start replay at system startup if you add `scripts/start-replay.sh` to startup (this can be done differently depending on your desktop environment / window manager) and then go into
hotkey settings on your system and choose a hotkey to run the script `scripts/save-replay.sh`. Modify `scripts/start-replay.sh` if you want to use other replay options.
## Run replay on system startup
If you installed GPU Screen Recorder from AUR or from source and you are running a distro that uses systemd then you will have a systemd service installed that can be started with `systemctl enable --now --user gpu-screen-recorder`. This systemd service runs GPU Screen Recorder on system startup.\
It's configured with `$HOME/.config/gpu-screen-recorder.env` (create it if it doesn't exist). You can look at [extra/gpu-screen-recorder.env](https://git.dec05eba.com/gpu-screen-recorder/plain/extra/gpu-screen-recorder.env) to see an example.
You can see which variables that you can use in the `gpu-screen-recorder.env` file by looking at the `extra/gpu-screen-recorder.service` file. Note that all of the variables are optional, you only have to set the ones that are you interested in.
You can use the `scripts/save-replay.sh` script to save a replay and by default the systemd service saves videos in `$HOME/Videos`.
# Issues
## NVIDIA
Nvidia drivers have an issue where CUDA breaks if CUDA is running when suspend/hibernation happens, and it remains broken until you reload the nvidia driver. `extra/gsr-nvidia.conf` will be installed by default when you install GPU Screen Recorder and that should fix this issue. If this doesn't fix the issue for you then your distro may use a different path for modprobe files. In that case you have to install that `extra/gsr-nvidia.conf` yourself into that location.
You have to reboot your computer after installing GPU Screen Recorder for the first time for the fix to have any effect.
# Examples
Look at the [scripts](https://git.dec05eba.com/gpu-screen-recorder/tree/scripts) directory for script examples. For example if you want to automatically save a recording/replay into a folder with the same name as the game you are recording.

# Reporting bugs
Issues are reported on this Github page: [https://github.com/dec05eba/gpu-screen-recorder-issues](https://github.com/dec05eba/gpu-screen-recorder-issues).
# Contributing patches
See [https://git.dec05eba.com/?p=about](https://git.dec05eba.com/?p=about) for contribution steps.
# Donations
See [https://git.dec05eba.com/?p=about](https://git.dec05eba.com/?p=about) for donation options.

# Demo
[![Click here to watch a demo video on youtube](https://img.youtube.com/vi/n5tm0g01n6A/0.jpg)](https://www.youtube.com/watch?v=n5tm0g01n6A)

# FAQ
## It tells me that my AMD/Intel GPU is not supported or that my GPU doesn't support h264/hevc, but that's not true!
Some linux distros (such as manjaro and fedora) disable hardware accelerated h264/hevc on AMD/Intel because of "patent license issues". If you are using an arch-based distro then you can install mesa-git instead of mesa and if you are using another distro then you may have to switch to a better distro. On fedora based distros you can follow this: [Hardware Accelerated Codec](https://rpmfusion.org/Howto/Multimedia).\
If you installed GPU Screen Recorder flatpak then you can try installing mesa-extra freedesktop runtime by running this command: `flatpak install --system org.freedesktop.Platform.GL.default//23.08-extra`
## I have an old nvidia GPU that supports nvenc but I get a cuda error when trying to record
Newer ffmpeg versions don't support older nvidia cards. Try installing GPU Screen Recorder flatpak from [flathub](https://flathub.org/apps/details/com.dec05eba.gpu_screen_recorder) instead. It comes with an older ffmpeg version which might work for your GPU.
## I get a black screen/glitches while live streaming
It seems like ffmpeg earlier than version 6.1 has some type of bug. Install ffmpeg version 6.1 or later and then reinstall GPU Screen Recorder to fix this issue. The flatpak version of GPU Screen Recorder comes with a newer version of ffmpeg so no extra steps are needed.
## I can't play the video in my browser directly or in discord
Browsers and discord don't support hevc video codec at the moment. Choose h264 video codec instead with the -k h264 option.
Note that websites such as youtube support hevc so there is no need to choose h264 video codec if you intend to upload the video to youtube or if you want to play the video locally or if you intend to
edit the video with a video editor. Hevc allows for better video quality (especially at lower file sizes) so hevc (or av1) is recommended for source videos.
## I get a black bar/distorted colors on the sides in the video
This is mostly an issue on AMD. For av1 it's a hardware issue, see: https://gitlab.freedesktop.org/mesa/mesa/-/issues/9185. For hevc it's a software issue in the AMD driver that hasn't been fixed yet. This issue happens at certain video resolutions. If you get this issue then a workaround is to record with h264 video codec instead (using the -k h264 option).
## The video doesn't display or has a green/yellow overlay
This can happen if your video player is missing the H264/HEVC video codecs. Either install the codecs or use mpv.
## I get stutter in the video
Try recording to an SSD and make sure it's not using NTFS file system. Also record in variable framerate format.
## The colors look washed out when recording a monitor with HDR enabled
You have to either record in hdr mode (-k `hevc_hdr` or -k `av1_hdr` option) to record a HDR video or record with desktop portal option (`-w portal`) to turn the HDR recording into SDR.
## GPU Screen Recorder records night light when recording in HDR mode
You can record with desktop portal option (`-w portal`) instead which ignores night light, if you are ok with recording without HDR.
## Kdenlive says that the video is not usable for editing because it has variable frame rate
To fix this you can either record the video in .mkv format or constant frame rate (-fm cfr).
## Colors look incorrect when recording HDR with hevc_hdr/av1_hdr
The latest version of KDE Plasma breaks HDR for recording applications. Wayland in general doesn't properly support recording HDR yet. Use desktop portal option (`-w portal`) for now to turn HDR recording into SDR.