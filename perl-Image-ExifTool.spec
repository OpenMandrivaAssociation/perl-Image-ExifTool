%define modname	Image-ExifTool

Summary:	Read and write meta information

Name:		perl-%{modname}
Version:	13.61
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://exiftool.org/
Source0:	https://downloads.sourceforge.net/project/exiftool/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

%description
ExifTool provides an extensible set of perl modules to read and write meta
information in image, audio and video files, including the maker note
information of many digital cameras by various manufacturers such as Canon,
Casio, FujiFilm, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon,
Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Ricoh, Sanyo and Sigma/Foveon.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build CFLAGS="%{optflags} -DENGLISH"

%check
make test

%install
%make_install

%files
%{_bindir}/*
%{perl_vendorlib}/Image
%{perl_vendorlib}/File
%{_mandir}/man1/*
%{_mandir}/man3/*
