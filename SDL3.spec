#
# Conditional build:
%bcond_without	alsa		# ALSA audio support
%bcond_with	jack		# JACK audio support
%bcond_without	opengl		# OpenGL (GLX) support
%bcond_without	gles		# OpenGL ES (EGL) support
%bcond_with	kms		# KMS/DRM graphics support
%bcond_without	pipewire	# Pipewire audio support
%bcond_without	vulkan		# Vulkan graphics support
%bcond_without	wayland		# Wayland graphics support
%bcond_without	ibus		# IBus IM support
%bcond_without	static_libs	# static library
%bcond_with	avx		# AVX instructions
%bcond_with	avx2		# AVX2 instructions
%bcond_with	avx512f		# AVX512F instructions
%bcond_with	mmx		# MMX instructions
%bcond_with	neon		# NEON instructions
%bcond_with	sse		# SSE instructions
%bcond_with	sse2		# SSE2 instructions
%bcond_with	sse3		# SSE3 instructions
%bcond_with	sse41		# SSE4.1 instructions
%bcond_with	sse42		# SSE4.2 instructions
%bcond_with	altivec		# Altivec instructions
#
# NOTE: the following libraries are dlopened by soname detected at build time:
# libasound.so.2		[if with alsa]
# libdecor-0.so.0		[if with wayland]
# libdrm.so.2			[if with kms]
# libgbm.so.1			[if with kms]
# libjack.so.0			[if with jack]
# libpipewire-0.3.so.0
# libpulse-simple.so.0
# libudev.so.1
# libusb-1.0.so.0
# libwayland-client.so.0	[if with wayland]
# libwayland-cursor.so.0	[if with wayland]
# libwayland-egl.so.1		[if with wayland]
# libxkbcommon.so.0		[if with wayland]
# libX11.so.6
# libXcursor.so.1
# libXext.so.6
# libXfixes.so.3
# libXi.so.6
# libXrandr.so.2
# libXrender.so.1
# libXss.so.1
%ifarch %{x8664} x32 pentium2 pentium3 pentium4 athlon
%define	with_mmx	1
%endif
%ifarch %{x8664} x32 pentium3 pentium4
%define	with_sse	1
%endif
%ifarch %{x8664} x32 pentium4
%define	with_sse2	1
%endif
%ifarch %{arm_with_neon}
%define	with_neon	1
%endif
Summary:	SDL (Simple DirectMedia Layer) - Game/Multimedia Library
Summary(pl.UTF-8):	SDL (Simple DirectMedia Layer) - Biblioteka do gier/multimediów
Summary(zh_CN.UTF-8):	SDL (Simple DirectMedia Layer) Generic APIs - 游戏/多媒体库
Name:		SDL3
Version:	3.2.8
Release:	1
License:	Zlib (BSD-like)
Group:		Libraries
Source0:	http://www.libsdl.org/release/%{name}-%{version}.tar.gz
# Source0-md5:	285f86b00bea955bf521e91ba4c66d59
URL:		http://www.libsdl.org/
%{?with_kms:BuildRequires:	Mesa-libgbm-devel >= 11.1.0}
%if %{with opengl} || %{with gles} || %{with wayland}
BuildRequires:	EGL-devel
%endif
%{?with_opengl:BuildRequires:	OpenGL-GLX-devel}
%{?with_opengl:BuildRequires:	OpenGL-devel}
%{?with_gles:BuildRequires:	OpenGLES-devel}
%{?with_gles:BuildRequires:	OpenGLESv2-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 1.0.11}
BuildRequires:	cmake >= 3.16
BuildRequires:	dbus-devel
BuildRequires:	gcc >= 5:4.0
%{?with_ibus:BuildRequires:	ibus-devel >= 1.0}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel >= 0.125}
%{?with_wayland:BuildRequires:	libdecor-devel >= 0.2.0}
%{?with_kms:BuildRequires:	libdrm-devel >= 1.4.82}
BuildRequires:	liburing-ffi-devel
BuildRequires:	libusb-devel >= 1.0.16
BuildRequires:	perl-modules
%{?with_pipewire:BuildRequires:	pipewire-devel >= 0.3.44}
BuildRequires:	pkgconfig >= 1:0.7
BuildRequires:	pulseaudio-devel >= 0.9.15
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.007
BuildRequires:	udev-devel
# wayland-client, wayland-cursor
%{?with_wayland:BuildRequires:	wayland-devel >= 1.18}
%{?with_wayland:BuildRequires:	wayland-egl-devel}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
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
Requires:	%{name}%{?_isa} = %{version}-%{release}
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
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

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

%{__sed} -i -e '1s,.*env python\b,#!%{__python3},' test/emscripten/{driver,server}.py

%build
%cmake -B build \
	%{cmake_on_off alsa SDL_ALSA} \
	%{cmake_on_off altivec SDL_ALTIVEC} \
	%{cmake_on_off neon SDL_ARMNEON} \
	%{cmake_on_off avx SDL_AVX} \
	%{cmake_on_off avx2 SDL_AVX2} \
	%{cmake_on_off avx512f SDL_AVX512F} \
	%{cmake_on_off ibus SDL_IBUS} \
	%{cmake_on_off jack SDL_JACK} \
	%{cmake_on_off mmx SDL_MMX} \
	%{cmake_on_off pipewire SDL_PIPEWIRE} \
	-DSDL_PTHREADS:BOOL=ON \
	-DSDL_PTHREADS_SEM:BOOL=ON \
	-DSDL_RPATH:BOOL=OFF \
	%{cmake_on_off sse SDL_SSE} \
	%{cmake_on_off sse2 SDL_SSE2} \
	%{cmake_on_off sse41 SDL_SSE4_1} \
	%{cmake_on_off sse42 SDL_SSE4_2} \
	%{cmake_on_off static_libs SDL_STATIC} \
	%{cmake_on_off kms SDL_KMSDRM} \
	%{cmake_on_off opengl SDL_OPENGL} \
	%{cmake_on_off gles SDL_OPENGLES} \
	%{cmake_on_off vulkan SDL_VULKAN} \
	%{cmake_on_off wayland SDL_WAYLAND} \
	-DSDL_X11:BOOL=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cp -pr test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS.txt CREDITS.md LICENSE.txt README.md WhatsNew.txt
%attr(755,root,root) %{_libdir}/libSDL3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL3.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL3.so
%{_libdir}/libSDL3_test.a
%{_includedir}/SDL3
%{_pkgconfigdir}/sdl3.pc
%{_libdir}/cmake/SDL3

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL3.a
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
