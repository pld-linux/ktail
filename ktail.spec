Summary:	ktail - monitors files (like tail -f) and pipes
Summary(pl):	ktail - do monitorowania plików (jak tail -f) i rurek
Name:		ktail
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Rolf Jakob <rjakob@duffy1.franken.de>
Source0:	http://www.franken.de/users/duffy1/rjakob/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-acfix.patch
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
ktail monitoruje wiele plików lub wyj¶æ z komend w jednym okienku.
Pliki i komendy mog± byæ dodawane i usuane poprzez przesun-i-upu¶æ lub
z menu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure \
	--prefix=%{_prefix} \
	--with-install-root=$RPM_BUILD_ROOT
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
