Name:		texlive-etaremune
Version:	v1.2
Release:	1
Summary:	Reverse-counting enumerate environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etaremune
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package implements the etaremune environment which is
similar to the enumerate environment, except that labels are
decreasing instead of increasing. The package provides a
noticeably more efficient alternative to the revnum package,
which uses painfully many counters.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
