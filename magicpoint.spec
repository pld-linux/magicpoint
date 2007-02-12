Summary:	MagicPoint is a X11 Presentation Application
Summary(pl.UTF-8):   MagicPoint - program do grafiki prezentacyjnej pod X11
Name:		magicpoint
Version:	1.10a
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.mew.org/pub/mgp/%{name}-%{version}.tar.gz
# Source0-md5:	7a5d91b2b3bdabea704ee3cb6505d772
Patch0:		%{name}-freetype.patch
Patch1:		%{name}-ac.patch
URL:		http://www.mew.org/mgp/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
# blegh, freetype2 is used for Xft2, but obsolete freetype1 is used to access TTFs :/
BuildRequires:	freetype1-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	giflib-devel
BuildRequires:	imlib-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	xft-devel
Requires:	libjpeg-progs
Obsoletes:	mgp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MagicPoint is an X11 based presentation tool. It is designed to make
simple presentations easy while to make complicated presentations
possible. Its presentation file (whose suffix is typically .mgp) is
just text so that you can create presentation files quickly with your
favorite editor (e.g. VI).

%description -l pl.UTF-8
MagicPoint jest narzędziem do robienia grafiki prezentacyjnej pod X11.
Został on zrobiony do tworzenia prostych prezentacji. Pliki z opisem
prezentacji (z rozszerzeniem .mgp) są plikami tekstowymi, więc samą
prezentację można szybko przygotować z użyciem ulubionego edytora.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .orig

%build
cp -f %{_datadir}/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	mgp_cv_path_uuencode="/usr/bin/uuencode" \
	mgp_cv_path_uudecode="/usr/bin/uudecode" \
	--enable-gif \
	--enable-imlib

xmkmf -a
%{__make} \
	LIBDIR=%{_datadir} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	LIBDIR=%{_datadir} \
	MANDIR=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README SYNTAX USAGE FAQ RELNOTES sample/*.{mgp,jpg,eps}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mgp
%{_mandir}/man1/*
