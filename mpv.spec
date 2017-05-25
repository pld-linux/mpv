Summary:	Movie player based on MPlayer and mplayer2
Name:		mpv
Version:	0.25.0
Release:	3
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	http://github.com/mpv-player/mpv/archive/v%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	73b3d233c3b4428d0cfd5491c5cb6c41
Source1:	%{name}.conf
Patch0:		%{name}-lua.patch
URL:		http://mpv.io/
BuildRequires:	Mesa-libEGL-devel >= 9.0.0
BuildRequires:	Mesa-libwayland-egl-devel >= 9.0.0
BuildRequires:	OpenAL-devel >= 1.13
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel >= 1.0.18
BuildRequires:	docutils
BuildRequires:	ffmpeg-devel >= 3.2.2
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lcms2-devel >= 2.6
BuildRequires:	libass-devel >= 0.12.1
%ifarch	i386 i486
BuildRequires:	libatomic-devel
%endif
BuildRequires:	libbluray-devel >= 0.3.0
BuildRequires:	libcaca-devel >= 0.99-0.beta18.1
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libdvdnav-devel >= 4.2.0
BuildRequires:	libdvdread-devel >= 4.1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libv4l-devel
BuildRequires:	libva-devel >= 1.4.0
BuildRequires:	libva-glx-devel >= 1.4.0
BuildRequires:	libvdpau-devel >= 0.2
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 1.0
BuildRequires:	rpmbuild(macros) >= 1.336
BuildRequires:	uchardet-devel
BuildRequires:	waf >= 1.8.12
BuildRequires:	wayland-devel >= 1.3.0
BuildRequires:	xorg-lib-libX11-devel >= 1.0.0
BuildRequires:	xorg-lib-libXScrnSaver-devel >= 1.0.0
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.0.0
BuildRequires:	xorg-lib-libXinerama-devel >= 1.0.0
BuildRequires:	xorg-lib-libXrandr-devel >= 1.2.0
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.3.0
BuildRequires:	xorg-proto-xproto-devel
Requires:	Mesa-libwayland-egl >= 9.0.0
Requires:	OpenAL >= 1.13
Requires:	OpenGL
Requires:	alsa-lib >= 1.0.18
%requires_eq	ffmpeg-libs
Requires:	lcms2 >= 2.6
Requires:	libass >= 0.12.1
Requires:	libbluray >= 0.3.0
Requires:	libcaca >= 0.99-0.beta18.1
Requires:	libdvdnav >= 4.2.0
Requires:	libdvdread >= 4.1.0
Requires:	libva >= 1.4.0
Requires:	libva-glx >= 1.4.0
Requires:	libvdpau >= 0.2
Requires:	pulseaudio-libs >= 1.0
Requires:	wayland >= 1.6.0
Requires:	xorg-lib-libX11 >= 1.0.0
Requires:	xorg-lib-libXScrnSaver >= 1.0.0
Requires:	xorg-lib-libXext >= 1.0.0
Requires:	xorg-lib-libXinerama >= 1.0.0
Requires:	xorg-lib-libXrandr >= 1.2.0
Requires:	xorg-lib-libxkbcommon >= 0.3.0
Suggests:	youtube-dl >= 2:20150223
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		zshdir %{_datadir}/zsh/site-functions

%description
Movie player based on MPlayer and mplayer2.

%package client-libs
Summary:	Client library for controlling mpv
Group:		Development/Libraries

%description client-libs
Client library for controlling mpv.

%package client-devel
Summary:	Development files for mpv client library
Group:		Development/Libraries
Requires:	%{name}-client-libs = %{version}-%{release}

%description client-devel
Development files for mpv client library.

%package -n zsh-completion-mpv
Summary:	zsh-completion for mpv
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}

%description -n zsh-completion-mpv
zsh-completion for mpv.

%prep
%setup -q
%patch0 -p1

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
		--enable-cplugins \
		--enable-dvb \
		--enable-dvbin \
		--enable-dvdnav \
		--enable-dvdread \
		--enable-encoding \
		--enable-gl-wayland \
		--enable-gl-x11 \
		--enable-iconv \
		--enable-jack \
		--enable-jpeg \
		--enable-lcms2 \
		--enable-libass \
		--enable-libass-osd \
		--enable-libavdevice \
		--enable-libbluray \
		--enable-libmpv-shared \
		--enable-libsmbclient \
		--enable-libv4l2 \
		--enable-openal \
		--enable-oss-audio \
		--enable-pulse \
		--enable-sdl1 \
		--enable-shm \
		--enable-tv \
		--enable-tv-v4l2 \
		--enable-uchardet \
		--enable-vaapi \
		--enable-vaapi-glx \
		--enable-vaapi-hwaccel \
		--enable-vdpau \
		--enable-vdpau-gl-x11 \
		--enable-vdpau-hwaccel \
		--enable-wayland \
		--enable-x11 \
		--enable-xv \
		--enable-zsh-comp \
		--lua=51pld \
		--zshdir=%{zshdir}

%waf build -v

%install
rm -rf $RPM_BUILD_ROOT

%waf install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/mpv
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/mpv

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	client-libs -p /sbin/ldconfig
%postun	client-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md RELEASE_NOTES etc/input.conf etc/mplayer-input.conf etc/mpv.conf etc/restore-old-bindings.conf
%dir %{_sysconfdir}/mpv
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mpv/encoding-profiles.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mpv/mpv.conf
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/mpv.desktop
%{_iconsdir}/hicolor/*/apps/mpv.png
%{_iconsdir}/hicolor/scalable/apps/mpv.svg
%{_iconsdir}/hicolor/symbolic/apps/mpv-symbolic.svg
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
