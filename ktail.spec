%define name ktail
%define version 0.4.3
%define release 1
%define prefix /opt/kde

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: ktail - monitors files (like tail -f) and pipes
Name: %{name}
Version: %{version}
Release: %{release}
Group: X11/KDE/Utilities
Copyright: GPL
Vendor: Rolf Jakob <rjakob@duffy1.franken.de>
Packager: Troy Engel <tengel@sonic.net>
Source: %{name}-%{version}.tar.gz
URL: http://www.franken.de/users/duffy1/rjakob
Requires: qt >= 1.30 kdelibs
BuildRoot: /tmp/build-%{name}-%{version}

%description
ktail monitors multiple files and/or command output in one window.
Files and commands may be added and removed via drag'n'drop or menu
options.

%prep
%setup

%build
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{prefix} --with-install-root=$RPM_BUILD_ROOT
make

%install
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%defattr(-,root,root)
%{prefix}/bin/ktail
%{prefix}/share/applnk/Utilities/ktail.kdelnk
%{prefix}/share/doc/HTML/en/ktail/index.html
%{prefix}/share/icons/ktail.xpm
%{prefix}/share/icons/mini/ktail.xpm
%{prefix}/share/locale/de/LC_MESSAGES/ktail.mo
%{prefix}/share/locale/fr/LC_MESSAGES/ktail.mo
