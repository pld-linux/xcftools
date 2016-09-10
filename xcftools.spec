Summary:	Tools for extracting information from Gimp's native file format XCF
Summary(pl.UTF-8):	Narzędzia do wydobywania informacji z natywnego formatu Gimpa XCF
Name:		xcftools
Version:	1.0.7
%define	gitref	196f51790bbaff594525935adeab1247bb798946
%define	snap	20150128
Release:	1.%{snap}.1
# included (GPL v2+) GIMP code is used only as source to generate some enums, the rest is PD
License:	Public Domain
Group:		Applications/Graphics
Source0:	https://github.com/j-jorge/xcftools/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	fb4626e9066e3925ddfee049feb755c6
# original version at <http://henning.makholm.net/software>, but development seems stalled there
URL:		https://github.com/j-jorge/xcftools
BuildRequires:	gettext-tools
BuildRequires:	libpng-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xcftools is a set of fast command-line tools for extracting
information from the Gimp's native file format XCF. The tools
are designed to allow efficient use of layered XCF files as
sources in a build system that use 'make' and similar tools
to manage automatic processing of the graphics. These tools
work independently of the Gimp engine and do not require the
Gimp to even be installed.

%description -l pl.UTF-8
Xcftools to zbiór szybkich narzędzi linii poleceń do wydobywania
informacji z natywnego formatu plików Gimpa XCF. Narzędzia są
zaprojektowane tak, aby umożliwić wydajne zastosowanie plików XCF z
warstwami jako źródłowych w systemie budowania wykorzystującym "make"
i podobne narzędzia do automatycznego przetwarzania grafiki. Narzędzia
te działają niezależnie od silnika Gimpa i nie wymagają nawet samej
instalacji Gimpa.

%prep
%setup -q -n %{name}-%{gitref}

%build
%configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README 
%attr(755,root,root) %{_bindir}/xcf2png
%attr(755,root,root) %{_bindir}/xcf2pnm
%attr(755,root,root) %{_bindir}/xcfinfo
%attr(755,root,root) %{_bindir}/xcfview
%{_mandir}/man1/xcf2png.1*
%{_mandir}/man1/xcf2pnm.1*
%{_mandir}/man1/xcfinfo.1*
%{_mandir}/man1/xcfview.1*
%lang(da) %{_mandir}/da/man1/xcf2png.1*
%lang(da) %{_mandir}/da/man1/xcf2pnm.1*
%lang(da) %{_mandir}/da/man1/xcfinfo.1*
%lang(da) %{_mandir}/da/man1/xcfview.1*
