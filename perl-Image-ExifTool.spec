%define upstream_name    Image-ExifTool
%define upstream_version 8.50

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:    Read and write meta information
License:    GPL
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Image/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Obsoletes:  Image-ExifTool
Provides:   Image-ExifTool

%description
ExifTool provides an extensible set of perl modules to read and write meta
information in image, audio and video files, including the maker note
information of many digital cameras by various manufacturers such as Canon,
Casio, FujiFilm, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon,
Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Ricoh, Sanyo and Sigma/Foveon.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
