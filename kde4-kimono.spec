%define		_state		stable
%define		orgname		kimono

Summary:	K Desktop Environment - C# Mono KDE4 bindings
Summary(pl_PL.UTF8):	K Desktop Environment - Dowiązania C# Mono
Name:		kimono
Version:	4.7.1
Release:	0.1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	673e41be49c6277f832450fa2ba5c698
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
Obsoletes:	kde4-kdebindings-kimono < 4.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C# Mono KDE4 bindings.

%description -l pl.UTF-8
Dowiązania C# Mono do KDE4.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pykimono.py
%attr(755,root,root) %{_libdir}/kde4/kimonopart.so
%attr(755,root,root) %{_bindir}/kimono
%{_desktopdir}/kde4/kimono.desktop
%{_datadir}/kde4/services/kimono_part.desktop
%{_datadir}/apps/kimono
%{_iconsdir}/hicolor/*x*/apps/kimono.png
%{_iconsdir}/hicolor/scalable/apps/kimono.svgz
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-kimono.png
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-kimono.svgz
%{_mandir}/man1/kimono.1*
