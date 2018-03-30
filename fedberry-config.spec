%define bname   fedberry
%define name    %{bname}-config

Name:       %{name}
Version:    0.4.2
Release:    1%{?dist}
License:    GPLv3+
Summary:    Easy configuration of various system options in FedBerry
Group:      Applications/System
URL:        https://github.com/fedberry/fedberry-config
Source0:    https://raw.githubusercontent.com/%{bname}/%{name}/master/%{name}
Source1:    https://raw.githubusercontent.com/%{bname}/%{name}/master/LICENSE
Source2:    https://raw.githubusercontent.com/%{bname}/%{name}/master/README.md
Source3:    https://raw.githubusercontent.com/%{bname}/%{name}/master/rootfs-grow.service
Source4:    https://raw.githubusercontent.com/%{bname}/%{name}/master/%{name}.desktop
Source5:    https://raw.githubusercontent.com/%{bname}/%{name}/master/%{name}.svg
Source6:    https://raw.githubusercontent.com/%{bname}/%{name}/master/pi3_disable_pwr_led.service
BuildArch:  noarch
Obsoletes:  rootfs-resize
Conflicts:  rootfs-resize
BuildRequires: discount >= 2.1
BuildRequires: systemd
Requires: newt
Requires: pv
Requires: raspberrypi-vc-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
A utility for making common Raspberry Pi configuration changes via a simple menu-driven interface.
The majority of the configuration changes result in automated modifications to /boot/config.txt
and/or other standard Fedora configuration files. Many options will require a reboot to take effect.


%prep
%setup -c -T
cp -a %{sources} .


%build
for MD_FILE in *.md; do
  markdown -o ${MD_FILE%.*}.html ${MD_FILE}
done


%install
rm -rf %{buildroot}

%{__install} -d %{buildroot}/%{_sbindir}
%{__install} -p %{name} %{buildroot}/%{_sbindir}

%{__install} -d %{buildroot}/%{_unitdir}
%{__install} -p *.service %{buildroot}/%{_unitdir}

%{__install} -d %{buildroot}/%{_datadir}/applications
%{__install} -p %{name}.desktop %{buildroot}/%{_datadir}/applications

%{__install} -d %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
%{__install} -p %{name}.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps



%clean
rm -rf %{buildroot}


%post
%systemd_post rootfs-grow.service
%systemd_post pi3_disable_pwr_led.service


%preun
%systemd_preun rootfs-grow.service
%systemd_preun pi3_disable_pwr_led.service


%postun
%systemd_postun rootfs-grow.service
%systemd_postun pi3_disable_pwr_led.service


%files
%doc README.md README.html
%license LICENSE
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0644,root,root) %{_unitdir}/*.service
%attr(0755,root,root) %{_datadir}/applications/%{name}.desktop
%attr(0755,root,root) %{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sat Dec 16 2017 Vaughan <vaughan at agrez dot net> 0.4.2-1
- New release

* Fri Dec 01 2017 Vaughan <vaughan at agrez dot net> 0.4.1-1
- New release

* Sun Jul 23 2017 Vaughan <vaughan at agrez dot net> 0.4.0-1
- New release

* Tue May 02 2017 Vaughan <vaughan at agrez dot net> 0.3.11-1
- New release
- Add custom icon

* Sun Apr 30 2017 Vaughan <vaughan at agrez dot net> 0.3.10-2
- Update desktop file

* Fri Apr 28 2017 Vaughan <vaughan at agrez dot net> 0.3.10-1
- New release
- Add desktop file

* Fri Mar 17 2017 Vaughan <vaughan at agrez dot net> 0.3.9-1
- New release

* Wed Feb 15 2017 Vaughan <vaughan at agrez dot net> 0.3.8-1
- New release

* Sat Jan 07 2017 Vaughan <vaughan at agrez dot net> 0.3.7-1
- New release
- Simplify %%prep

* Mon Nov 07 2016 Vaughan <vaughan at agrez dot net> 0.3.6-1
- New release

* Tue Oct 11 2016 Vaughan <vaughan at agrez dot net> 0.3.5-1
- New release

* Sat Oct 01 2016 Vaughan <vaughan at agrez dot net> 0.3.3-2
- Ensure rootfs-grow.service executes before initial-setup.service

* Mon Sep 26 2016 Vaughan <vaughan at agrez dot net> 0.3.3-1
- New release

* Mon Aug 22 2016 Vaughan <vaughan at agrez dot net> 0.3.2-1
- New release

* Mon May 30 2016 Vaughan <vaughan at agrez dot net> 0.3.1-1
- New release

* Wed May 11 2016 Vaughan <vaughan at agrez dot net> 0.3.0-1
- New release

* Thu Apr 28 2016 Vaughan <vaughan at agrez dot net> 0.2.2-2
- Add %%postun macro 
- Fix build with mock

* Wed Apr 27 2016 Vaughan <vaughan at agrez dot net> 0.2.2-1
- New release
- Requires 'pv'

* Sat Mar 12 2016 Vaughan <vaughan at agrez dot net> 0.2.1-1
- New release

* Sun Mar 06 2016 mrjoshuap <jpreston at redhat dot com> 0.2-2
- fix URL for package
- autogenerate html documentation from md files

* Sun Mar 06 2016 Vaughan <vaughan at agrez dot net> 0.2-1
- Initial package
