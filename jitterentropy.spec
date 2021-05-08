Summary:	Library implementing the jitter entropy source
Summary(pl.UTF-8):	Biblioteka implementująca źródło entropii jitter
Name:		jitterentropy
Version:	3.0.2
Release:	1
License:	BSD or GPL v2+
Group:		Libraries
Source0:	http://www.chronox.de/jent/%{name}-library-%{version}.tar.xz
# Source0-md5:	f09160fa89953444bdb73a071abf8484
URL:		http://www.chronox.de/jent.html
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Jitter RNG provides a noise source using the CPU execution timing
jitter. It does not depend on any system resource other than a
high-resolution time stamp. It is a small-scale, yet fast entropy
source that is viable in almost all environments and on a lot of CPU
architectures.

%description -l pl.UTF-8
Jitter RNG zapewnia źródło szumu wykorzystujące fluktuacje czasu
wykonywania kodu przez CPU. Nie zależy od żadnego zasobu systemowego
innego niż znacznik czasu wysokiej rozdzielczości. Jest to źródło
entropii małej skali, ale szybkie, opłacalne w prawie każdym
środowisku, przy wielu architekturach CPU.

%package devel
Summary:	Header files for jitterentropy library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki jitterentropy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for jitterentropy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki jitterentropy.

%package static
Summary:	Static jitterentropy library
Summary(pl.UTF-8):	Statyczna biblioteka jitterentropy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static jitterentropy library.

%description static -l pl.UTF-8
Statyczna biblioteka jitterentropy.

%prep
%setup -q -n %{name}-library-%{version}

%build
# NOTE: jitterentropy-base.c must be compiled with optimizations disabled
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -fPIC -O0 -fwrapv -Wall -Wextra" \
	LIBRARIES="rt pthread"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-static \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_lib}" \
	INSTALL_STRIP=install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES.md COPYING COPYING.bsd README.md
%attr(755,root,root) %{_libdir}/libjitterentropy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjitterentropy.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjitterentropy.so
%{_includedir}/jitterentropy.h
%{_includedir}/jitterentropy-base-user.h
%{_mandir}/man3/jitterentropy.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libjitterentropy.a
