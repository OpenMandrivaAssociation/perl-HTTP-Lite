%define upstream_name    HTTP-Lite
%define upstream_version 2.43

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Lightweight HTTP implementation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/HTTP-Lite-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
HTTP::Lite is a stand-alone lightweight HTTP/1.1 implementation
for perl.  It is not intended as a replacement for the
fully-features LWP module.  Instead, it is intended for use in
situations where it is desirable to install the minimal number of
modules to achieve HTTP support, or where LWP is not a good
candidate due to CPU overhead, such as slower processors.
HTTP::Lite is also significantly faster than LWP.

HTTP::Lite is ideal for CGI (or mod_perl) programs or for bundling
for redistribution with larger packages where only HTTP GET and
POST functionality are necessary.

HTTP::Lite supports basic POST and GET operations only.  As of
0.2.1, HTTP::Lite supports HTTP/1.1 and is compliant with the Host
header, necessary for name based virtual hosting.  Additionally,
HTTP::Lite now supports Proxies.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 2.300.0-2mdv2011.0
+ Revision: 654350
- rebuild for updated spec-helper

* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.300.0-1mdv2011.0
+ Revision: 622698
- update to new version 2.3

* Sun Oct 17 2010 Thierry Vignaud <tv@mandriva.org> 2.200.0-2mdv2011.0
+ Revision: 586146
- fix description

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.200.0-1mdv2011.0
+ Revision: 586065
- import perl-HTTP-Lite



