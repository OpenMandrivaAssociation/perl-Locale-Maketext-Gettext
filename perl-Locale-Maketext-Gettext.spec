%define module   Locale-Maketext-Gettext
%define version    1.27
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Joins the gettext and Maketext frameworks
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Locale/%{module}-%{version}.tar.gz
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description

Locale::Maketext::Gettext joins the GNU gettext and Maketext frameworks. It
is a subclass of Locale::Maketext/3 that follows the way GNU gettext works.
It works seamlessly, _both in the sense of GNU gettext and Maketext_. As a
result, you _enjoy both their advantages, and get rid of both their
problems, too._

You start as an usual GNU gettext localization project: Work on PO files
with the help of translators, reviewers and Emacs. Turn them into MO files
with _msgfmt_. Copy them into the appropriate locale directory, such as
_/usr/share/locale/de/LC_MESSAGES/myapp.mo_.

Then, build your Maketext localization class, with your base class changed
from Locale::Maketext/3 to Locale::Maketext::Gettext. That is all.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/maketext
%{_mandir}/man3/*
%{_mandir}/man1/maketext.1.lzma
%{perl_vendorlib}/Locale

