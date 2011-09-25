%define		_state		stable
%define		orgname		kimono

Summary:	K Desktop Environment - C# Mono KDE4 bindings
Summary(pl_PL.UTF8):	K Desktop Environment - Dowiązania C# Mono
Name:		kimono
Version:	4.7.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	673e41be49c6277f832450fa2ba5c698
URL:		http://www.kde.org/
BuildRequires:	akonadi-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	mono-csharp
BuildRequires:	qyoto-devel >= %{version}
BuildRequires:	soprano-devel
Requires:	qyoto >= %{version}
Obsoletes:	kde4-kdebindings-kimono < 4.6.100
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

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kimonopluginfactory.so
%attr(755,root,root) %{_libdir}/libakonadi-sharp.so
%attr(755,root,root) %{_libdir}/libkhtml-sharp.so
%attr(755,root,root) %{_libdir}/libkimono.so
%attr(755,root,root) %{_libdir}/libktexteditor-sharp.so
%attr(755,root,root) %{_libdir}/libnepomuk-sharp.so
%attr(755,root,root) %{_libdir}/libplasma-sharp.so
%attr(755,root,root) %{_libdir}/libsoprano-sharp.so
%{_prefix}/lib/mono/gac/akonadi
%{_prefix}/lib/mono/gac/kde-dotnet
%{_prefix}/lib/mono/gac/khtml-dll
%{_prefix}/lib/mono/gac/ktexteditor-dotnet
%{_prefix}/lib/mono/gac/nepomuk-dll
%{_prefix}/lib/mono/gac/plasma-dll
%{_prefix}/lib/mono/gac/soprano
%{_prefix}/lib/mono/qyoto/akonadi.dll
%{_prefix}/lib/mono/qyoto/kde-dotnet.dll
%{_prefix}/lib/mono/qyoto/khtml-dll.dll
%{_prefix}/lib/mono/qyoto/ktexteditor-dotnet.dll
%{_prefix}/lib/mono/qyoto/nepomuk-dll.dll
%{_prefix}/lib/mono/qyoto/plasma-dll.dll
%{_prefix}/lib/mono/qyoto/soprano.dll

%{_datadir}/apps/plasma_scriptengine_kimono
%{_datadir}/kde4/services/plasma-scriptengine-kimono-applet.desktop
%{_datadir}/kde4/services/plasma-scriptengine-kimono-dataengine.desktop