Name:           gpu-screen-recorder-adwaita
Version:        2.0.1
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
BuildRequires:  (libappstream-glib or lib64appstream-glib8 or appstream-glib)
BuildRequires:  gettext

Requires:       gpu-screen-recorder

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
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.runlevel5.gpu_screen_recorder_adwaita.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.github.runlevel5.gpu_screen_recorder_adwaita.metainfo.xml
%meson_test

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/gpu-screen-recorder-adw
%{_datadir}/applications/io.github.runlevel5.gpu_screen_recorder_adwaita.desktop
%{_datadir}/metainfo/io.github.runlevel5.gpu_screen_recorder_adwaita.metainfo.xml
%{_datadir}/icons/hicolor/

%changelog
* Wed Oct 28 2026 Trung Lê <8@tle.id.au> - 2.0.1-1
- Update to 2.0.1

* Sun Feb 22 2026 Trung Lê <8@tle.id.au> - 1.0.1-1
- Initial release of gpu-screen-recorder-adwaita
