%global snapshot r584.357df7c
%global debug_package %{nil}

Name:           gpu-screen-recorder
Version:        %{snapshot}
Release:        %autorelease
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.

License:        GPL-3.0-or-later

URL:            https://git.dec05eba.com/%{name}

Source:         https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz


BuildArchitectures: x86_64 aarch64

%description
%{name} is a shadowplay-like screen recorder for Linux. It is the fastest screen recorder for Linux.

BuildRequires:  bash
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
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
BuildRequires: libdrm
BuildRequires:  libdrm-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: ffmpeg-devel
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkconfig(libpulse)
BuildRequires: pkgconfig(ffmpeg)
]BuildRequires: pkgconfig(wayland-client)
# https://i.imgflip.com/1tpd.gif
#BuildRequires: nvidia-settings

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
#BuildRequires: nvidia-utils            
#BuildRequires: libxnvctrl             
BuildRequires: mesa-libGL-devel         
BuildRequires: libva-intel-driver       
BuildRequires: intel-media-driver     

%prep
%autosetup -c

%build
./build.sh

# Installation requires root permissions
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
install -Dm755 %{name} %{buildroot}%{_bindir}
install -Dm755 gsr-kms-server %{buildroot}%{_bindir}
install -Dm644 "extra/%{name}.service" "%{buildroot}/usr/lib/systemd/user/%{name}.service"



%files
%license LICENSE
%doc README.md
%{_bindir}/gpu-screen-recorder
%{_bindir}/gsr-kms-server
/usr/lib/systemd/user/%{name}.service



%changelog
%autochangelog
