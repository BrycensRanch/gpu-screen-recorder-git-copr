%global snapshot r421.c08811c

Name:           gpu-screen-recorder-gtk
Version:        4.3.3
Release:        5%{dist}
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
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  (pkgconfig(ayatana-appindicator3-0.1) or libayatana-appindicator-gtk3-devel or libayatana-appindicator3)
BuildRequires:  desktop-file-utils
Requires:       gpu-screen-recorder

%description
Shadowplay like screen recorder for Linux. This package exposes the GTK3 UI.


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
%{_bindir}/%{name}
/usr/share/applications/com.dec05eba.gpu_screen_recorder.desktop
/usr/share/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
/usr/share/icons/hicolor/

%changelog
* Thu Sep 05 2024 Brycen G <brycengranville@outlook.com> - 4.3.3-3
- Update to 4.3.3