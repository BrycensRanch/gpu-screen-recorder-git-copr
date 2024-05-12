%global snapshot r269.67a2c39
%global debug_package %{nil}

Name:           gpu-screen-recorder-gtk
Version:        %{snapshot}
Release:        %autorelease
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.
License:        GPL-3.0-or-later
Source:         https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz
BuildArchitectures: x86_64 aarch64
URL:            https://git.dec05eba.com/%{name}

%description
%{name} is a shadowplay-like screen recorder for Linux. It is the fastest screen recorder for Linux.

BuildRequires:  bash
BuildRequires:  git
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
BuildRequires: libXcomposite-devel
BuildRequires: libXrandr-devel
BuildRequires: libXfixes-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libdrm
BuildRequires: libva-devel
BuildRequires: libcap-devel
BuildRequires: libdrm-devel
BuildRequires: wayland-devel
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

%prep
%autosetup -c


%build
./build.sh

# Installation requires root permissions
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
install -Dm755 %{name} %{buildroot}%{_bindir}
install -Dm644 "%{name}.desktop" "%{buildroot}/usr/share/applications/com.dec05eba.gpu_screen_recorder.desktop"
install -Dm644 com.dec05eba.gpu_screen_recorder.appdata.xml "%{buildroot}/usr/share/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml"
install -Dm644 icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png "%{buildroot}/usr/share/icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png"
install -Dm644 icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png "%{buildroot}/usr/share/icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png"


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
/usr/share/applications/com.dec05eba.gpu_screen_recorder.desktop
/usr/share/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
/usr/share/icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png
/usr/share/icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png


%changelog
%autochangelog
