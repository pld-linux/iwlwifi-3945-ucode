# NOTE: currently it's included in linux-firmware.spec
%define		module		3945
%define		version1	15.28.1.8
Summary:	Microcode image for Intel PRO/Wireless 3945ABG/BG Network Connection Adapter
Summary(pl.UTF-8):	Obraz mikrokodu dla układów bezprzewodowych Intel PRO/Wireless 3945ABG/BG
Name:		iwlwifi-%{module}-ucode
Version:	15.32.2.9
Release:	1.1
License:	distributable
Group:		Base/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
# Source0-md5:	d99a75ab1305d1532a09471b2f9a547a
Source1:	http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version1}.tgz
# Source1-md5:	e793b43b2ef96f8b2605bfee03d78622
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The file provided in this package is required to be present on your
system in order for the Intel PRO/Wireless 3945ABG/BG Network
Connection Adapter driver for Linux (iwlwifi-%{module}) to be able to
operate on your system.

On adapter initialization, and at varying times during the uptime of
the adapter, the microcode is loaded into the RAM on the network
adapter. The microcode provides the low level MAC features including
radio control and high precision timing events (backoff, transmit,
etc.) while also providing varying levels of packet filtering which
can be used to keep the host from having to handle packets that are
not of interest given the current operating mode of the device.

%description -l pl.UTF-8
Plik dostarczany przez ten pakiet jest wymagany w systemie do
działania linuksowego sterownika dla układów bezprzewodowych Intel
PRO/Wireless 3945ABG/BG Network Connection Adapter
(iwlwifi-%{module}).

Przy inicjalizacji układu i w różnych chwilach w trakcie jego
działania mikrokod jest wczytywany do pamięci RAM układu. Mikrokod
udostępnia funkcje niskopoziomowe MAC, w tym sterowanie częścią
radiową i zdarzeniami wymagającymi dużej dokładności czasowej
(oczekiwania, transmisja itp.), a także różne poziomy filtrowania
pakietów, zapobiegające docieraniu do komputera pakietów
niepotrzebnych w danym trybie pracy urządzenia.

%prep
%setup -q -a 1
%{__mv} %{name}-%{version1}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware
cp -a iwlwifi-%{module}-1.ucode $RPM_BUILD_ROOT/lib/firmware
cp -a iwlwifi-%{module}-2.ucode $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.%{name} README.%{name}
/lib/firmware/iwlwifi-3945-*.ucode
