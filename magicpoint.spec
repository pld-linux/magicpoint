Summary:     MagicPoint is a X11 Presentation Application
Summary(pl): MagicPoint - program do grafiki prezentacyjnej pod X11
Name:        magicpoint
Version:     1.04a
Release:     3
Copyright:   GPL
Group:       X11/Applications/Graphics
Group(pl):   X11/Aplikacje/Grafika
Source:      ftp://ftp.mew.org/pub/MagicPoint/%{name}-%{version}.tar.gz
URL:         http://www.mew.org/mgp/
BuildRoot:   /tmp/%{name}-%{version}-root
Obsoletes:   mgp

%description
MagicPoint is an X11 based presentation tool. It is designed to make simple
presentations easy while to make complicated presentations possible. Its
presentation file (whose suffix is typically .mgp) is just text so that you
can create presentation files quickly with your favorite editor (e.g. VI).

%description
MagicPoint jest narzêdziem do robienia grafiki prezentacyjnej pod X11.
Zosta³ on zrobiony do tworzenia prostych prezentacji. Pliki z opisem
prezentacji (z rozszerzeniem .mgp) s± plikami tekstowymi tak wiêc sam±
prezentacjê mo¿na szybko przygotowaæ z u¿yciem ulubionego edytora.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6 \
	--enable-freetype

xmkmf -a
make LIBDIR=/usr/X11R6/share

%install
rm -rf $RPM_BUILD_ROOT
make install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=/usr/X11R6/share

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README SYNTAX USAGE sample/*.{mgp,gif,eps}
%attr(755, root, root) /usr/X11R6/bin/*
/usr/X11R6/share/mgp
%attr(644, root,  man) /usr/X11R6/man/man1/*

%changelog
* Sat Dec 19 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.04a-3]
- added gzipping man pages,
- added misiing %attr ofrm man pages,
- fixed pl translation (thanks for Micha³ Kuratczyk).

* Mon Dec  9 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.04a-2]
- added gzipping man pages,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- LIBDIR changed to /usr/X11R6/share,
- added using %%{name} and %%{version} in Source,
- added using LDFLAGS="-s" to ./configure enviroment,
- Group changed to X11/Applications/Graphics,
- added pl translation,
- added full %attr description in %files.

* Fri Oct 08 1998 Michael Maher <mike@redhat.com> 
- updated source to 1.04a
- built for 5.2

* Fri May 22 1998 Cristian Gafton <gafton@redhat.com>
- built for PowerTools
