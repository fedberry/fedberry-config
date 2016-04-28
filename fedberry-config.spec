%define bname   fedberry
%define name    %{bname}-config

Name:       %{name}
Version:    0.2.2
Release:    2%{?dist}
License:    GPLv3+
Summary:    Easy configuration of various system options in FedBerry
Group:      Applications/System
URL:        https://github.com/fedberry/fedberry-config
Source0:    https://raw.githubusercontent.com/%{bname}/%{name}/master/%{name}
Source1:    https://raw.githubusercontent.com/%{bname}/%{name}/master/LICENSE
Source2:    https://raw.githubusercontent.com/%{bname}/%{name}/master/README.md
Source3:    https://raw.githubusercontent.com/%{bname}/%{name}/master/rootfs-grow.service
BuildArch:  noarch
Obsoletes:  rootfs-resize
Conflicts:  rootfs-resize
BuildRequires: discount >= 2.1
BuildRequires: systemd
Requires: pv
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%description
A utility for making common Raspberry Pi configuration changes via a simple menu-driven interface.
The majority of the configuration changes result in automated modifications to /boot/config.txt
and/or other standard Fedora configuration files. Many options will require a reboot to take effect.


%prep
%setup -c -T
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .


%build
for MD_FILE in *.md; do
  markdown -o ${MD_FILE%.*}.html ${MD_FILE}
done


%install
rm -rf %{buildroot}

%{__install} -d %{buildroot}/%{_sbindir}
%{__install} -p %{name} %{buildroot}/%{_sbindir}

%{__install} -d %{buildroot}/%{_unitdir}
%{__install} -p rootfs-grow.service %{buildroot}/%{_unitdir}


%clean
rm -rf %{buildroot}


%post
%systemd_post rootfs-grow.service


%preun
%systemd_preun rootfs-grow.service


%postun
%systemd_postun rootfs-grow.service


%files
%doc README.md
%doc README.html
%license LICENSE
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0644,root,root) %{_unitdir}/rootfs-grow.service


%changelog
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
