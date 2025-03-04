Summary:	Utility programs for Host AP driver for Intersil Prism2/2.5/3
Name:		hostap-utils
Epoch:		0
Version:	0.4.7
Release:	21
License:	GPLv2
Group:		System/Configuration/Networking
Url:		https://hostap.epitest.fi/
Source0:	http://hostap.epitest.fi/releases/hostap-utils-%{version}.tar.bz2
Source1:	hostap_cs.conf
Provides:	hostap

%description
This is a Linux driver for wireless LAN cards based on Intersil's Prism2/2.5/3
chipset. The driver supports a so called Host AP mode, i.e., it takes care of 
IEEE 802.11 management functions in the host computer and acts as an access
point. This does not require any special firmware for the wireless LAN card.
In addition to this, it has support for normal station operations in BSS and
possible also in IBSS. 

This packages contains binary utilities for use with hostap. 

%prep
%autosetup -p1

%build
%make_build CC="%{__cc}" CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_sysconfdir}/pcmcia
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pcmcia
install -m 755 hostap_crypt_conf %{buildroot}%{_sbindir}
install -m 755 hostap_diag %{buildroot}%{_sbindir}
install -m 755 hostap_fw_load %{buildroot}%{_sbindir}
install -m 755 hostap_io_debug %{buildroot}%{_sbindir}
install -m 755 hostap_rid %{buildroot}%{_sbindir}
install -m 755 prism2_param %{buildroot}%{_sbindir}
install -m 755 prism2_srec %{buildroot}%{_sbindir}
install -m 755 split_combined_hex %{buildroot}%{_sbindir}

%files
%doc COPYING ChangeLog README 
%config(noreplace) %{_sysconfdir}/pcmcia/hostap_cs.conf
%{_sbindir}/hostap_crypt_conf
%{_sbindir}/hostap_diag
%{_sbindir}/hostap_fw_load
%{_sbindir}/hostap_io_debug
%{_sbindir}/hostap_rid
%{_sbindir}/prism2_param
%{_sbindir}/prism2_srec
%{_sbindir}/split_combined_hex

