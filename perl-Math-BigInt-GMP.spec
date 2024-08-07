#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	BigInt-GMP
Summary:	Math::BigInt::GMP - use the GMP library for Math::BigInt routines
Summary(pl.UTF-8):	Math::BigInt::GMP - wykorzystanie biblioteki GMP do funkcji Math::BigInt
Name:		perl-Math-BigInt-GMP
Version:	1.7001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86e6ee4832e999ff05fb69aee90980a4
URL:		http://search.cpan.org/dist/Math-BigInt-GMP/
BuildRequires:	gmp-devel
BuildRequires:	perl-Math-BigInt >= 1.999812
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.94
%endif
Requires:	perl-Math-BigInt >= 1.999801
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInt::GMP provides support for big integer calculations via
means of the GMP C-library. Math::BigInt::GMP now no longer uses
Math::GMP, but provides it's own XS layer to access the GMP C-library.
This cuts out another (perl sub routine) layer and also reduces the
memory footprint by not loading Math::GMP and Carp at all.

%description -l pl.UTF-8
Math::BigInt::GMP dostarcza obsługę obliczeń na wielkich liczbach
całkowitych z wykorzystaniem funkcjonalności biblioteki C GMP. Moduł
ten już nie używa Math::GMP, ale dostarcza własną warstwę XS do
odwoływania się do biblioteki GMP w C. Dzięki temu nie ma kolejnej
warstwy (podprocedury Perla), a wykorzystanie pamięci jest mniejsze
dzięki nie wczytywaniu modułów Math::GMP i Carp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES CREDITS LICENSE README TODO
%{perl_vendorarch}/Math/BigInt/GMP.pm
%dir %{perl_vendorarch}/auto/Math/BigInt/GMP
%attr(755,root,root) %{perl_vendorarch}/auto/Math/BigInt/GMP/GMP.so
%{_mandir}/man3/Math::BigInt::GMP.3pm*
