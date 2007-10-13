Summary:	Microcode image for Intel PRO/Wireless 3945ABG/BG Network Connection Adapter
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
The file iwlwifi-3945.ucode provided in this package is required to be
present on your system in order for the Intel PRO/Wireless 3945ABG/BG Network
Connection Adapter driver for Linux (iwlwifi-3945) to be able to operate
on your system.

On adapter initialization, and at varying times during the uptime of
the adapter, the microcode is loaded into the RAM on the network
adapter.  The microcode provides the low level MAC features including
radio control and high precision timing events (backoff, transmit,
etc.) while also providing varying levels of packet filtering which can
be used to keep the host from having to handle packets that are not of
interest given the current operating mode of the device.

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
