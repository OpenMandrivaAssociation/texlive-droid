Name:		texlive-droid
Version:	54512
Release:	1
Summary:	LaTeX support for the Droid font families
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/droid
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/droid.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/droid.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Droid typeface family was designed in the fall of 2006 by
Steve Matteson, as a commission from Google to create a set of
system fonts for its Android platform. The goal was to provide
optimal quality and comfort on a mobile handset when rendered
in application menus, web browsers and for other screen text.
The Droid family consists of Droid Serif, Droid Sans and Droid
Sans Mono fonts, licensed under the Apache License Version 2.0.
The bundle includes the fonts in both TrueType and Adobe Type 1
formats. The package does not support the Droid Pro family of
fonts, available for purchase from the Ascender foundry.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/droid
%{_texmfdistdir}/fonts/map/dvips/droid
%{_texmfdistdir}/fonts/tfm/ascender/droid
%{_texmfdistdir}/fonts/truetype/ascender/droid
%{_texmfdistdir}/fonts/type1/ascender/droid
%{_texmfdistdir}/fonts/vf/ascender/droid
%{_texmfdistdir}/tex/latex/droid
%doc %{_texmfdistdir}/doc/fonts/droid

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
