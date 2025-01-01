%global snapshot r188.f526c17

Name:           gpu-screen-recorder-ui
Version:        1.0.3
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
BuildRequires:  cmake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  desktop-file-utils
Requires:       gpu-screen-recorder
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
rm -rf %{_buildroot}%{_datadir}/gsr-ui/fonts

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/gsr*
%{_datadir}/gsr-ui
%{_exec_prefix}/lib/systemd/user/%{name}.service

%changelog
* Fri Dec 13 2024 Brycen G <brycengranville@outlook.com> - r142.4c83972
- Initial package