%global commit 2cd031db48272635b851d6c79a6f283e497293d1
%global version 3.0.0
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20240512

Name:           gpu-screen-recorder
Version:        %{version}^%{git_date}git%{shortcommit}
Release:        %autorelease
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.

License:        GPL-3.0-or-later
URL:            https://git.dec05eba.com/gpu-screen-recorder
Source0:        ./gpu-screen-recorder

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(x11)
BuildRequires:  make
BuildRequires:  ffmpeg-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXfixes-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  ffmpeg-libs
BuildRequires:  libva-devel
BuildRequires:  libcap-devel
BuildRequires:  libdrm-devel
BuildRequires:  wayland-egl-devel
BuildRequires:  wayland-devel
BuildRequires:  nvidia-settings
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: ffmpeg-devel
BuildRequires: libX11-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXrandr-devel
BuildRequires: libXfixes-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: ffmpeg-libs
BuildRequires: libva-devel
BuildRequires: libcap-devel
BuildRequires: libdrm-devel
BuildRequires: wayland-egl-devel
BuildRequires: wayland-devel
BuildRequires: nvidia-settings

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


%description
%{name} is a shadowplay-like screen recorder for Linux. It is the fastest screen recorder for Linux.

%prep
%autosetup -p1 -a2 -N -n %{name}-%{commit}

%build
./build.sh

# Installation requires root permissions
%install
./install.sh

%files
%license LICENSE
%doc README.md
%{_bindir}/gpu-screen-recorder
