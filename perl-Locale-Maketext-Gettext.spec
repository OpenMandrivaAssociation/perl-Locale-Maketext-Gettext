%define upstream_name    Locale-Maketext-Gettext
%define upstream_version 1.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Joins the gettext and Maketext frameworks
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_bindir}/maketext
%{_mandir}/man3/*
%{_mandir}/man1/maketext.1.*
%{perl_vendorlib}/Locale

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.280.0-1mdv2010.0
+ Revision: 403395
- rebuild using %%perl_convert_version

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.28-1mdv2010.0
+ Revision: 390361
- update to new version 1.28

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2010.0
+ Revision: 370136
- update to new version 1.27

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.26-2mdv2009.0
+ Revision: 268540
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdv2009.0
+ Revision: 213717
- import perl-Locale-Maketext-Gettext


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdv2009.0
- first mdv release
