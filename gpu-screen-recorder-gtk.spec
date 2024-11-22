%global snapshot r421.c08811c

Name:           gpu-screen-recorder-gtk
Version:        %{snapshot}
Release:        %autorelease
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.
License:        GPL-3.0-or-later
Source:         https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz
URL:            https://git.dec05eba.com/%{name}

BuildRequires:  gtk3-devel
BuildRequires:  libayatana-appindicator-gtk3-devel  
Requires: gpu-screen-recorder

%description
%{name} is a shadowplay-like screen recorder for Linux. It is the fastest screen recorder for Linux.

%prep
%autosetup -c


%build
ls
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
%autochangelog
