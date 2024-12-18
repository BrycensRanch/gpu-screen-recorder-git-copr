%global snapshot r43.b03e4cd

Name:           gpu-screen-recorder-notification
Version:        %{snapshot}
Release:        2%{dist}
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.
License:        GPL-3.0-or-later
Source:         https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz
URL:            https://git.dec05eba.com/%{name}/about

BuildRequires:  gcc
BuildRequires:  (gcc-g++ or gcc-c++)
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libglvnd)
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