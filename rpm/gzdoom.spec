Name:           gzdoom
Version:        3.7.2
Release:        3%{?dist}
Summary:        A DOOM source port with graphic and modding extensions
License:        GPLv3
Url:            http://zdoom.org
Source0:        https://github.com/coelckers/gzdoom/archive/g%{version}.tar.gz
Source1:        gzdoom.desktop

Provides:       zdoom = 2.8.1
Provides:       qzdoom = 1.3.0
#Provides:       bundled(lzma-sdk) = 17.01
#Provides:       bundled(dumb) = 0.9.3
#Provides:       bundled(gdtoa)
#Provides:       bundled(re2c) = 0.16.0

Patch1:         gzdoom-waddir.patch
Patch2:         gzdoom-wadsrc-extra.patch
Patch3:         gzdoom-staticlibs.patch
Patch5:         gzdoom-lzma.patch
Patch6:         gzdoom-asmjit.patch
Patch7:         gzdoom-fl2.patch

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
#Recommends:     timidity++
%endif

%description
ZDoom is a family of enhanced ports (modifications) of the Doom engine for
running on modern operating systems. It runs on Windows, Linux, and OS X, and
adds new features not found in the games as originally published by id Software.

ZDoom features the following that is not found in the original Doom:

  * Runs on all modern versions of Windows, Mac, and Linux distributions
  * Can play all Doom engine games, including Ultimate Doom, Doom II, Heretic,
    Hexen, Strife, and more
  * Supports all editing features of Hexen
  * Supports most of the Boom editing features
  * Supports new features such as colored lighting, 3D floors, and much more
  * All Doom limits are gone
  * Several softsynths for MUS and MIDI playback, including OPL softsynth for an
    authentitc "oldschool" flavor
  * High resolutions
  * Quake-style console and key bindings
  * Crosshairs
  * Free look
  * Jumping, crouching, swimming, and flying
  * Up to 8 player network games using UDP/IP, including team-based gameplay
  * Support for the Bloodbath announcer from the classic Monolith game Blood
  * Walk over/under monsters and other things

GZDoom provides an OpenGL renderer and HQnX rescaling.

%prep
%setup -q -n %{name}-g%{version}
%patch -P 1 -P 2 -P 3 -P 6 -P 7 -p1

perl -i -pe 's{__DATE__}{""}g' src/posix/sdl/i_main.cpp
perl -i -pe 's{<unknown version>}{%version}g' \
        tools/updaterevision/updaterevision.c

%build
%cmake  -DNO_STRIP=1 \
        -DCMAKE_SHARED_LINKER_FLAGS="" \
        -DCMAKE_EXE_LINKER_FLAGS="" \
        -DCMAKE_MODULE_LINKER_FLAGS="" \
        -DINSTALL_DOCS_PATH="%{_docdir}/%{name}" \
        -DINSTALL_PK3_PATH="%{_datadir}/doom"

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
%{__install} -m 0644 %{SOURCE1} \
  %{_datadir}/applications/gzdoom.desktop

# Don't know why but the XPM isn't put anywhere
cp %{_builddir}/%{name}-g%{version}/src/posix/zdoom.xpm \
  %{_datadir}/icons/hicolor/256x256/apps/gzdoom.xpm

%post
echo "INFO: %{name}: The global IWAD directory is %{_datadir}/doom."

%files
%defattr(-, root, root, -)
%doc docs/console.css docs/console.html docs/rh-log.txt docs/licenses/*
%{_bindir}/%{name}
%{_datadir}/doom/*
%{_docdir}/%{name}/*
%{_datadir}/applications/gzdoom.desktop
%{_datadir}/icons/gzdoom.desktop
%{_datadir}/icons/hicolor/256x256/apps/gzdoom.xpm

%changelog
* Mon Feb 25 2019 Louis Abel <tucklesepk@gmail.com> - 3.7.2-3
- Added application file for games menu
- Updated description
- Removed timidity++ as a weak dependency
- Removed Group section as it is not required

* Mon Feb 25 2019 Louis Abel <tucklesepk@gmail.com> - 3.7.2-2
- Added back qzdoom provides
- Added patch to allow build to work with fluidsynth 2
  for when Fedora decides to rebase

* Mon Feb 25 2019 Tommy Nguyen <remyabel@gmail.com> - 3.7.2-2
- Added patch for libasmjit.so

* Mon Feb 25 2019 Louis Abel <tucklesepk@gmail.com> - 3.7.2-1
- Rebased to 3.7.2
- Removed provides of qzdoom
- Automated webhook build from git

* Fri Oct 12 2018 Louis Abel <tucklesepk@gmail.com> - 3.6.0-1
- Rebuild spec according to Fedora guidelines
- Removed timidity dependency as timidity is built-in to gzdoom
- Rebased to 3.6.0
