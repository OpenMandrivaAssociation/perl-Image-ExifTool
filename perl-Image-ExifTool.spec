%define module  Image-ExifTool
%define name    perl-%{module}
%define version 7.21
%define release %mkrel 1
%define epoch   1

Name:       %{name}
Version:    %{version}
Release:    %{release} 
Epoch:      %{epoch}
Summary:    Read and write meta information
License:    GPL
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Image/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
Obsoletes:  Image-ExifTool
Provides:   Image-ExifTool
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
ExifTool provides an extensible set of perl modules to read and write meta
information in image, audio and video files, including the maker note
information of many digital cameras by various manufacturers such as Canon,
Casio, FujiFilm, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon,
Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Ricoh, Sanyo and Sigma/Foveon.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%optflags} -DENGLISH"

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/Image
%{perl_vendorlib}/File


