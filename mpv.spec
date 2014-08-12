Summary:	Movie player based on MPlayer and mplayer2
Name:		mpv
Version:	0.5.0
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	http://github.com/mpv-player/mpv/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	85e4895dfdce888fb436e7c217958b8b
Source1:	%{name}.conf
Patch0:		%{name}-zshcompdir.patch
Patch1:		%{name}-lua.patch
Patch2:		%{name}-wafsyms.patch
URL:		http://mpv.io/
BuildRequires:	Mesa-libwayland-egl-devel >= 9.0.0
BuildRequires:	OpenAL-devel >= 1.13
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	enca-devel
BuildRequires:	ffmpeg-devel >= 2.1.4
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
BuildRequires:	lcms2-devel >= 2.6
BuildRequires:	libass-devel
%ifarch	i386 i486
BuildRequires:	libatomic-devel
%endif
BuildRequires:	libbluray-devel >= 0.2.1
BuildRequires:	libbs2b-devel
BuildRequires:	libcaca-devel >= 0.99
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libdvdnav-devel >= 4.2.0
BuildRequires:	libdvdread-devel >= 4.1.0
BuildRequires:	libguess-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmpg123-devel >= 1.14.0
BuildRequires:	libquvi-devel < 0.9.0
BuildRequires:	libsmbclient-devel
BuildRequires:	libv4l-devel
BuildRequires:	libva-devel >= 1.2.0
BuildRequires:	libva-glx-devel >= 1.2.0
BuildRequires:	libvdpau-devel >= 0.2
BuildRequires:	lirc-devel
BuildRequires:	lua51-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel >= 19
BuildRequires:	pulseaudio-devel >= 0.9
BuildRequires:	rpmbuild(macros) >= 1.336
# version dep to handle packaging issue in PLD
BuildRequires:	waf >= 1.7.14
BuildRequires:	wayland-devel >= 1.3.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.3.0
BuildRequires:	xorg-proto-xproto-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		zshdir %{_datadir}/zsh/site-functions

%description
Movie player based on MPlayer and mplayer2.

%package client-libs
Summary:        Client library for controlling mpv
Group:          Development/Libraries

%description client-libs
Client library for controlling mpv.

%package client-devel
Summary:        Development files for mpv client library
Group:          Development/Libraries
Requires:       %{name}-client-libs = %{version}-%{release}

%description client-devel
Development files for mpv client library.

%package -n zsh-completion-mpv
Summary:        zsh-completion for mpv
Group:          Applications/Shells
Requires:       %{name} = %{version}-%{release}

%description -n zsh-completion-mpv
zsh-completion for mpv.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%waf configure \
		--prefix=%{_prefix} \
		--bindir=%{_bindir} \
		--confdir=%{_sysconfdir}/mpv \
		--libdir=%{_libdir} \
		--datadir=%{_datadir} \
		--mandir=%{_mandir} \
		--disable-debug-build \
		--enable-alsa \
		--enable-audio-input \
		--enable-caca \
		--enable-cdda \
		--enable-dvb \
		--enable-dvbin \
		--enable-dvdnav \
		--enable-dvdread \
		--enable-enca \
		--enable-encoding \
		--enable-gl-wayland \
		--enable-gl-x11 \
		--enable-iconv \
		--enable-jack \
		--enable-joystick \
		--enable-jpeg \
		--enable-ladspa \
		--enable-lcms2 \
		--enable-libass \
		--enable-libass-osd \
		--enable-libavdevice \
		--enable-libavfilter \
		--enable-libavresample \
		--enable-libbluray \
		--enable-libbs2b \
		--enable-libguess \
		--enable-libmpv-shared \
		--enable-libpostproc \
		--enable-libquvi4 \
		--enable-libsmbclient \
		--enable-libv4l2 \
		--enable-lirc \
		--enable-mpg123 \
		--enable-openal \
		--enable-oss-audio \
		--enable-portaudio \
		--enable-pulse \
		--enable-pvr \
		--enable-sdl1 \
		--enable-shm \
		--enable-terminfo \
		--enable-tv \
		--enable-tv-v4l2 \
		--enable-vaapi \
		--enable-vaapi-glx \
		--enable-vaapi-hwaccel \
		--enable-vaapi-vpp \
		--enable-vdpau \
		--enable-vdpau-gl-x11 \
		--enable-vdpau-hwaccel \
		--enable-wayland \
		--enable-x11 \
		--enable-xext \
		--enable-xf86vm \
		--enable-xf86xk \
		--enable-xinerama \
		--enable-xss \
		--enable-xv \
		--enable-zsh-comp \
		--lua=51pld

%waf build -v

%install
rm -rf $RPM_BUILD_ROOT

%waf install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/mpv
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/mpv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/mpv
%{_sysconfdir}/mpv/encoding-profiles.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mpv/mpv.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/mpv.desktop
%{_iconsdir}/hicolor/*/apps/mpv.png
%{_mandir}/man1/mpv.1*

%files client-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpv.so.1

%files client-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpv.so
%{_includedir}/mpv
%{_pkgconfigdir}/mpv.pc

%files -n zsh-completion-mpv
%defattr(644,root,root,755)
%{zshdir}/_mpv
