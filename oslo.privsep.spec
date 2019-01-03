#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.privsep
Version  : 1.31.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/b6/d5/daef2e4775a41a7b969f32673784d4e317312faad86149a5e9b56a3d0dd0/oslo.privsep-1.31.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b6/d5/daef2e4775a41a7b969f32673784d4e317312faad86149a5e9b56a3d0dd0/oslo.privsep-1.31.0.tar.gz
Summary  : OpenStack library for privilege separation
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.privsep-bin = %{version}-%{release}
Requires: oslo.privsep-license = %{version}-%{release}
Requires: oslo.privsep-python = %{version}-%{release}
Requires: oslo.privsep-python3 = %{version}-%{release}
Requires: cffi
Requires: enum34
Requires: eventlet
Requires: futures
Requires: greenlet
Requires: msgpack
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
BuildRequires : buildreq-distutils3
BuildRequires : hacking
BuildRequires : oslo.config
BuildRequires : oslo.log
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : python-dateutil

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/oslo.privsep.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the oslo.privsep package.
Group: Binaries
Requires: oslo.privsep-license = %{version}-%{release}

%description bin
bin components for the oslo.privsep package.


%package license
Summary: license components for the oslo.privsep package.
Group: Default

%description license
license components for the oslo.privsep package.


%package python
Summary: python components for the oslo.privsep package.
Group: Default
Requires: oslo.privsep-python3 = %{version}-%{release}

%description python
python components for the oslo.privsep package.


%package python3
Summary: python3 components for the oslo.privsep package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.privsep package.


%prep
%setup -q -n oslo.privsep-1.31.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546552412
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.privsep
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.privsep/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/privsep-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.privsep/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
