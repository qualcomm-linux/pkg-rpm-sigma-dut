# Example RPM spec file.
#
# Rename this to <your-component>.spec and edit the fields below:
#
#   git mv mypackage.spec.example mycomponent.spec
#
# The workflows expect exactly ONE *.spec at the repo root, which is why this
# ships with a .example suffix — it stays invisible to the build until renamed.
#
Name:           sigma-dut
Version:        1.11
Release:        1%{?dist}
Summary:        rpm pakcage for sigma-dut

License:        BSD-3-Clause
URL:            https://github.com/qualcomm/sigma-dut
# Source0's filename must match the entry in `sources`. On a cache miss the
# build downloads this URL, so keep it pointing at a fetchable upstream tarball.
# %{name} and %{version} are expanded, so bumping Version: is usually all you need.
Source0:        https://github.com/qualcomm/sigma-dut/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
A longer description of the package.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/mypackage

%changelog
* Mon Jun 29 2026 Maintainer <maintainer@example.com> - 1.0-1
- Initial package
