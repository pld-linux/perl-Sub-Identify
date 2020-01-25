#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Sub
%define	pnam	Identify
Summary:	Sub::Identify - Retrieve names of code references
Summary(pl.UTF-8):	Sub::Identify - odtwarzanie nazw z referencji do kodu
Name:		perl-Sub-Identify
Version:	0.14
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	014f19e72698b6a2cbcb54adc9691825
URL:		http://search.cpan.org/dist/Sub-Identify/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sub::Identify allows you to retrieve the real name of code references.
For this, it uses Perl's introspection mechanism, provided by the B
module.

%description -l pl.UTF-8
Sub::Identify umożliwia odtworzenie prawdziwej nazwy z referencji do
kodu. W tym celu wykorzystuje mechanizm obserwacyjny Perla
udostępniany przez moduł B.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Sub/Identify.pm
%dir %{perl_vendorarch}/auto/Sub/Identify
%attr(755,root,root) %{perl_vendorarch}/auto/Sub/Identify/Identify.so
%{_mandir}/man3/Sub::Identify.3pm*
