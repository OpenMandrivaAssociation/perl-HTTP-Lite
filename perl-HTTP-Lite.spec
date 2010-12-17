%define upstream_name    HTTP-Lite
%define upstream_version 2.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Lightweight HTTP implementation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*


