%global snapshot r502.74cc5de

# gsr's appdata was split into separate repository.
%global appdata r9.e7e9f5b

Name:           gpu-screen-recorder-gtk
Version:        5.7.8
Release:        2%{dist}
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.
License:        GPL-3.0-or-later
Source0:        https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz
Source1:        https://dec05eba.com/snapshot/gpu-screen-recorder-appdata.git.%{appdata}.tar.gz
URL:            https://git.dec05eba.com/%{name}/about
# WARNING. I had to bump this because I decided to use normal versions instead of git snapshot as a version.
# If you remove this, you will be FIRED.
Epoch:          2

BuildRequires:  gcc
BuildRequires:  (gcc-g++ or gcc-c++)
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  (pkgconfig(ayatana-appindicator3-0.1) or libayatana-appindicator-gtk3-devel or libayatana-appindicator3-dev)
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
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.dec05eba.gpu_screen_recorder.desktop
%{_datadir}/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
%{_datadir}/icons/hicolor/

%changelog
* Thu Sep 05 2024 Brycen G <brycengranville@outlook.com> - 4.3.3-3
- Update to 4.3.3
