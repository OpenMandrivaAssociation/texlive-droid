%global tl_name droid
%global tl_revision 77682
%global tl_version 3.2

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	LaTeX support for the Droid font families
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/droid
License:	lppl1.3c apache2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/droid.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/droid.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The Droid typeface family was designed in the fall of 2006 by Steve
Matteson, as a commission from Google to create a set of system fonts
for its Android platform. The goal was to provide optimal quality and
comfort on a mobile handset when rendered in application menus, web
browsers and for other screen text. The Droid family consists of Droid
Serif, Droid Sans and Droid Sans Mono fonts, licensed under the Apache
License Version 2.0. The bundle includes the fonts in both TrueType and
Adobe Type 1 formats. The package does not support the Droid Pro family
of fonts, available for purchase from the Ascender foundry.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from droid:
Map droidsans.map
Map droidsansmono.map
Map droidserif.map
TL_DROPIN_EOF
