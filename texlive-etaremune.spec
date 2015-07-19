# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/etaremune
# catalog-date 2009-05-14 13:22:18 +0200
# catalog-license lppl
# catalog-version v1.2
Name:		texlive-etaremune
Version:	v1.2
Release:	10
Summary:	Reverse-counting enumerate environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etaremune
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements the etaremune environment which is
similar to the enumerate environment, except that labels are
decreasing instead of increasing. The package provides a
noticeably more efficient alternative to the revnum package,
which uses painfully many counters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/etaremune/etaremune.sty
%doc %{_texmfdistdir}/doc/latex/etaremune/README
%doc %{_texmfdistdir}/doc/latex/etaremune/etaremune.pdf
#- source
%doc %{_texmfdistdir}/source/latex/etaremune/etaremune.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.2-2
+ Revision: 751585
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.2-1
+ Revision: 718374
- texlive-etaremune
- texlive-etaremune
- texlive-etaremune
- texlive-etaremune

