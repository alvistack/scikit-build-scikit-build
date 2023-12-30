# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-scikit-build
Epoch: 100
Version: 0.17.6
Release: 1%{?dist}
BuildArch: noarch
Summary: Improved build system generator for Python C/C++/Fortran/Cython extensions
License: MIT
URL: https://github.com/scikit-build/scikit-build/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools >= 42.0.0

%description
scikit-build is an improved build system generator for CPython
C/C++/Fortran/Cython extensions. It provides better support for
additional compilers, build systems, cross compilation, and locating
dependencies and their associated build requirements.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-scikit-build
Summary: Improved build system generator for Python C/C++/Fortran/Cython extensions
Requires: cmake
Requires: ninja-build
Requires: python3
Requires: python3-distro
Requires: python3-packaging
Requires: python3-setuptools >= 42.0.0
Requires: python3-tomli
Requires: python3-typing-extensions >= 3.7
Requires: python3-wheel >= 0.32.0
Provides: python3-scikit-build = %{epoch}:%{version}-%{release}
Provides: python3dist(scikit-build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-scikit-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(scikit-build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-scikit-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(scikit-build) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-scikit-build
scikit-build is an improved build system generator for CPython
C/C++/Fortran/Cython extensions. It provides better support for
additional compilers, build systems, cross compilation, and locating
dependencies and their associated build requirements.

%files -n python%{python3_version_nodots}-scikit-build
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-scikit-build
Summary: Improved build system generator for Python C/C++/Fortran/Cython extensions
Requires: cmake
Requires: ninja-build
Requires: python3
Requires: python3-distro
Requires: python3-packaging
Requires: python3-setuptools >= 42.0.0
Requires: python3-tomli
Requires: python3-typing-extensions >= 3.7
Requires: python3-wheel >= 0.32.0
Provides: python3-scikit-build = %{epoch}:%{version}-%{release}
Provides: python3dist(scikit-build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-scikit-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(scikit-build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-scikit-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(scikit-build) = %{epoch}:%{version}-%{release}

%description -n python3-scikit-build
scikit-build is an improved build system generator for CPython
C/C++/Fortran/Cython extensions. It provides better support for
additional compilers, build systems, cross compilation, and locating
dependencies and their associated build requirements.

%files -n python3-scikit-build
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-scikit-build
Summary: Improved build system generator for Python C/C++/Fortran/Cython extensions
Requires: cmake
Requires: ninja-build
Requires: python3
Requires: python3-distro
Requires: python3-packaging
Requires: python3-setuptools >= 42.0.0
Requires: python3-tomli
Requires: python3-typing-extensions >= 3.7
Requires: python3-wheel >= 0.32.0
Provides: python3-scikit-build = %{epoch}:%{version}-%{release}
Provides: python3dist(scikit-build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-scikit-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(scikit-build) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-scikit-build = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(scikit-build) = %{epoch}:%{version}-%{release}

%description -n python3-scikit-build
scikit-build is an improved build system generator for CPython
C/C++/Fortran/Cython extensions. It provides better support for
additional compilers, build systems, cross compilation, and locating
dependencies and their associated build requirements.

%files -n python3-scikit-build
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
