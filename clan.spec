Summary:	Clan - a Polyhedral Representation Extraction Tool for C-Based High Level Languages
Summary(pl.UTF-8):	Clan - narzędzie do tworzenia reprezentacji wielościanowej dla języków opartych na C
Name:		clan
Version:	0.8.1
Release:	2
License:	LGPL v3+
Group:		Libraries
##Source0Download: http://icps.u-strasbg.fr/people/bastoul/public_html/development/clan/
#Source0:	http://icps.u-strasbg.fr/people/bastoul/public_html/development/clan/docs/%{name}-%{version}.tar.gz
#Source0Download: https://github.com/periscop/clan/releases
Source0:	https://github.com/periscop/clan/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bffd26cc8b1360e47245ef71cea78aa3
Patch0:		%{name}-info.patch
URL:		http://icps.u-strasbg.fr/people/bastoul/public_html/development/clan/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison >= 2.4
BuildRequires:	doxygen
BuildRequires:	flex >= 2.5.35
BuildRequires:	libtool
BuildRequires:	osl-devel >= 0.9.0
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clan is a free software and library which translates some particular
parts of high level programs written in C, C++, C# or Java into a
polyhedral representation called OpenScop. This representation may be
manipulated by other tools to, e.g., achieve complex analyses or
program restructurations (for optimization, parallelization or any
other kind of manipulation). It has been created to avoid tedious and
error-prone input file writing for polyhedral tools (such as CLooG,
LeTSeE, Clan etc.). Using Clan, the user has to deal with source
codes based on C grammar only (as C, C++, C# or Java).

%description -l pl.UTF-8
Clan to wolnodostępne oprogramowanie i biblioteka tłumacząca wybrane
części programów napisanych w językach wysokiego poziomu, takich jak
C, C++, C# lub Java na reprezentację wielościanową o nazwie OpenScop.
Reprezentacja ta może być przetwarzana przez inne narzędzia w celu np.
złożonych analiz lub restrukturyzacji programu (optymalizacji,
zrównoleglenia i innych). Powstało, aby zapobiec nudnemu i
błędogennemu tworzeniu plików wejściowych dla narzędzi wielościanowych
(takich jak CLooG, LeTSeE, Clan itp.). Przy użyciu narzędzia Clan
można obsłużyć tylko kody źródłowe oparte na gramatyce C (takie jak C,
C++, C# lub Java).

%package devel
Summary:	Header files for Clan library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Clan
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	osl-devel >= 0.9.0

%description devel
Header files for Clan library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Clan.

%package static
Summary:	Static Clan library
Summary(pl.UTF-8):	Statyczna biblioteka Clan
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Clan library.

%description static -l pl.UTF-8
Statyczna biblioteka Clan.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-osl=system

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_bindir}/clan
%attr(755,root,root) %{_libdir}/libclan.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclan.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclan.so
%{_libdir}/libclan.la
%dir %{_libdir}/clan
%{_libdir}/clan/clan-config.cmake
%{_includedir}/clan
%{_infodir}/clan.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libclan.a
