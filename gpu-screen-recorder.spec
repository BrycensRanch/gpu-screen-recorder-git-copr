%global snapshot r909.8644c72

Name:           gpu-screen-recorder
Version:        %{snapshot}
Release:        %autorelease
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.

License:        GPL-3.0-or-later

URL:            https://git.dec05eba.com/%{name}/about

Source:         https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz

BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  vulkan-headers
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  /usr/bin/ffmpeg
BuildRequires:  pkgconfig(x11)
BuildRequires:  meson
BuildRequires:  pipewire-devel
BuildRequires:  pipewire-libs
BuildRequires:  libglvnd


%description
Shadowplay like screen recorder for Linux. It is the fastest screen recorder for Linux.


%prep
%autosetup -c

%build
%meson
%meson_build


%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/gpu-screen-recorder
%{_bindir}/gsr-kms-server
/usr/lib/systemd/user/%{name}.service
/usr/lib/modprobe.d/gsr-nvidia.conf


%changelog
%autochangelog
