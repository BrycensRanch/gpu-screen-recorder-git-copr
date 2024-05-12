![](https://dec05eba.com/images/gpu_screen_recorder_logo_small.png)

# GPU Screen Recorder

This screen recorder has minimal impact on system performance by recording your monitor using the GPU only,
similar to shadowplay on Windows. This is the fastest screen recording tool for Linux.

This screen recorder can be used for recording your desktop offline, for live streaming, and for NVIDIA shadowplay-like instant replay,
where only the last few minutes are saved.

Supported video codecs:
* H264 (default on Intel)
* HEVC (default on AMD and NVIDIA)
* AV1 (not currently supported on NVIDIA if you use GPU Screen Recorder Flatpak)

Supported audio codecs:
* Opus (default)
* AAC

## Notes

- This software works with x11 and Wayland, but only monitors can be recorded when using Wayland.
- This is an unofficial community-maintained version. The [GPU Screen Recorder binary](https://git.dec05eba.com/gpu-screen-recorder/) is bundled alongside the [GTK UI](https://git.dec05eba.com/gpu-screen-recorder-gtk/).
