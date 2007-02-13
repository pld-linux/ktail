Summary:	ktail - monitors files (like tail -f) and pipes
Summary(pl.UTF-8):	ktail - do monitorowania plików (jak tail -f) i rurek
Name:		ktail
Version:	0.6.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Vendor:		Rolf Jakob <rjakob@duffy1.franken.de>
Source0:	http://www.duffy1.franken.de/rjakob/%{name}-%{version}.tar.bz2
# Source0-md5:	596dd464e8c86f32ef89654afca27719
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-kde3.patch
URL:		http://www.duffy1.franken.de/rjakob/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 6:3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
ktail monitors multiple files and/or command output in one window.
Files and commands may be added and removed via drag'n'drop or menu
options.

%description -l pl.UTF-8
ktail monitoruje wiele plików lub wyjść z komend w jednym okienku.
Pliki i komendy mogą być dodawane i usuwane poprzez przesuń-i-upuść lub
z menu.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1

%build
#rm -f missing
#%{__aclocal}
#%{__autoconf}
#%{__automake}

kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktail
%{_applnkdir}/Utilities/ktail.desktop
%{_pixmapsdir}/*/*/apps/*.png
