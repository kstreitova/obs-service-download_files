#
# spec file for package test
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           Test-Simple
Version:	1.001014
Release:	0.0
License:
Summary:
Url:
Group:
Source:		http://localhost:8080/data/%{name}-%{version}.tar.bz2
Patch:    http://localhost:8080/data/patch1.diff
Patch1:    http://localhost:8080/data/patch2.diff
BuildRequires:
PreReq:
Provides:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING


