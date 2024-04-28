# Global settings
%global major_version 4
%global minor_version 12
%global micro_version 2
#define debug_package %{nil}

Name:           gzdoom
Version:        %{major_version}.%{minor_version}.%{micro_version}
Release:        3%{?dist}
Summary:        An OpenGL DOOM source port with graphic and modding extensions
License:        GPLv3
Url:            http://zdoom.org
Source0:        https://github.com/coelckers/gzdoom/archive/g%{version}.tar.gz
Source1:        gzdoom.desktop

Provides:       zdoom = 2.8.1
Provides:       qzdoom = 1.3.0
Provides:       bundled(re2c) = 0.16.0
Provides:       bundled(gdtoa)
#Provides:       bundled(lzma-sdk) = 17.01
#Provides:       bundled(dumb) = 0.9.3

Patch1:         %{name}-waddir.patch
Patch2:         %{name}-asmjit.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  tar
BuildRequires:  git
BuildRequires:  nasm
BuildRequires:  glew-devel
BuildRequires:  pkgconfig(libwebp)

# Todo: Patch
#BuildRequires:  glslang-devel

# pkgconfig
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(vpx)

BuildRequires:  timidity++
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(wildmidi)
Requires:       wildmidi

Requires:       openal-soft
Requires:       fluidsynth
Requires:       SDL2

# ZMusic Requirement
BuildRequires:  zmusic-devel
Requires:       zmusic

Recommends:     freedoom

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
%patch -P 1 -P 2 -p1

perl -i -pe 's{__DATE__}{""}g' \
        src/common/platform/posix/sdl/i_main.cpp
perl -i -pe 's{<unknown version>}{%version}g' \
        tools/updaterevision/UpdateRevision.cmake

%build
%define _lto_cflags %nil
%cmake  -B builddir \
        -DNO_STRIP=1 \
        -DCMAKE_SHARED_LINKER_FLAGS="" \
        -DCMAKE_EXE_LINKER_FLAGS="" \
        -DCMAKE_MODULE_LINKER_FLAGS="" \
        -DBUILD_SHARED_LIBS="OFF" \
        -DINSTALL_DOCS_PATH="%{_docdir}/%{name}" \
        -DINSTALL_PK3_PATH="%{_datadir}/doom" \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo

#make_build -C builddir
make %{?_smp_mflags} -C builddir

%install
rm -rf $RPM_BUILD_ROOT

# Install gzdoom
%make_install -C builddir

%{__mkdir} -p ${RPM_BUILD_ROOT}%{_datadir}/applications
%{__install} -m 0644 %{SOURCE1} \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/gzdoom.desktop

# Don't know why but the XPM isn't put anywhere
%{__mkdir} -p ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/256x256/apps
cp %{_builddir}/%{name}-g%{version}/src/posix/zdoom.xpm \
  ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/256x256/apps/gzdoom.xpm

# Fallback soundfont - Symlinking instead of copying
# as a test for now. It's not clear if the binary will look here
# or look in /usr/share/games/doom yet.
pushd ${RPM_BUILD_ROOT}%{_datadir}/doom
    %{__ln_s} %{_datadir}/games/doom/soundfounts soundfonts
    %{__ln_s} %{_datadir}/games/doom/fm_banks fm_banks
popd

%post
echo "INFO: %{name}: The global IWAD directory is %{_datadir}/doom."

%files
%defattr(-, root, root, -)
%doc docs/console.css docs/console.html docs/rh-log.txt docs/licenses/* docs/skins.txt
%{_bindir}/%{name}
%{_datadir}/doom/*
%{_docdir}/%{name}/*
%{_datadir}/applications/gzdoom.desktop
%{_datadir}/icons/hicolor/256x256/apps/gzdoom.xpm
%{_datadir}/games/doom/*

%changelog
* Sun Apr 28 2024 Louis Abel <tucklesepk@gmail.com> - 4.12.2-3
- Rebuild for gcc 14

* Sun Apr 21 2024 Louis Abel <tucklesepk@gmail.com> - 4.12.1-3
- Attempt to fix compiler errors

* Sun Apr 21 2024 Louis Abel <tucklesepk@gmail.com> - 4.12.1-1
- Update to 4.12.1

* Sun Apr 21 2024 Louis Abel <tucklesepk@gmail.com> - 4.12.0-1
- Update to 4.12.0

* Thu Oct 26 2023 Louis Abel <tucklesepk@gmail.com> - 4.11.3-1
- Update to 4.11.3

* Wed Oct 25 2023 Louis Abel <tucklesepk@gmail.com> - 4.11.2-1
- Update to 4.11.2 

* Wed Oct 11 2023 Louis Abel <tucklesepk@gmail.com> - 4.11.1-1
- Update to 4.11.1

* Mon Oct 09 2023 Louis Abel <tucklesepk@gmail.com> - 4.11.0-3
- Actually fix non-x86 builds

* Mon Sep 25 2023 Louis Abel <tucklesepk@gmail.com> - 4.11.0-2
- Fix non-x86 builds

* Mon Sep 25 2023 Louis Abel <tucklesepk@gmail.com> - 4.11.0-1
- Update to 4.11.0

* Thu Sep 21 2023 Louis Abel <tucklesepk@gmail.com> - 4.10.0-6
- Rebuild version 4.9.0

* Sun Dec 04 2022 Louis Abel <tucklesepk@gmail.com> - 4.10.0-5
- Update to 4.9.0

* Sat Nov 05 2022 Louis Abel <tucklesepk@gmail.com> - 4.9.0-1
- Update to 4.9.0

* Mon Jul 04 2022 Louis Abel <tucklesepk@gmail.com> - 4.8.2-4
- Turn on 32 bit builds for armhfp

* Mon Jul 04 2022 Louis Abel <tucklesepk@gmail.com> - 4.8.2-3
- Update to 4.8.2

* Sun Jun 26 2022 Louis Abel <tucklesepk@gmail.com> - 4.8.1-3
- Update to 4.8.1

* Mon Jun 06 2022 Louis Abel <tucklesepk@gmail.com> - 4.8.0-3
- Rebuild against zmusic 1.1.9
- Revert a commit from May 1st

* Mon Jun 06 2022 Louis Abel <tucklesepk@gmail.com> - 4.8.0-1
- Update to 4.8.0

* Wed Oct 20 2021 Louis Abel <tucklesepk@gmail.com> - 4.7.1-1
- Update to 4.7.1

* Wed Sep 22 2021 Louis Abel <tucklesepk@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Sun Jul 25 2021 Louis Abel <tucklesepk@gmail.com> - 4.6.1-2
- Updates to 4.6.1

* Tue May 25 2021 Louis Abel <tucklesepk@gmail.com> - 4.6.0-2
- Rebuild against zmusic 1.1.8

* Sat May 22 2021 Louis Abel <tucklesepk@gmail.com> - 4.6.0-1
- Rebase to 4.6.0

* Fri Nov 06 2020 Louis Abel <tucklesepk@gmail.com> - 4.5.0-2
- Turn on debuginfo packages
- Adopt relinfo from flatpak
- Fixing perl replacements

* Wed Nov 04 2020 Louis Abel <tucklesepk@gmail.com> - 4.5.0-1
- Rebase to 4.5.0
- Remove spirv static patch
- Cleanup unneeded macros
- Added temporary zipdir patch to fix make build errors
- Created symlinks for banks and soundfonts

* Mon Oct 26 2020 Louis Abel <tucklesepk@gmail.com> - 4.4.2-4
- Build for Fedora 33
- Adapt to Fedora macro changes for out-of-source builds

* Sun Sep 27 2020 Louis Abel <tucklesepk@gmail.com> - 4.4.2-3
- Rebuild with zmusic 1.1.3

* Tue Jun 16 2020 Louis Abel <tucklesepk@gmail.com> - 4.4.2-2
- Rebase to 4.4.2
- Add asmjit and spirv patches

* Mon Jun 15 2020 Louis Abel <tucklesepk@gmail.com> - 4.4.1-1
- Update to 4.4.1
- Add ZMusic Requirement
- Fix waddir patch
- Remove debug info packages
- Add vulkan requirements
- Remove openSUSE support as default repos contain it

* Mon Jan 20 2020 Louis Abel <tucklesepk@gmail.com> - 4.3.3-1
- Update to 4.3.3

* Sun Jan 12 2020 Louis Abel <tucklesepk@gmail.com> - 4.3.2-1
- Update to 4.3.2

* Sun Jan 05 2020 Louis Abel <tucklesepk@gmail.com> - 4.3.1-1
- Update to 4.3.1

* Sun Jan 05 2020 Louis Abel <tucklesepk@gmail.com> - 4.3.0-1
- Update to 4.3.0

* Sun Oct 20 2019 Louis Abel <tucklesepk@gmail.com> - 4.2.3-1
- Update to 4.2.3

* Mon Sep 09 2019 Louis Abel <tucklesepk@gmail.com> - 4.2.1-1
- Update to 4.2.1
- Remove fl2 patch as it is now in code

* Mon Aug 12 2019 Louis Abel <tucklesepk@gmail.com> - 4.2.0-1
- Update to 4.2.0

* Mon Jun 10 2019 Louis Abel <tucklesepk@gmail.com> - 4.1.3-1
- Update to 4.1.3
- Removed static patches

* Fri May 31 2019 Louis Abel <tucklesepk@gmail.com> - 4.1.2-6
- Added AARCH64 to builds
- Added i386 back to builds

* Wed May 22 2019 Louis Abel <tucklesepk@gmail.com> - 4.1.2-5
- Update to 4.1.2
- Modified patches

* Wed May 15 2019 Louis Abel <tucklesepk@gmail.com> - 4.1.1-5
- Update to 4.1.1

* Sun Apr 28 2019 Louis Abel <tucklesepk@gmail.com> - 4.0.0-5
- Added more static libraries in patches

* Tue Apr 16 2019 Louis Abel <tucklesepk@gmail.com> - 4.0.0-4
- Rebase to 4.0.0
- Fixed, removed, redid patches as needed
- 32 bit builds are no longer supported

* Tue Apr 09 2019 Louis Abel <tucklesepk@gmail.com> - 3.7.2-4
- Adding Fedora 30 to build
- Added OpenSUSE Tumbleweed as a distribution
- Some BuildRequires converted to pkgconfig based on fedora spec

* Mon Feb 25 2019 Louis Abel <tucklesepk@gmail.com> - 3.7.2-3
- Added application file for games menu
- Updated description
- Removed timidity++ as a weak dependency
- Removed Group section as it is not required
- Added fallback soundfont from the sources

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
