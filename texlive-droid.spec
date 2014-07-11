# revision 23912
# category Package
# catalog-ctan /fonts/droid
# catalog-date 2011-09-12 10:00:04 +0200
# catalog-license lppl1.3
# catalog-version 2.1
Name:		texlive-droid
Version:	2.1
Release:	8
Summary:	LaTeX support for the Droid font families
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/droid
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/droid.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/droid.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/droid.source.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/droid/DroidSans-Bold.afm
%{_texmfdistdir}/fonts/afm/public/droid/DroidSans.afm
%{_texmfdistdir}/fonts/afm/public/droid/DroidSansMono.afm
%{_texmfdistdir}/fonts/afm/public/droid/DroidSerif-Bold.afm
%{_texmfdistdir}/fonts/afm/public/droid/DroidSerif-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/droid/DroidSerif-Italic.afm
%{_texmfdistdir}/fonts/afm/public/droid/DroidSerif-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/droid/droid-01.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/droid-02.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/droid-03.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/droid-04.enc
%{_texmfdistdir}/fonts/map/dvips/droid/droid.map
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-Slanted-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Bold-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-Slanted-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSans-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-Slanted-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSansMono-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-Slanted-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Bold-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-Upright-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-BoldItalic-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-Upright-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Italic-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-01.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-02.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-03.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-04.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-Slanted-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-SmallCaps-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-SmallCaps-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-SmallCaps-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-SmallCaps-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-SmallCaps-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-SmallCaps-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-SmallCaps-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/droid/DroidSerif-Regular-x2.tfm
%{_texmfdistdir}/fonts/truetype/public/droid/DroidSans-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/droid/DroidSans.ttf
%{_texmfdistdir}/fonts/truetype/public/droid/DroidSansMono.ttf
%{_texmfdistdir}/fonts/truetype/public/droid/DroidSerif-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/droid/DroidSerif-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/droid/DroidSerif-Italic.ttf
%{_texmfdistdir}/fonts/truetype/public/droid/DroidSerif-Regular.ttf
%{_texmfdistdir}/fonts/type1/public/droid/DroidSans-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/droid/DroidSans.pfb
%{_texmfdistdir}/fonts/type1/public/droid/DroidSansMono.pfb
%{_texmfdistdir}/fonts/type1/public/droid/DroidSerif-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/droid/DroidSerif-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/droid/DroidSerif-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/droid/DroidSerif-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-Slanted-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Bold-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-Slanted-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSans-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-Slanted-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSansMono-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-Slanted-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Bold-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-Upright-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-BoldItalic-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-Upright-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Italic-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-Slanted-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-SmallCaps-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-SmallCaps-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-SmallCaps-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-SmallCaps-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-SmallCaps-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-SmallCaps-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-SmallCaps-x2.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-lgr.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-ot1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-t1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-t2a.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-t2b.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-t2c.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-ts1.vf
%{_texmfdistdir}/fonts/vf/public/droid/DroidSerif-Regular-x2.vf
%{_texmfdistdir}/tex/latex/droid/droid.sty
%{_texmfdistdir}/tex/latex/droid/droidmono.sty
%{_texmfdistdir}/tex/latex/droid/droidsans.sty
%{_texmfdistdir}/tex/latex/droid/droidserif.sty
%{_texmfdistdir}/tex/latex/droid/lgrfdm.fd
%{_texmfdistdir}/tex/latex/droid/lgrfdr.fd
%{_texmfdistdir}/tex/latex/droid/lgrfds.fd
%{_texmfdistdir}/tex/latex/droid/ot1fdm.fd
%{_texmfdistdir}/tex/latex/droid/ot1fdr.fd
%{_texmfdistdir}/tex/latex/droid/ot1fds.fd
%{_texmfdistdir}/tex/latex/droid/t1fdm.fd
%{_texmfdistdir}/tex/latex/droid/t1fdr.fd
%{_texmfdistdir}/tex/latex/droid/t1fds.fd
%{_texmfdistdir}/tex/latex/droid/t2afdm.fd
%{_texmfdistdir}/tex/latex/droid/t2afdr.fd
%{_texmfdistdir}/tex/latex/droid/t2afds.fd
%{_texmfdistdir}/tex/latex/droid/t2bfdm.fd
%{_texmfdistdir}/tex/latex/droid/t2bfdr.fd
%{_texmfdistdir}/tex/latex/droid/t2bfds.fd
%{_texmfdistdir}/tex/latex/droid/t2cfdm.fd
%{_texmfdistdir}/tex/latex/droid/t2cfdr.fd
%{_texmfdistdir}/tex/latex/droid/t2cfds.fd
%{_texmfdistdir}/tex/latex/droid/ts1fdm.fd
%{_texmfdistdir}/tex/latex/droid/ts1fdr.fd
%{_texmfdistdir}/tex/latex/droid/ts1fds.fd
%{_texmfdistdir}/tex/latex/droid/x2fdm.fd
%{_texmfdistdir}/tex/latex/droid/x2fdr.fd
%{_texmfdistdir}/tex/latex/droid/x2fds.fd
%doc %{_texmfdistdir}/doc/fonts/droid/CHANGES
%doc %{_texmfdistdir}/doc/fonts/droid/README
%doc %{_texmfdistdir}/doc/fonts/droid/droid.pdf
%doc %{_texmfdistdir}/doc/fonts/droid/droid.tex
%doc %{_texmfdistdir}/doc/fonts/droid/droidsans-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/droid/droidsans-samples.tex
%doc %{_texmfdistdir}/doc/fonts/droid/droidsansmono-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/droid/droidsansmono-samples.tex
%doc %{_texmfdistdir}/doc/fonts/droid/droidserif-samples.pdf
%doc %{_texmfdistdir}/doc/fonts/droid/droidserif-samples.tex
%doc %{_texmfdistdir}/doc/fonts/droid/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/droid/Makefile
%doc %{_texmfdistdir}/source/fonts/droid/droid-01.etx
%doc %{_texmfdistdir}/source/fonts/droid/droid-02.etx
%doc %{_texmfdistdir}/source/fonts/droid/droid-03.etx
%doc %{_texmfdistdir}/source/fonts/droid/droid-04.etx
%doc %{_texmfdistdir}/source/fonts/droid/droid-drv.tex
%doc %{_texmfdistdir}/source/fonts/droid/droid-fixcyrillic.mtx
%doc %{_texmfdistdir}/source/fonts/droid/droid-fixgreek.mtx
%doc %{_texmfdistdir}/source/fonts/droid/droid-fixlatin.mtx
%doc %{_texmfdistdir}/source/fonts/droid/droid-fixtextcomp.mtx
%doc %{_texmfdistdir}/source/fonts/droid/droid-map.tex
%doc %{_texmfdistdir}/source/fonts/droid/droidsans-drv.tex
%doc %{_texmfdistdir}/source/fonts/droid/droidsansmono-drv.tex
%doc %{_texmfdistdir}/source/fonts/droid/droidserif-drv.tex
%doc %{_texmfdistdir}/source/fonts/droid/ttf2type1.pe

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 751092
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 718263
- texlive-droid
- texlive-droid
- texlive-droid
- texlive-droid

