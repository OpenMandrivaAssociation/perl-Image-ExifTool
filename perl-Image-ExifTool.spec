%define upstream_name    Image-ExifTool
%define upstream_version 8.60

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Read and write meta information
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Image/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildArch:	noarch
Provides:	Image-ExifTool

%description
ExifTool provides an extensible set of perl modules to read and write meta
information in image, audio and video files, including the maker note
information of many digital cameras by various manufacturers such as Canon,
Casio, FujiFilm, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta, Nikon,
Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Ricoh, Sanyo and Sigma/Foveon.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%optflags} -DENGLISH"

%check
make test

%install
%makeinstall_std

%files
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/Image
%{perl_vendorlib}/File


%changelog
* Tue Jun 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:8.600.0-1mdv2011.0
+ Revision: 687703
- update to new version 8.60

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1:8.500.0-1
+ Revision: 643383
- update to new version 8.50

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:8.400.0-1mdv2011.0
+ Revision: 601877
- update to new version 8.40

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1:8.250.0-1mdv2011.0
+ Revision: 553135
- update to 8.25

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1:8.150.0-1mdv2010.1
+ Revision: 526454
- update to 8.15

* Tue Feb 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1:8.100.0-1mdv2010.1
+ Revision: 502642
- update to 8.10

* Sat Nov 21 2009 Jérôme Quelin <jquelin@mandriva.org> 1:8.0.0-1mdv2010.1
+ Revision: 467877
- update to 8.00

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 1:7.890.0-1mdv2010.0
+ Revision: 418418
- update to 7.89

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1:7.820.0-1mdv2010.0
+ Revision: 402541
- rebuild using %%perl_convert_version

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.82-1mdv2010.0
+ Revision: 391949
- update to new version 7.82

* Tue Feb 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.67-1mdv2009.1
+ Revision: 339146
- update to new version 7.67

* Wed Jan 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.60-1mdv2009.1
+ Revision: 326534
- update to new version 7.60

* Tue Oct 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.51-1mdv2009.1
+ Revision: 297813
- update to new version 7.51

* Mon Oct 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.50-1mdv2009.1
+ Revision: 297543
- update to new version 7.50

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1:7.30-2mdv2009.0
+ Revision: 268531
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 01 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.30-1mdv2009.0
+ Revision: 214056
- update to new version 7.30

* Tue Apr 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.25-1mdv2009.0
+ Revision: 196475
- update to new version 7.25
- update to new version 7.25

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.21-1mdv2009.0
+ Revision: 194858
- update to new version 7.21
- update to new version 7.21

* Wed Feb 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.15-1mdv2008.1
+ Revision: 162978
- update to new version 7.15

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:7.00-1mdv2008.1
+ Revision: 104499
- update to new version 7.00

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:6.90-1mdv2008.0
+ Revision: 46529
- update to new version 6.90


* Thu Mar 08 2007 Guillaume Rousse <guillomovitch@mandriva.org> 6.76-1mdv2007.1
+ Revision: 138516
- new version

* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:6.57-1mdv2007.1
+ Revision: 86578
- new version
- Import perl-Image-ExifTool

* Fri Sep 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:6.42-1mdv2007.0
- New version 6.42

* Sat Sep 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:6.36-1mdv2007.0
- New version 6.36
- drop patch0
- trim down description

* Sat Aug 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:6.29-1mdv2007.0
- New version 6.29

* Fri Jun 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1:6.17-1mdv2007.0
- new version
- spec cleanup
- rpmbuidupdate aware
- don't ship empty directories

* Fri May 19 2006 Oden Eriksson <oeriksson@mandriva.com> 1:6.12-3mdk
- fixed better gif support (P0)

* Sun Apr 16 2006 Jerome Martin <jmartin@mandriva.org> 1:6.12-2mdk
- Removed perl requirement (Thx Guillaume Rousse)

* Sat Apr 08 2006 Jerome Martin <jmartin@mandriva.org> 1:6.12-1mdk
- New version
- Fixed spec file

* Fri Apr 07 2006 Jerome Martin <jmartin@mandriva.org> 6.00-1mdk
- Initial version

