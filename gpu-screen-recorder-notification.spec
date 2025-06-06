%global snapshot r78.1d19340

Name:           gpu-screen-recorder-notification
Version:        1.0.7
Release:        1%{dist}
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.
License:        GPL-3.0-or-later
Source:         https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz
URL:            https://git.dec05eba.com/%{name}/about
# WARNING. I had to bump this because I decided to use normal versions instead of git snapshot as a version.
# If you remove this, you will be FIRED.
Epoch:          2

BuildRequires:  gcc
BuildRequires:  (gcc-g++ or gcc-c++)
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
Requires:       (google-noto-sans-fonts or noto-sans)

%description
A fullscreen overlay UI for GPU Screen Recorder in the style of ShadowPlay.


%prep
%autosetup -c


%build
%meson
%meson_build

%install
%meson_install

# Say it with me. I will not violate Fedora packaging guidelines.
rm -rf %{_buildroot}%{_datadir}/gsr-notify/fonts

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/gsr*
%{_datadir}/gsr-notify

%changelog
* Fri Dec 13 2024 Brycen G <brycengranville@outlook.com> - r43.b03e4cd
- Initial package
