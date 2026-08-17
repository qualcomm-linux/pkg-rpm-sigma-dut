Name:           sigma-dut
Version:        latest
Release:        master%{?dist}
Summary:        WFA certification testing tool for QCA devices

License:        BSD-3-Clause
URL:            https://github.com/qualcomm/sigma-dut
# Source0's filename must match the entry in `sources`. On a cache miss the
# build downloads this URL, so keep it pointing at a fetchable upstream tarball.
# %{name} and %{version} are expanded, so bumping Version: is usually all you need.
Source0:        https://github.com/qualcomm/sigma-dut/archive/refs/heads/master.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
sigma-dut is the WFA Sigma DUT/CA tool used for Wi-Fi certification
testing on Qualcomm/Atheros devices.  It implements the WFA control
agent protocol and supports 802.11a/b/g/n/ac/ax, P2P, NAN, and
related certification test cases.

%prep
%autosetup

%build
%make_build


%install
%make_install BINDIR=%{_sbindir}

%files
%doc README CONTRIBUTIONS
%license README
%{_sbindir}/sigma_dut

%changelog
* Mon Jun 29 2026 geyi <geyi@qti.qualcomm.com> - 1.11-1
- Initial RPM packaging for sigma-dut.
