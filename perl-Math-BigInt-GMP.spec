#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	BigInt-GMP
Summary:	Math::BigInt::GMP - use the GMP library for Math::BigInt routines
Summary(pl):	Math::BigInt::GMP - wykorzystanie biblioteki GMP do funkcji Math::BigInt
Name:		perl-Math-BigInt-GMP
Version:	1.14
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3067740831f9b47ed8ae852753c411c6
BuildRequires:	gmp-devel
BuildRequires:	perl-Math-BigInt >= 1.64
BuildRequires:	perl(Math::BigFloat) >= 1.38
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.64
Requires:	perl(Math::BigFloat) >= 1.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::BigInt::GMP provides support for big integer calculations via
means of the GMP C-library. Math::BigInt::GMP now no longer uses
Math::GMP, but provides it's own XS layer to access the GMP C-library.
This cuts out another (perl sub routine) layer and also reduces the
memory footprint by not loading Math::GMP and Carp at all.

%description -l pl
Math::BigInt::GMP dostarcza obs³ugê obliczeñ na wielkich liczbach
ca³kowitych z wykorzystaniem funkcjonalno¶ci biblioteki C GMP. Modu³
ten ju¿ nie u¿ywa Math::GMP, ale dostarcza w³asn± warstwê XS do
odwo³ywania siê do biblioteki GMP w C. Dziêki temu nie ma kolejnej
warstwy (podprocedury Perla), a wykorzystanie pamiêci jest mniejsze
dziêki nie wczytywaniu modu³ów Math::GMP i Carp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

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
%{perl_vendorarch}/auto/Math/BigInt/GMP/GMP.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/BigInt/GMP/GMP.so
%{_mandir}/man3/*
