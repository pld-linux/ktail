Summary:	ktail - monitors files (like tail -f) and pipes
Summary(pl):	ktail - do monitorowania plików (jak tail -f) i rurek
Name:		ktail
Version:	0.6.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Vendor:		Rolf Jakob <rjakob@duffy1.franken.de>
Source0:	http://www.duffy1.franken.de/rjakob/%{name}-%{version}.tar.bz2
# Source0-md5:	596dd464e8c86f32ef89654afca27719
Patch0:		%{name}-am_fix.patch
URL:		http://www.duffy1.franken.de/rjakob/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	qt-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
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
