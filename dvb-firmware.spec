%global commit0 3c1910ba4cd0c3e241796ec6025d1b8e882a892f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate0 20230604

Name:           dvb-firmware
Version:        %{commitdate0}
Release:        9.git%{shortcommit0}%{?dist}
Summary:        DVB firmware nonfree

License:        Redistributable, no modification permitted
URL:            https://github.com/LibreELEC/dvb-firmware
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildArch:      noarch

BuildRequires:  dvb-firmware

%description
DVB firmware nonfree.

%package nonfree
Summary: DVB firmware nonfree

%description nonfree


%prep
%autosetup -p1 -n dvb-firmware-%{commit0}


%build
# Nothing to build


%install
# Remove linux-firmware provided content
rm -rf firmware/go7007

# Remove ivtv-firmware
for i in v4l-cx2341x-dec.fw v4l-cx2341x-enc.fw v4l-cx2341x-init.mpg v4l-pvrusb2-24xxx-01.fw v4l-pvrusb2-29xxx-01.fw ; do
  rm -f firmware/${i}
done

mkdir -p %{buildroot}/lib/firmware
# Verify that this package co-install with linux-firmware
for i in $(find firmware ! -type d) ; do
  if [ -e /lib/${i}.xz ] ; then
    rm -f ${i}.xz
    echo "Removing ${i}.xz"
  elif [ -e /lib/${i} ] ; then
    rm -f ${i}
    echo "Removing ${i}"
  fi
done

cp -pr firmware/* %{buildroot}/lib/firmware

# Remove empty directories
find %{buildroot}/lib/firmware/* -empty -type d -delete


%files nonfree
/lib/firmware/*


%changelog
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20230604-9.git3c1910b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20230604-8.git3c1910b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 17 2023 Nicolas Chauvet <kwizart@gmail.com> - 20230604-7.git3c1910b
- Drop compression and fix duplicates - rfbz#6736

* Sat Aug 05 2023 Nicolas Chauvet <kwizart@gmail.com> - 20230604-6.git3c1910b
- Update snapshot
- Fix duplication and xz compress - rfbz#6736

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20210719-5.git0eaf5b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Nicolas Chauvet <kwizart@gmail.com> - 20210719-4.git0eaf5b3
- Switch to nonfree sub-package

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20210719-2.git0eaf5b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Feb 28 2022 Sérgio Basto <sergio@serjux.com> - 20210719-1.git0eaf5b3
- Update and fix the build

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 20200922-12.git6c61d12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20200922-11.git6c61d12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 07 2021 Nicolas Chauvet <kwizart@gmail.com> - 20200922-10.git6c61d12
- Switch to LibreELEC

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170329-9.git3fef04a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20170329-8.git3fef04a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

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
