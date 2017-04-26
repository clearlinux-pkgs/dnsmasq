#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x28FC869A289B82B7 (simon@thekelleys.org.uk)
#
Name     : dnsmasq
Version  : 2.76
Release  : 30
URL      : http://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.76.tar.xz
Source0  : http://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.76.tar.xz
Source1  : dnsmasq.service
Source99 : http://www.thekelleys.org.uk/dnsmasq/dnsmasq-2.76.tar.xz.asc
Summary  : A lightweight caching nameserver
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: dnsmasq-bin
Requires: dnsmasq-config
Requires: dnsmasq-data
Requires: dnsmasq-doc
Patch1: stateless.patch
Patch2: cve-2015-3294.nopatch
Patch3: noping.patch
Patch4: nov6.patch
Patch5: build.patch

%description
Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server. It 
is designed to provide DNS and, optionally, DHCP, to a small network. It can
serve the names of local machines which are not in the global DNS. The DHCP 
server integrates with the DNS server and allows machines with DHCP-allocated
addresses to appear in the DNS with names configured either in each host or 
in a central configuration file. Dnsmasq supports static and dynamic DHCP 
leases and BOOTP for network booting of diskless machines.

%package bin
Summary: bin components for the dnsmasq package.
Group: Binaries
Requires: dnsmasq-data
Requires: dnsmasq-config

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


%package doc
Summary: doc components for the dnsmasq package.
Group: Documentation

%description doc
doc components for the dnsmasq package.


%prep
%setup -q -n dnsmasq-2.76
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493169879
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1493169879
rm -rf %{buildroot}
%make_install PREFIX=%{_prefix}
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/dnsmasq.service
## make_install_append content
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_libdir}/systemd/system/
install -D dnsmasq.conf.example %{buildroot}%{_datadir}/defaults/dnsmasq/dnsmasq.conf
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dnsmasq

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/dnsmasq.service

%files data
%defattr(-,root,root,-)
/usr/share/defaults/dnsmasq/dnsmasq.conf

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*
