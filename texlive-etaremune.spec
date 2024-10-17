Name:		texlive-etaremune
Version:	15878
Release:	2
Summary:	Reverse-counting enumerate environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etaremune
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
