Summary:	MagicPoint is a X11 Presentation Application
Summary(pl):	MagicPoint - program do grafiki prezentacyjnej pod X11
Name:		magicpoint
Version:	1.04a
Release:	4
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.mew.org/pub/MagicPoint/%{name}-%{version}.tar.gz
URL:		http://www.mew.org/mgp/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	mgp

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
MagicPoint is an X11 based presentation tool. It is designed to make simple
presentations easy while to make complicated presentations possible. Its
presentation file (whose suffix is typically .mgp) is just text so that you
can create presentation files quickly with your favorite editor (e.g. VI).

%description -l pl
MagicPoint jest narzêdziem do robienia grafiki prezentacyjnej pod X11.
Zosta³ on zrobiony do tworzenia prostych prezentacji. Pliki z opisem
prezentacji (z rozszerzeniem .mgp) s± plikami tekstowymi, wiêc sam±
prezentacjê mo¿na szybko przygotowaæ z u¿yciem ulubionego edytora.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--enable-freetype

xmkmf -a
make LIBDIR=%{_datadir}

%install
rm -rf $RPM_BUILD_ROOT
make install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_datadir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README SYNTAX USAGE sample/*.{mgp,gif,eps}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mgp
%{_mandir}/man1/*
