#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
# Source0 file verified with key 0x15CDDA6AE19135A2 (srk@debian.org)
#
Name     : dnsmasq
Version  : 2.89
Release  : 68
URL      : https://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.89.tar.xz
Source0  : https://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.89.tar.xz
Source1  : dnsmasq.service
Source2  : dnsmasq.sysusers
Source3  : https://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.89.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: dnsmasq-bin = %{version}-%{release}
Requires: dnsmasq-config = %{version}-%{release}
Requires: dnsmasq-data = %{version}-%{release}
Requires: dnsmasq-license = %{version}-%{release}
Requires: dnsmasq-locales = %{version}-%{release}
Requires: dnsmasq-man = %{version}-%{release}
Requires: dnsmasq-services = %{version}-%{release}
BuildRequires : buildreq-nginx
BuildRequires : gmp-dev
BuildRequires : gnupg
BuildRequires : nettle-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(hogweed)
BuildRequires : pkgconfig(libidn2)
BuildRequires : pkgconfig(libnetfilter_conntrack)
BuildRequires : pkgconfig(nettle)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: stateless.patch
Patch2: build.patch
Patch3: contrib.patch
Patch4: options.patch
Patch5: 0001-Store-leases-in-var-lib-dnsmasq.patch

%description
Dnsmasq logo, contributed by Justin Clift.
The source format is Inkscape SVG vector format, which is scalable and
easy to export to other formats. For convenience I've included a 56x31
png export and a 16x16 ico suitable for use as a web favicon.

%package bin
Summary: bin components for the dnsmasq package.
Group: Binaries
Requires: dnsmasq-data = %{version}-%{release}
Requires: dnsmasq-config = %{version}-%{release}
Requires: dnsmasq-license = %{version}-%{release}
Requires: dnsmasq-services = %{version}-%{release}

%description bin
bin components for the dnsmasq package.


%package config
Summary: config components for the dnsmasq package.
Group: Default

%description config
config components for the dnsmasq package.


%package data
Summary: data components for the dnsmasq package.
Group: Data

%description data
data components for the dnsmasq package.


%package license
Summary: license components for the dnsmasq package.
Group: Default

%description license
license components for the dnsmasq package.


%package locales
Summary: locales components for the dnsmasq package.
Group: Default

%description locales
locales components for the dnsmasq package.


%package man
Summary: man components for the dnsmasq package.
Group: Default

%description man
man components for the dnsmasq package.


%package services
Summary: services components for the dnsmasq package.
Group: Systemd services
Requires: systemd

%description services
services components for the dnsmasq package.


%prep
%setup -q -n dnsmasq-2.89
cd %{_builddir}/dnsmasq-2.89
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683232140
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}  all-i18n


%install
export SOURCE_DATE_EPOCH=1683232140
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dnsmasq
cp %{_builddir}/dnsmasq-%{version}/COPYING %{buildroot}/usr/share/package-licenses/dnsmasq/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/dnsmasq-%{version}/COPYING-v3 %{buildroot}/usr/share/package-licenses/dnsmasq/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
%make_install PREFIX=%{_prefix} install-i18n
%find_lang dnsmasq
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/dnsmasq.service
mkdir -p %{buildroot}/usr/lib/sysusers.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/sysusers.d/dnsmasq.conf
## install_append content
install -d %{buildroot}/usr/bin
install -d %{buildroot}/usr/share/man/man1
install -d %{buildroot}/usr/lib/systemd/system/
install -D dnsmasq.conf.example %{buildroot}/usr/share/defaults/dnsmasq/dnsmasq.conf
pushd contrib/lease-tools
%make_install
popd
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dhcp_lease_time
/usr/bin/dhcp_release
/usr/bin/dhcp_release6
/usr/bin/dnsmasq

%files config
%defattr(-,root,root,-)
/usr/lib/sysusers.d/dnsmasq.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/dnsmasq/dnsmasq.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dnsmasq/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/dnsmasq/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/es/man8/dnsmasq.8
/usr/share/man/fr/man8/dnsmasq.8
/usr/share/man/man8/dnsmasq.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/dnsmasq.service

%files locales -f dnsmasq.lang
%defattr(-,root,root,-)

