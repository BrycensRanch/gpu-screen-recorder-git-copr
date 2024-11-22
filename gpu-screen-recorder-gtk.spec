%global snapshot r421.c08811c
%global debug_package %{nil}

Name:           gpu-screen-recorder-gtk
Version:        %{snapshot}
Release:        %autorelease
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.
License:        GPL-3.0-or-later
Source:         https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz
URL:            https://git.dec05eba.com/%{name}

BuildRequires:  bash
BuildRequires:  git
BuildRequires:  gtk3-devel
BuildRequires:  libayatana-appindicator-gtk3-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  make
BuildRequires:  libX11-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  libXcomposite-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXfixes-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libdrm
BuildRequires:  libva-devel
BuildRequires:  libcap-devel
BuildRequires:  libdrm-devel
BuildRequires:  wayland-devel
# https://i.imgflip.com/1tpd.gif
#BuildRequires: nvidia-settings

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
#BuildRequires: nvidia-utils            
#BuildRequires: libxnvctrl             
BuildRequires: mesa-libGL-devel         
BuildRequires: libva-intel-driver       
BuildRequires: intel-media-driver     
Requires: gpu-screen-recorder

%description
%{name} is a shadowplay-like screen recorder for Linux. It is the fastest screen recorder for Linux.

%prep
%autosetup -c


%build
ls
%meson
%meson_build

# Installation requires root permissions
%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
/usr/share/applications/com.dec05eba.gpu_screen_recorder.desktop
/usr/share/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
/usr/share/icons/hicolor/

%changelog
%autochangelog
