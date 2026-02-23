Name:           gpu-screen-recorder-adwaita
Version:        1.0.1
Release:        1%{?dist}
Summary:        GNOME frontend for GPU Screen Recorder
License:        GPL-3.0-or-later
URL:            https://github.com/runlevel5/gpu-screen-recorder-adwaita
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Epoch:          1

BuildRequires:  gcc
BuildRequires:  meson >= 0.56
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8
BuildRequires:  pkgconfig(x11)
BuildRequires:  (update-desktop-files or desktop-file-utils)
BuildRequires:  (libappstream-glib or lib64appstream-glib8)

Requires:       gpu-screen-recorder
Conflicts:      gpu-screen-recorder-gtk

%description
GNOME (libadwaita) frontend for GPU Screen Recorder.
Provides a modern Adwaita UI for screen recording, streaming, and
replay (ShadowPlay-like) functionality using GPU hardware acceleration.

%prep
%autosetup -n %{name}-%{version}

%build
%meson -Dx11=true -Dwayland=true
%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.dec05eba.gpu_screen_recorder.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.dec05eba.gpu_screen_recorder.metainfo.xml
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/gpu-screen-recorder-adw
%{_datadir}/applications/com.dec05eba.gpu_screen_recorder.desktop
%{_datadir}/metainfo/com.dec05eba.gpu_screen_recorder.metainfo.xml
%{_datadir}/icons/hicolor/

%changelog
* Sun Feb 22 2026 Trung Lê <8@tle.id.au> - 1.0.1-1
- Initial release of gpu-screen-recorder-adwaita