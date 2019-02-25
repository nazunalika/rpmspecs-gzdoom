Name:           gzdoom
Version:        3.7.2
Release:        1%{?dist}
Summary:        A DOOM source port with graphic and modding extensions
License:        GPLv3
Group:          Games/Shooter
Url:            http://zdoom.org
Source0:        https://github.com/coelckers/gzdoom/archive/g%{version}.tar.gz

Provides:       zdoom = 2.8.1
#Provides:       qzdoom = 2.1.0
#Provides:       bundled(lzma-sdk) = 17.01
#Provides:       bundled(dumb) = 0.9.3
#Provides:       bundled(gdtoa)
#Provides:       bundled(re2c) = 0.16.0

Patch1:         gzdoom-waddir.patch
Patch2:         gzdoom-wadsrc-extra.patch
Patch3:         gzdoom-staticlibs.patch
Patch5:         gzdoom-lzma.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  SDL2-devel
BuildRequires:  git
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  game-music-emu-devel
BuildRequires:  openal-soft-devel
BuildRequires:  libmpg123-devel
BuildRequires:  libsndfile-devel
BuildRequires:  wildmidi-devel
BuildRequires:  gtk3-devel
BuildRequires:  timidity++
BuildRequires:  nasm
BuildRequires:  mesa-libGL-devel
BuildRequires:  tar
BuildRequires:  SDL-devel
BuildRequires:  glew-devel

Requires:       wildmidi
Requires:       openal-soft
Requires:       fluidsynth
Requires:       SDL2

%if 0%{?fedora}
Recommends:     freedoom
Recommends:     timidity++
%endif

%description
GZDoom is a port (a modification) of the original Doom source code, featuring:
  * an OpenGL renderer, HQnX rescaling, 3D floor and model support
  * Truecolor software rendering, extending the classic 8-bit palette
  * a three-point projection software renderer, extending the classic
    2-point projection
  * Heretic, Hexen and Strife game modes and support for a lot of
    additional IWADs.
  * Boom and Hexen map extension support, scriptability with ACS and
    ZScript, and various modding features regarding actors and scenery.
  * Demo record/playback of classic and Boom demos is not supported.

%prep
%setup -q -n %{name}-g%{version}
%patch -P 1 -P 2 -P 3 -p1

perl -i -pe 's{__DATE__}{""}g' src/posix/sdl/i_main.cpp
perl -i -pe 's{<unknown version>}{%version}g' \
        tools/updaterevision/updaterevision.c

%build
# We must not strip - %%debug_package will take care of it
# Deactivate -Wl,--as-needed
%cmake  -DNO_STRIP=1 \
        -DCMAKE_SHARED_LINKER_FLAGS="" \
        -DCMAKE_EXE_LINKER_FLAGS="" -DCMAKE_MODULE_LINKER_FLAGS="" \
        -DINSTALL_DOCS_PATH="%{_docdir}/%{name}" \
        -DINSTALL_PK3_PATH="%{_datadir}/doom"

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install/fast

%post
echo "INFO: %{name}: The global IWAD directory is %{_datadir}/doom."

%files
%defattr(-, root, root, -)
%doc docs/console.css docs/console.html docs/rh-log.txt docs/licenses/*
%{_bindir}/%{name}
%{_datadir}/doom/*
%{_docdir}/%{name}/*

%changelog
* Mon Feb 25 2019 Louis Abel <tucklesepk@gmail.com> - 3.7.2-1
- Rebased to 3.7.2
- Removed provides of qzdoom
- Automated webhook build from git

* Fri Oct 12 2018 Louis Abel <tucklesepk@gmail.com> - 3.6.0-1
- Rebuild spec according to Fedora guidelines
- Removed timidity dependency as timidity is built-in to gzdoom
- Rebased to 3.6.0

