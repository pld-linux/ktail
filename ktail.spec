Summary:	ktail - monitors files (like tail -f) and pipes
Name:		ktail
Version:	0.4.3
Release:	1
Group:		X11/KDE/Utilities
######		Unknown group!
License:	GPL
Vendor:		Rolf Jakob <rjakob@duffy1.franken.de>
Source0:	%{name}-%{version}.tar.gz
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
%{_datadir}/doc/HTML/en/ktail/index.html
%{_datadir}/icons/ktail.xpm
%{_datadir}/icons/mini/ktail.xpm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/ktail.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/ktail.mo
