%define modname	Image-ExifTool
%define modver 9.70

Summary:	Read and write meta information

Name:		perl-%{modname}
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2
Group:		Development/Perl
Url:	http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Image/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
Provides:	Image-ExifTool

%description
ExifTool provides an extensible set of perl modules to read and write meta
information in image, audio and video files, including the maker note
information of many digital cameras by various manufacturers such as Canon,
Casio, FujiFilm, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon,
Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Ricoh, Sanyo and Sigma/Foveon.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}} -DENGLISH"

%check
make test

%install
%makeinstall_std

%files
%{_bindir}/*
%{perl_vendorlib}/Image
%{perl_vendorlib}/File
%{_mandir}/man1/*
%{_mandir}/man3/*
