Summary:	MagicPoint is a X11 Presentation Application
Summary(pl):	MagicPoint - program do grafiki prezentacyjnej pod X11
Name:		magicpoint
Version:	1.07a
Release:	5
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.mew.org/pub/MagicPoint/%{name}-%{version}.tar.gz
URL:		http://www.mew.org/mgp/
BuildRequires:	XFree86-devel
BuildRequires:	freetype1-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mgp

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
MagicPoint is an X11 based presentation tool. It is designed to make
simple presentations easy while to make complicated presentations
possible. Its presentation file (whose suffix is typically .mgp) is
just text so that you can create presentation files quickly with your
favorite editor (e.g. VI).

%description -l pl
MagicPoint jest narzêdziem do robienia grafiki prezentacyjnej pod X11.
Zosta³ on zrobiony do tworzenia prostych prezentacji. Pliki z opisem
prezentacji (z rozszerzeniem .mgp) s± plikami tekstowymi, wiêc sam±
prezentacjê mo¿na szybko przygotowaæ z u¿yciem ulubionego edytora.

%prep
%setup -q

%build
#aclocal
#autoconf
%configure2_13 \
	--enable-freetype

xmkmf -a
%{__make} LIBDIR=%{_datadir} \
	CXXDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_datadir}

gzip -9nf README SYNTAX USAGE FAQ RELNOTES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz sample/*.{mgp,jpg,eps}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mgp
%{_mandir}/man1/*
