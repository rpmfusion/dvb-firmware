%global commit0 3fef04a4a4bfeba88ae3b20aff9d3a1fabf1c159
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate0 20170329

Name:           dvb-firmware
Version:        %{commitdate0}
Release:        1.git%{shortcommit0}%{?dist}
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



%files
/lib/firmware/*


%changelog
* Fri Mar 16 2018 Nicolas Chauvet <kwizart@gmail.com> - 20170329-1.git3fef04a
- Initial spec file
