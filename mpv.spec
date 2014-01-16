Summary:	Movie player based on MPlayer and mplayer2
Name:		mpv
Version:	0.3.3
Release:	2
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	http://github.com/mpv-player/mpv/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	bdf40570d1fc025058f9f2aabb91899f
Source1:	%{name}.conf
URL:		http://mpv.io/
BuildRequires:	Mesa-libwayland-egl-devel >= 9.0.0
BuildRequires:	OpenAL-devel >= 1.13
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	enca-devel
BuildRequires:	ffmpeg-devel >= 1.1.0
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
BuildRequires:	lcms2-devel
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
BuildRequires:	libmpg123-devel >= 1.2.0
BuildRequires:	libquvi-devel < 0.9.0
BuildRequires:	libsmbclient-devel
BuildRequires:	libv4l-devel
BuildRequires:	libva-devel >= 1.2.0
BuildRequires:	libva-glx-devel >= 1.2.0
BuildRequires:	libvdpau-devel >= 0.2
BuildRequires:	lirc-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel >= 19
BuildRequires:	pulseaudio-devel >= 0.9
BuildRequires:	rpmbuild(macros) >= 1.336
# version dep to handle packaging issue in PLD
BuildRequires:	waf >= 1.7.14
BuildRequires:	wayland-devel >= 1.2.0
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

%description
Movie player based on MPlayer and mplayer2.

%prep
%setup -q

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
		--enable-gl-wayland \
		--enable-gl-x11 \
		--enable-iconv \
		--enable-jack \
		--enable-joystick \
		--enable-jpeg \
		--enable-ladspa \
		--enable-lcms2 \
		--enable-libass \
		--enable-libbluray \
		--enable-libbs2b \
		--enable-libguess \
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
		--enable-radio \
		--enable-radio-capture \
		--enable-radio-v4l2 \
		--enable-sdl \
		--enable-shm \
		--enable-terminfo \
		--enable-tv \
		--enable-tv-v4l2 \
		--enable-wayland \
		--enable-vaapi \
		--enable-vaapi-glx \
		--enable-vaapi-hwaccel \
		--enable-vaapi-vpp \
		--enable-vcd \
		--enable-vdpau \
		--enable-vdpau-hwaccel \
		--enable-x11 \
		--enable-xext \
		--enable-xf86vm \
		--enable-xf86xk \
		--enable-xinerama \
		--enable-xss \
		--enable-xv

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
