#
# Conditional build:
%bcond_with	directfb	# DirectFB graphics support
%bcond_with	nas		# NAS audio support
%bcond_without	alsa		# ALSA audio support
%bcond_with	arts		# aRts audio support
%bcond_with	esd		# EsounD audio support
%bcond_with	jack		# JACK audio support
%bcond_without	opengl		# OpenGL (GLX) support
%bcond_without	gles		# OpenGL ES (EGL) support
%bcond_with	kms		# KMS/DRM graphics support
%bcond_without	pipewire	# Pipewire audio support
%bcond_without	vulkan		# Vulkan graphics support
%bcond_without	wayland		# Wayland graphics support
%bcond_without	fcitx		# Fcitx IM support
%bcond_without	ibus		# IBus IM support
%bcond_without	static_libs	# don't build static libraries
%bcond_with	mmx		# MMX instructions
%bcond_with	sse		# SSE instructions
%bcond_with	sse2		# SSE2 instructions
%bcond_with	3dnow		# 3Dnow! instructions
%bcond_with	altivec		# Altivec instructions
#
# NOTE: the following libraries are dlopened by soname detected at build time:
# libartsc.so.?			[if with arts]
# libasound.so.2		[if with alsa]
# libaudio.so.2			[if with nas]
# libdirectfb-*.so --needs patch (-release not supported by configure)
# libdrm.so.2			[if with kms]
# libesd.so.0			[if with esd]
# libfusionsound-*.so --needs patch (-release not supported by configure)
# libgbm.so.1			[if with kms]
# libjack.so.0			[if with jack]
# libpipewire-0.3.so.0
# libpulse-simple.so.0
# libsamplerate.so.0
# libwayland-client.so.0	[if with wayland]
# libwayland-cursor.so.0	[if with wayland]
# libwayland-egl.so.1		[if with wayland]
# libxkbcommon.so.0		[if with wayland]
# libX11.so.6
# libXcursor.so.1
# libXext.so.6
# libXi.so.6
# libXrandr.so.2
# libXrender.so.1
# libXss.so.1
%ifarch k6 athlon
%define	with_3dnow	1
%endif
%ifarch %{x8664} x32 pentium2 pentium3 pentium4 athlon
%define	with_mmx	1
%endif
%ifarch %{x8664} x32 pentium3 pentium4
%define	with_sse	1
%endif
%ifarch %{x8664} x32 pentium4
%define	with_sse2	1
%endif
Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Summary(pl.UTF-8):	SDL (Simple DirectMedia Layer) - Biblioteka do gier/multimediów
Summary(zh_CN.UTF-8):	SDL (Simple DirectMedia Layer) Generic APIs - 游戏/多媒体库
Name:		SDL2
Version:	2.30.11
Release:	1
License:	Zlib (BSD-like)
Group:		Libraries
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	bea190b480f6df249db29eb3bacfe41e
Patch0:		%{name}-config.patch
URL:		http://www.libsdl.org/
%{?with_kms:BuildRequires:	Mesa-libgbm-devel >= 11.1.0}
%{?with_directfb:BuildRequires:	DirectFB-devel >= 1.0.0}
%if %{with opengl} || %{with gles}
BuildRequires:	EGL-devel
%endif
%{?with_directfb:BuildRequires:	FusionSound-devel >= 1.1.1}
%{?with_opengl:BuildRequires:	OpenGL-GLX-devel}
%{?with_gles:BuildRequires:	OpenGLES-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.11}
%{?with_arts:BuildRequires:	artsc-devel >= 1.1}
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
BuildRequires:	dbus-devel
%{?with_esd:BuildRequires:	esound-devel >= 0.2.8}
%{?with_fcitx:BuildRequires:	fcitx-devel}
BuildRequires:	gcc >= 5:4.0
BuildRequires:	hidapi-devel
%{?with_ibus:BuildRequires:	ibus-devel >= 1.0}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel >= 0.125}
%{?with_kms:BuildRequires:	libdrm-devel >= 1.4.82}
BuildRequires:	libsamplerate-devel
BuildRequires:	libtool >= 2:2.0
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	perl-modules
%{?with_pipewire:BuildRequires:	pipewire-devel >= 0.3.20}
BuildRequires:	pkgconfig >= 1:0.7
BuildRequires:	pulseaudio-devel >= 0.9.15
BuildRequires:	rpm-build >= 4.6
BuildRequires:	udev-devel
# wayland-client, wayland-cursor
%{?with_wayland:BuildRequires:	wayland-devel >= 1.18}
%{?with_wayland:BuildRequires:	wayland-egl-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
%if %{with wayland}
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.5.0
%endif
BuildRequires:	xorg-proto-xextproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ppc	-maltivec

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

%description -l pl.UTF-8
SDL (Simple DirectMedia Layer) jest biblioteką udostępniającą
przenośny, niskopoziomowy dostęp do bufora ramki video, wyjścia audio,
myszy oraz klawiatury. Może obsługiwać zarówno okienkowy tryb XFree86
jak i DGA. Konstruując ją miano na uwadze przenośność: aplikacje
konsolidowane z SDL można również budować w systemach Win32 i BeOS.

%description -l pt_BR.UTF-8
Esse é o Simple DirectMedia Layer, uma API genérica que dá acesso de
baixo nível a áudio, teclado, mouse e vídeo em várias plataformas.

Essa biblioteca é usada por alguns jogos.

%description -l ru.UTF-8
SDL (Simple DirectMedia Layer) это набор функций, предоставляющий
низкоуровневый доступ к звуку, клавиатуре, манипулятору мышь и к
буферу экрана на множестве различных платформ.

%package devel
Summary:	SDL - Header files
Summary(pl.UTF-8):	SDL - Pliki nagłówkowe
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de cabeçalho para aplicações SDL
Summary(ru.UTF-8):	Файлы, необходимые для разработки программ, использующих SDL
Summary(uk.UTF-8):	Файли, необхідні для розробки програм, що використовують SDL
Summary(zh_CN.UTF-8):	SDL (Simple DirectMedia Layer) 开发库
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_directfb:Requires:	DirectFB-devel >= 1.0.0}
Requires:	xorg-lib-libX11-devel
Suggests:	OpenGL-GLU-devel

%description devel
SDL - Header files.

%description devel -l pl.UTF-8
SDL - Pliki nagłówkowe.

%description devel -l pt_BR.UTF-8
Esse pacote contém bibliotecas, arquivos de cabeçalho e outros
recursos para o desenvolvimento de aplicativos com SDL.

%description devel -l ru.UTF-8
Этот пакет содержит файлы, необходимые для разработки программ,
использующих SDL.

%description devel -l uk.UTF-8
Цей пакет містить файли, необхідні для розробки програм, що
використовують SDL.

%package static
Summary:	SDL - static libraries
Summary(pl.UTF-8):	SDL - biblioteki statyczne
Summary(pt_BR.UTF-8):	Biblioteca estática para desenvolvimento de aplicações com a SDL
Summary(ru.UTF-8):	Статические библиотеки для разработки с использованием SDL
Summary(uk.UTF-8):	Статичні бібліотеки для розробки з використанням SDL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
SDL - static libraries.

%description static -l pl.UTF-8
SDL - biblioteki statyczne.

%description static -l pt_BR.UTF-8
Biblioteca estática para desenvolvimento de aplicações com a SDL.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки для разработки программ,
использующих SDL.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки для розробки програм, що
використовують SDL.

%package examples
Summary:	SDL - example programs
Summary(pl.UTF-8):	SDL - programy przykładowe
License:	Public Domain
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch

%description examples
SDL - example programs.

%description examples -l pl.UTF-8
SDL - przykładowe programy.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I acinclude
%{__autoconf}
%configure \
	%{?with_3dnow:--enable-3dnow} \
	%{!?with_alsa:--disable-alsa} \
	%{!?with_altiveca:--disable-altivec} \
	%{!?with_arts:--disable-arts} \
	%{!?with_esd:--disable-esd} \
	%{!?with_fcitx:--disable-fcitx} \
	%{!?with_ibus:--disable-ibus} \
	%{!?with_jack:--disable-jack} \
	%{!?with_mmx:--disable-mmx} \
	%{!?with_nas:--disable-nas} \
	%{!?with_pipewire:--disable-pipewire} \
	--enable-pthreads \
	--enable-pthread-sem \
	--disable-rpath \
	%{!?with_sse:--disable-sse --disable-ssemath} \
	%{!?with_sse2:--disable-sse2} \
	%{?with_sse:--enable-ssemath} \
	%{!?with_static_libs:--disable-static} \
	%{!?with_directfb:--disable-video-directfb} \
	%{?with_kms:--enable-video-kmsdrm} \
	--enable-video-opengl%{!?with_opengl:=no} \
	--enable-video-opengles%{!?with_gles:=no} \
	--enable-video-vulkan%{!?with_vulkan:=no} \
	--enable-video-wayland%{!?with_wayland:=no} \
	--with-x

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

cp -pr test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# non-Linux READMEs packaged for portability information
%doc BUGS.txt CREDITS.txt LICENSE.txt README*.txt TODO.txt WhatsNew.txt
%attr(755,root,root) %{_libdir}/libSDL2-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL2-2.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sdl2-config
%attr(755,root,root) %{_libdir}/libSDL2.so
%{_libdir}/libSDL2.la
%{_libdir}/libSDL2_test.a
%{_libdir}/libSDL2_test.la
%{_libdir}/libSDL2main.a
%{_libdir}/libSDL2main.la
%{_includedir}/SDL2
%{_aclocaldir}/sdl2.m4
%{_pkgconfigdir}/sdl2.pc
%{_libdir}/cmake/SDL2

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL2.a
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
