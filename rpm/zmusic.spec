# Global settings
%global major_version 1
%global minor_version 1
%global micro_version 0
%global archive_name ZMusic

Name:           zmusic
Version:        %{major_version}.%{minor_version}.%{micro_version}
Release:        1%{?dist}
Summary:        ZMusic libraries and headers for GZDoom functionality
License:        GPLv3
Url:            http://zdoom.org
Source0:        https://github.com/coelckers/ZMusic/archive/%{version}.tar.gz

Provides:       zmusic = 1.1.0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  tar
BuildRequires:  git
BuildRequires:  nasm
BuildRequires:  glew-devel

# pkgconfig
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libmpg123)

BuildRequires:  timidity++
BuildRequires:  wildmidi-devel

%description
ZDoom is a family of enhanced ports (modifications) of the Doom engine for
running on modern operating systems. It runs on Windows, Linux, and OS X, and
adds new features not found in the games as originally published by id Software.

This package provides the necessary zmusic libraries necessary for gzdoom to
function.

%package        devel
Summary:        ZMusic development headers
Requires:       zmusic = %{version}-%{release}

%description    devel
This package contains the development headers required for building against
zmusic, typically for gzdoom installations.

%prep
%setup -q -n %{archive_name}-%{version}

%build
# Methodology used from zdoom forums
mkdir build
cd build
%cmake  -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_INSTALL_LIBDIR=%{_lib} ..

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%make_install
cd %{buildroot}/%{_prefix}
mv lib %{_lib}

%files
%defattr(-, root, root, -)
%doc licenses/*
%{_libdir}/*

%files devel
%defattr(-, root, root, -)
%{_includedir}/*

%changelog
* Sun Jun 14 2020 Louis Abel <tucklesepk@gmail.com> - 1.1.0-1
- Initial zmusic build

