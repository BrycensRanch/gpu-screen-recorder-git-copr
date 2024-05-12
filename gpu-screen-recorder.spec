%global snapshot r584.357df7c
%global debug_package %{nil}

Name:           gpu-screen-recorder
Version:        %{snapshot}
Release:        %autorelease
Summary:        A shadowplay-like screen recorder for Linux. The fastest screen recorder for Linux.

License:        GPL-3.0-or-later

URL:            https://git.dec05eba.com/%{name}

Source:         https://dec05eba.com/snapshot/%{name}.git.%{snapshot}.tar.gz

BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  libdrm-devel
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libX11)
BuildRequires:  pkgconfig(libX11-common)
BuildRequires:  pkgconfig(libXcomposite)
BuildRequires:  pkgconfig(libXrandr)
BuildRequires:  pkgconfig(libXfixes)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ffmpeg)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(x11)

#BuildRequires: nvidia-utils            
#BuildRequires: libxnvctrl             
BuildRequires: mesa-libGL-devel         
BuildRequires: libva-intel-driver       
BuildRequires: intel-media-driver    


%description
%{name} is a shadowplay-like screen recorder for Linux. It is the fastest screen recorder for Linux.
 

%prep
%autosetup -c

%build
./build.sh

# Installation requires root permissions
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
install -Dm755 %{name} %{buildroot}%{_bindir}
install -Dm755 gsr-kms-server %{buildroot}%{_bindir}
install -Dm644 "extra/%{name}.service" "%{buildroot}/usr/lib/systemd/user/%{name}.service"



%files
%license LICENSE
%doc README.md
%{_bindir}/gpu-screen-recorder
%{_bindir}/gsr-kms-server
/usr/lib/systemd/user/%{name}.service



%changelog
%autochangelog
