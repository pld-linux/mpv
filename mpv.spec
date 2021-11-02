#
# Conditional build:
%bcond_without	caca		# CACA
%bcond_without	dvdnav		# dvdnav support
%bcond_without	js		# JavaScript scripting support
%bcond_without	libplacebo	# libplacebo support
%bcond_without	rubberband	# librubberband support
%bcond_without	shaderc		# libshaderc SPIR-V compiler
%bcond_without	vapoursynth	# VapourSynth filter bridge
%bcond_without	zimg		# libzimg support (high quality software scaler)

Summary:	Movie player based on MPlayer and mplayer2
Summary(pl.UTF-8):	Odtwarzacz filmów oparty na projektach MPlayer i mplayer2
Name:		mpv
Version:	0.34.0
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
#Source0Download: http://github.com/mpv-player/mpv/releases
Source0:	https://github.com/mpv-player/mpv/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	14cd51160f41aee105d2b9d572bd8974
Source1:	%{name}.conf
Patch0:		%{name}-shaderc.patch
URL:		http://mpv.io/
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenAL-devel >= 1.13
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	alsa-lib-devel >= 1.0.18
BuildRequires:	docutils
BuildRequires:	ffmpeg-devel >= 4.0
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lcms2-devel >= 2.6
BuildRequires:	libarchive-devel >= 3.4.0
BuildRequires:	libass-devel >= 0.12.2
%ifarch	i386 i486
BuildRequires:	libatomic-devel
%endif
BuildRequires:	libbluray-devel >= 0.3.0
%{?with_caca:BuildRequires:	libcaca-devel >= 0.99-0.beta18.1}
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libdrm-devel >= 2.4.75
%if %{with dvdnav}
BuildRequires:	libdvdnav-devel >= 4.2.0
BuildRequires:	libdvdread-devel >= 4.1.0
%endif
BuildRequires:	libjpeg-devel
%{?with_libplacebo:BuildRequires:	libplacebo-devel >= 3.104.0}
BuildRequires:	libva-devel >= 1.4.0
BuildRequires:	libva-glx-devel >= 1.4.0
BuildRequires:	libvdpau-devel >= 0.2
BuildRequires:	lua52-devel
%{?with_js:BuildRequires:	mujs-devel >= 1.0.0}
BuildRequires:	nv-codec-headers >= 8.2.15.7
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 1.0
BuildRequires:	rpmbuild(macros) >= 1.719
%{?with_rubberband:BuildRequires:	rubberband-devel >= 1.8.0}
%{?with_shaderc:BuildRequires:	shaderc-devel >= 2019.0}
BuildRequires:	uchardet-devel
%{?with_vapoursynth:BuildRequires:	vapoursynth-devel >= 24}
BuildRequires:	waf >= 2.0.21
BuildRequires:	wayland-devel >= 1.15.0
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.14
BuildRequires:	xorg-lib-libX11-devel >= 1.0.0
BuildRequires:	xorg-lib-libXScrnSaver-devel >= 1.0.0
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.0.0
BuildRequires:	xorg-lib-libXinerama-devel >= 1.0.0
BuildRequires:	xorg-lib-libXrandr-devel >= 1.2.0
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.3.0
BuildRequires:	xorg-proto-xproto-devel
%{?with_zimg:BuildRequires:	zimg-devel >= 2.9}
BuildRequires:	zlib-devel
Requires:	OpenAL >= 1.13
Requires:	OpenGL
Requires:	alsa-lib >= 1.0.18
%requires_eq_to	ffmpeg-libs ffmpeg-devel
Requires:	lcms2 >= 2.6
Requires:	libarchive >= 3.4.0
Requires:	libass >= 0.12.2
Requires:	libbluray >= 0.3.0
%{?with_caca:Requires:	libcaca >= 0.99-0.beta18.1}
Requires:	libdrm >= 2.4.75
%if %{with dvdnav}
Requires:	libdvdnav >= 4.2.0
Requires:	libdvdread >= 4.1.0
%endif
%{?with_libplacebo:Requires:	libplacebo >= 3.104.0}
Requires:	libva >= 1.4.0
Requires:	libva-glx >= 1.4.0
Requires:	libvdpau >= 0.2
%{?with_js:Requires:	mujs >= 1.0.0}
Requires:	pulseaudio-libs >= 1.0
%{?with_rubberband:Requires:	rubberband-libs >= 1.8.0}
%{?with_shaderc:Requires:	shaderc >= 2019.0}
%{?with_vapoursynth:Requires:	vapoursynth >= 24}
Requires:	wayland >= 1.15.0
Requires:	xorg-lib-libX11 >= 1.0.0
Requires:	xorg-lib-libXScrnSaver >= 1.0.0
Requires:	xorg-lib-libXext >= 1.0.0
Requires:	xorg-lib-libXinerama >= 1.0.0
Requires:	xorg-lib-libXrandr >= 1.2.0
Requires:	xorg-lib-libxkbcommon >= 0.3.0
%{?with_zimg:Requires:	zimg >= 2.9}
Suggests:	yt-dlp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Movie player based on MPlayer and mplayer2.

%description -l pl.UTF-8
Odtwarzacz filmów oparty na projektach MPlayer i mplayer2.

%package client-libs
Summary:	Client library for controlling mpv
Summary(pl.UTF-8):	Biblioteka kliencka do sterowania odtwarzaczem mpv
Group:		Libraries

%description client-libs
Client library for controlling mpv.

%description client-libs -l pl.UTF-8
Biblioteka kliencka do sterowania odtwarzaczem mpv.

%package client-devel
Summary:	Development files for mpv client library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki klienckiej mpv
Group:		Development/Libraries
Requires:	%{name}-client-libs = %{version}-%{release}

%description client-devel
Development files for mpv client library.

%description client-devel -l pl.UTF-8
Pliki programistyczne biblioteki klienckiej mpv.

%package -n bash-completion-mpv
Summary:	Bash completion for mpv
Summary(pl.UTF-8):	Dopełnianie parametrów mpv dla powłoki Bash
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-mpv
Bash completion for mpv.

%description -n bash-completion-mpv -l pl.UTF-8
Dopełnianie parametrów mpv dla powłoki Bash.

%package -n zsh-completion-mpv
Summary:	ZSH completion for mpv
Summary(pl.UTF-8):	Dopełnianie parametrów mpv dla powłoki ZSH
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}

%description -n zsh-completion-mpv
ZSH completion for mpv.

%description -n zsh-completion-mpv -l pl.UTF-8
Dopełnianie parametrów mpv dla powłoki ZSH.

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
		%{__enable_disable caca} \
		--enable-cdda \
		--enable-cplugins \
		--enable-dvb \
		--enable-dvbin \
		%{__enable_disable dvdnav} \
		--enable-gl-wayland \
		--enable-gl-x11 \
		--enable-iconv \
		--enable-jack \
		%{__enable_disable js javascript} \
		--enable-jpeg \
		--enable-lcms2 \
		--enable-libavdevice \
		--enable-libbluray \
		--enable-libmpv-shared \
		%{__enable_disable libplacebo} \
		%{__enable_disable rubberband} \
		--enable-openal \
		--enable-pulse \
		--enable-sdl2 \
		%{__enable_disable shaderc} \
		--enable-uchardet \
		--enable-vaapi \
		%{__enable_disable vapoursynth} \
		--enable-vdpau \
		--enable-vdpau-gl-x11 \
		--enable-wayland \
		--enable-x11 \
		--enable-xv \
		%{__enable_disable zimg} \
		--lua=52deb \
		--bashdir=%{bash_compdir} \
		--zshdir=%{zsh_compdir}

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

%files -n bash-completion-mpv
%defattr(644,root,root,755)
%{bash_compdir}/mpv

%files -n zsh-completion-mpv
%defattr(644,root,root,755)
%{zsh_compdir}/_mpv
