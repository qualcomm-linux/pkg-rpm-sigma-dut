%global commit a7859766c2bc60bcbc5d6271617141e6853fea8a

Name:           sigma-dut
Version:        %{commit}
Release:        1%{?dist}
Summary:        WFA certification testing tool for QCA devices

License:        BSD-3-Clause-Clear
URL:            https://github.com/qualcomm/sigma-dut
Source0:        https://github.com/qualcomm/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  pkgconfig(libnl-3.0)

%description
sigma-dut is the WFA Sigma DUT/CA tool used for Wi-Fi certification
testing on Qualcomm/Atheros devices.  It implements the WFA control
agent protocol and supports 802.11a/b/g/n/ac/ax, P2P, NAN, and
related certification test cases.

%prep
%autosetup -n %{name}-%{commit}

%build
%make_build

%install
%make_install BINDIR=%{_sbindir}

%files
%doc README CONTRIBUTIONS
%license README
%{_sbindir}/sigma_dut

%changelog
* Wed Aug 19 2026 Yu Zhang <yu.zhang@oss.qualcomm.com> - a7859766c2bc60bcbc5d6271617141e6853fea8a-1
- Build from fixed upstream commit a7859766c2bc60bcbc5d6271617141e6853fea8a
