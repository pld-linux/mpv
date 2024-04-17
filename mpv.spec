#
# Conditional build:
%bcond_without	caca		# CACA
%bcond_without	dvdnav		# dvdnav support
%bcond_without	js		# JavaScript scripting support
%bcond_without	rubberband	# librubberband support
%bcond_without	shaderc		# libshaderc SPIR-V compiler
%bcond_without	sixel		# sixel video output
%bcond_without	vapoursynth	# VapourSynth filter bridge
%bcond_without	zimg		# libzimg support (high quality software scaler)

Summary:	Movie player based on MPlayer and mplayer2
Summary(pl.UTF-8):	Odtwarzacz filmów oparty na projektach MPlayer i mplayer2
Name:		mpv
Version:	0.37.0
Release:	3
License:	GPL v2+
Group:		Applications/Multimedia
#Source0Download: http://github.com/mpv-player/mpv/releases
Source0:	https://github.com/mpv-player/mpv/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	54bd6864cc831f1fee6dee693a0421eb
Source1:	%{name}.conf
URL:		http://mpv.io/
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel >= 17.1.0
BuildRequires:	OpenAL-devel >= 1.13
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	Vulkan-Loader-devel >= 1.3.238
BuildRequires:	alsa-lib-devel >= 1.0.18
BuildRequires:	docutils
BuildRequires:	ffmpeg-devel >= 4.4
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lcms2-devel >= 2.6
BuildRequires:	libarchive-devel >= 3.4.0
BuildRequires:	libass-devel >= 0.12.2
%ifnarch %arch_with_atomics64
BuildRequires:	libatomic-devel
%endif
BuildRequires:	libbluray-devel >= 0.3.0
%{?with_caca:BuildRequires:	libcaca-devel >= 0.99-0.beta18.1}
BuildRequires:	libcdio-devel >= 0.90
BuildRequires:	libcdio-paranoia-devel
BuildRequires:	libdrm-devel >= 2.4.105
%if %{with dvdnav}
BuildRequires:	libdvdnav-devel >= 4.2.0
BuildRequires:	libdvdread-devel >= 4.1.0
%endif
BuildRequires:	libjpeg-devel
BuildRequires:	libplacebo-devel >= 6.338.0
%{?with_sixel:BuildRequires:	libsixel-devel >= 1.5}
BuildRequires:	libva-devel >= 1.4.0
BuildRequires:	libva-glx-devel >= 1.4.0
BuildRequires:	libvdpau-devel >= 0.2
BuildRequires:	lua52-devel
BuildRequires:	meson >= 0.62.0
%{?with_js:BuildRequires:	mujs-devel >= 1.0.0}
BuildRequires:	ninja
BuildRequires:	nv-codec-headers >= 11.1.5.1
BuildRequires:	pipewire-devel >= 0.3.48
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 1.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.025
%{?with_rubberband:BuildRequires:	rubberband-devel >= 1.8.0}
%{?with_shaderc:BuildRequires:	shaderc-devel >= 2019.0}
BuildRequires:	uchardet-devel
%{?with_vapoursynth:BuildRequires:	vapoursynth-devel >= 26}
BuildRequires:	wayland-devel >= 1.20.0
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.32
BuildRequires:	xorg-lib-libX11-devel >= 1.0.0
BuildRequires:	xorg-lib-libXScrnSaver-devel >= 1.0.0
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.0.0
BuildRequires:	xorg-lib-libXpresent-devel >= 1.0.0
BuildRequires:	xorg-lib-libXrandr-devel >= 1.4.0
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.3.0
BuildRequires:	xorg-proto-xproto-devel
%{?with_zimg:BuildRequires:	zimg-devel >= 3.0.5}
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	OpenAL >= 1.13
Requires:	OpenGL
Requires:	alsa-lib >= 1.0.18
Requires:	hicolor-icon-theme
%requires_eq_to	ffmpeg-libs ffmpeg-devel
Requires:	lcms2 >= 2.6
Requires:	libarchive >= 3.4.0
Requires:	libass >= 0.12.2
Requires:	libbluray >= 0.3.0
%{?with_caca:Requires:	libcaca >= 0.99-0.beta18.1}
Requires:	libdrm >= 2.4.105
%if %{with dvdnav}
Requires:	libdvdnav >= 4.2.0
Requires:	libdvdread >= 4.1.0
%endif
Requires:	pipewire-libs >= 0.3.48
%requires_ge_to	libplacebo libplacebo-devel
%{?with_sixel:Requires:	libsixel >= 1.5}
Requires:	libva >= 1.4.0
Requires:	libva-glx >= 1.4.0
Requires:	libvdpau >= 0.2
%{?with_js:Requires:	mujs >= 1.0.0}
Requires:	pulseaudio-libs >= 1.0
%{?with_rubberband:Requires:	rubberband-libs >= 1.8.0}
%{?with_shaderc:Requires:	shaderc >= 2019.0}
%{?with_vapoursynth:Requires:	vapoursynth >= 26}
Requires:	wayland >= 1.15.0
Requires:	xorg-lib-libX11 >= 1.0.0
Requires:	xorg-lib-libXScrnSaver >= 1.0.0
Requires:	xorg-lib-libXext >= 1.0.0
Requires:	xorg-lib-libXrandr >= 1.4.0
Requires:	xorg-lib-libxkbcommon >= 0.3.0
%{?with_zimg:Requires:	zimg >= 3.0.5}
Suggests:	yt-dlp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-mpv
Bash completion for mpv.

%description -n bash-completion-mpv -l pl.UTF-8
Dopełnianie parametrów mpv dla powłoki Bash.

%package -n zsh-completion-mpv
Summary:	ZSH completion for mpv
Summary(pl.UTF-8):	Dopełnianie parametrów mpv dla powłoki ZSH
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description -n zsh-completion-mpv
ZSH completion for mpv.

%description -n zsh-completion-mpv -l pl.UTF-8
Dopełnianie parametrów mpv dla powłoki ZSH.

%prep
%setup -q

%build
%meson build \
	-Dalsa=enabled \
	-Dcaca=%{__enabled_disabled caca} \
	-Dcdda=enabled \
	-Dcplugins=enabled \
	-Ddvbin=enabled \
	-Ddvdnav=%{__enabled_disabled dvdnav} \
	-Degl-wayland=enabled \
	-Degl-x11=enabled \
	-Dgl-x11=enabled \
	-Diconv=enabled \
	-Djack=enabled \
	-Djavascript=%{__enabled_disabled js} \
	-Djpeg=enabled \
	-Dlcms2=enabled \
	-Dlibavdevice=enabled \
	-Dlibbluray=enabled \
	-Dlibmpv=true \
	-Drubberband=%{__enabled_disabled rubberband} \
	-Dopenal=enabled \
	-Dpulse=enabled \
	-Dsdl2=enabled \
	-Dshaderc=%{__enabled_disabled shaderc} \
	-Dsixel=%{__enabled_disabled sixel} \
	-Duchardet=enabled \
	-Dvaapi=enabled \
	-Dvapoursynth=%{__enabled_disabled vapoursynth} \
	-Dvdpau=enabled \
	-Dvdpau-gl-x11=enabled \
	-Dwayland=enabled \
	-Dx11=enabled \
	-Dxv=enabled \
	-Dzimg=%{__enabled_disabled zimg} \
	-Dlua=lua5.2

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

install -d $RPM_BUILD_ROOT%{_sysconfdir}/mpv
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/mpv

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

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
%{_datadir}/metainfo/mpv.metainfo.xml

%files client-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpv.so.2

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
