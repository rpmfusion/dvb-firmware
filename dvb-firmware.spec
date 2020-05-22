%global commit0 3fef04a4a4bfeba88ae3b20aff9d3a1fabf1c159
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate0 20170329

Name:           dvb-firmware
Version:        %{commitdate0}
Release:        7.git%{shortcommit0}%{?dist}
Summary:        DVB firmwares

License:        Redistributable, no modification permitted
URL:            https://github.com/OpenELEC/dvb-firmware
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildArch:      noarch

BuildRequires:  linux-firmware

%description
DVB firmwares.


%prep
%autosetup -p1 -n dvb-firmware-%{commit0}


%build
# Nothing to build


%install
mkdir -p %{buildroot}/lib/firmware
# Verify that this package co-install with linux-firmware
for i in $(find firmware ! -type d) ; do
  if [ -e /lib/${i} ] ; then
    rm -f ${i}
    echo "Removing ${i}"
  fi
done

cp -pr firmware/* %{buildroot}/lib/firmware

# Remove empty directories
find %{buildroot}/lib/firmware/* -type d -delete

# Remove linux-firmware provided content
rm -rf %{buildroot}/lib/firmware/LICENCE.go7007

# Remove ivtv-firmware
for i in v4l-cx2341x-dec.fw v4l-cx2341x-enc.fw v4l-cx2341x-init.mpg v4l-pvrusb2-24xxx-01.fw v4l-pvrusb2-29xxx-01.fw ; do
  rm -f %{buildroot}/lib/firmware/${i}
done



%files
/lib/firmware/*


%changelog
* Fri May 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 20170329-7.git3fef04a
- Remove ivtv-firmware provided files

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170329-6.git3fef04a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170329-5.git3fef04a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170329-4.git3fef04a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170329-3.git3fef04a
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 20170329-2.git3fef04a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Nicolas Chauvet <kwizart@gmail.com> - 20170329-1.git3fef04a
- Initial spec file
