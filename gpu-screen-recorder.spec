Name:           gpu-screen-recorder
Version:        4.1.7
Release:        0%{?dist}
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.

License:        GPL-3.0-or-later

URL:            https://git.dec05eba.com/%{name}

Source:         %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  libdrm-devel
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  libX11-devel
BuildRequires:  libX11-common
BuildRequires:  libXcomposite-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXfixes-devel
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(x11)
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  ninja-build


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
%{_bindir}/gpu-screen-recorder
%{_bindir}/gsr-kms-server
%{_prefix}/lib/modprobe.d/gsr-nvidia.conf
%{_prefix}/lib/systemd/user/gpu-screen-recorder.service

%changelog
* Thu Sep 05 2024 Trung Lê <8@tle.id.au> - 1.4.7-0
- update to 1.4.7
