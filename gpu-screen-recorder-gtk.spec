Name:           gpu-screen-recorder-gtk
Version:        4.1.7
Release:        0%{?dist}
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.
License:        GPL-3.0-or-later
Source:         %{name}-%{version}.tar.gz
URL:            https://git.dec05eba.com/%{name}

BuildRequires: bash
BuildRequires: git
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig(x11)
BuildRequires: make
BuildRequires: libX11-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: wayland-devel
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(libdrm)
BuildRequires: libXcomposite-devel
BuildRequires: libXrandr-devel
BuildRequires: libXfixes-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libdrm
BuildRequires: libva-devel
BuildRequires: libcap-devel
BuildRequires: libdrm-devel
BuildRequires: wayland-devel
BuildRequires: libayatana-appindicator-gtk3-devel

# Additional dependencies found via pkg-config
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: libX11
BuildRequires: libX11-common
BuildRequires: mesa-libGL-devel
BuildRequires: meson
BuildRequires: ninja-build
Requires: gpu-screen-recorder

%description
%{name} is a shadowplay-like screen recorder for Linux. It is the fastest screen recorder for Linux.

%prep
%setup -q -n %{name}-%{version}
rm -rf build && mkdir build

%build
meson setup --prefix %{_prefix} build
meson compile -C build

# Installation requires root permissions
%install
DESTDIR=%{buildroot} meson install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/gpu-screen-recorder-gtk
%{_datadir}/applications/com.dec05eba.gpu_screen_recorder.desktop
%{_datadir}/icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png
%{_datadir}/icons/hicolor/128x128/status/com.dec05eba.gpu_screen_recorder.tray-idle.png
%{_datadir}/icons/hicolor/128x128/status/com.dec05eba.gpu_screen_recorder.tray-paused.png
%{_datadir}/icons/hicolor/128x128/status/com.dec05eba.gpu_screen_recorder.tray-recording.png
%{_datadir}/icons/hicolor/32x32/apps/com.dec05eba.gpu_screen_recorder.png
%{_datadir}/icons/hicolor/32x32/status/com.dec05eba.gpu_screen_recorder.tray-idle.png
%{_datadir}/icons/hicolor/32x32/status/com.dec05eba.gpu_screen_recorder.tray-paused.png
%{_datadir}/icons/hicolor/32x32/status/com.dec05eba.gpu_screen_recorder.tray-recording.png
%{_datadir}/icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png
%{_datadir}/icons/hicolor/64x64/status/com.dec05eba.gpu_screen_recorder.tray-idle.png
%{_datadir}/icons/hicolor/64x64/status/com.dec05eba.gpu_screen_recorder.tray-paused.png
%{_datadir}/icons/hicolor/64x64/status/com.dec05eba.gpu_screen_recorder.tray-recording.png
%{_datadir}/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml

%changelog
* Thu Sep 05 2024 Trung Lê <8@tle.id.au> - 1.4.7-0
- update to 1.4.7
