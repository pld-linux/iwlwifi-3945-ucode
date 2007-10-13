Summary:	Microcode image for Intel(R) PRO/Wireless 2200 Driver
%define	_module	3945
Name:		iwlwifi-%{_module}-ucode
Version:	2.14.1.5
Release:	1
License:	distributable
Group:		System Environment/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
# Source0-md5:	a8122d3e026561055f488dc654ccfcd1
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Microcode Image for 

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install iwlwifi-%{_module}-1.ucode $RPM_BUILD_ROOT/lib/firmware
install LICENSE.%{name} $RPM_BUILD_ROOT/lib/firmware/%{name}-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.%{name}
/lib/firmware/%{name}-LICENSE
/lib/firmware/*.ucode
