%define upstream_name    Locale-Maketext-Gettext
Name:		perl-%{upstream_name}
Version:	1.32
Release:	2
Summary:	Joins the gettext and Maketext frameworks
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/imacat/Locale-Maketext-Gettext
Source0:	https://cpan.metacpan.org/authors/id/I/IM/IMACAT/Locale-Maketext-Gettext-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	perl(Digest::SHA)
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
%setup -q -n %{upstream_name}-%{version}
rm t/00-signature.t

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

