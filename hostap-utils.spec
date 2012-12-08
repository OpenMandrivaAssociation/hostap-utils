Summary:	Utility programs for Host AP driver for Intersil Prism2/2.5/3
Name:		hostap-utils
Version:	0.4.7
Release:	%mkrel 10
License:	GPL
Group:		System/Configuration/Networking
URL:		http://hostap.epitest.fi/
Source0:	http://hostap.epitest.fi/releases/hostap-utils-%{version}.tar.bz2
Source1:	hostap_cs.conf
Requires:	wireless-tools
Provides:	hostap
Obsoletes:	hostap
Epoch:		0
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This is a Linux driver for wireless LAN cards based on Intersil's Prism2/2.5/3
chipset. The driver supports a so called Host AP mode, i.e., it takes care of 
IEEE 802.11 management functions in the host computer and acts as an access
point. This does not require any special firmware for the wireless LAN card.
In addition to this, it has support for normal station operations in BSS and
possible also in IBSS. 

This packages contains binary utilities for use with hostap. 

%prep

%setup -q -n %{name}-%{version}

%build
%make CC="%{__cc}" CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0:0.4.7-8mdv2011.0
+ Revision: 665415
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.4.7-7mdv2011.0
+ Revision: 605859
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.4.7-6mdv2010.1
+ Revision: 522847
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0:0.4.7-5mdv2010.0
+ Revision: 425148
- rebuild

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 0:0.4.7-4mdv2009.1
+ Revision: 317986
- use %%ldflags

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0:0.4.7-3mdv2009.0
+ Revision: 221213
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0:0.4.7-2mdv2008.1
+ Revision: 126728
- kill re-definition of %%buildroot on Pixel's request


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.4.7-2mdv2007.1
+ Revision: 145535
- Import hostap-utils

* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0:0.4.7-2mdv2007.1
- use the %%mrel macro

* Sun Jan 08 2006 Pascal Terjan <pterjan@mandriva.org> 0:0.4.7-1mdk
- 0.4.7

* Sun Sep 25 2005 David Walluck <walluck@mandriva.org> 0:0.4.0-1mdk
- 0.4.0
- mark hostap_cs.conf as %%config
- fix CC and CFLAGS

* Wed Mar 09 2005 Laurent Culioli <laurent@mandrake.org> 0.3.7-1mdk
- 0.3.7

* Wed Aug 11 2004 Laurent Culioli <laurent@mandrake.org> 0.2.4-1mdk
- 0.2.4
- provides/obsoletes hostap
- split hostap in 2 packages ( hostap-utils & hostapd )

