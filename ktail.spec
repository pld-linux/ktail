Summary:	ktail - monitors files (like tail -f) and pipes
Summary(pl):	ktail - do monitorowania plik�w (jak tail -f) i rurek
Name:		ktail
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Vendor:		Rolf Jakob <rjakob@duffy1.franken.de>
Source0:	ftp://ftp.kde.org/pub/kde/unstable/apps/utils/%{name}-%{version}.tar.bz2
URL:		http://www.franken.de/users/duffy1/rjakob
BuildRequires:	qt-devel >= 1.30
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ktail monitors multiple files and/or command output in one window.
Files and commands may be added and removed via drag'n'drop or menu
options.

%description -l pl
ktail monitoruje wiele plik�w lub wyj�� z komend w jednym okienku.
Pliki i komendy mog� by� dodawane i usuane poprzez przesun-i-upu�� lub
z menu.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags}" CFLAGS="%{rpmcflags}" ./configure \
	--prefix=%{_prefix} --with-install-root=$RPM_BUILD_ROOT
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktail
%{_applnkdir}/Utilities/ktail.kdelnk
%{_docdir}/doc/HTML/en/ktail/index.html
%{_pixmapsdir}/ktail.xpm
%{_pixmapsdir}/mini/ktail.xpm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/ktail.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/ktail.mo
