%global tl_name etaremune
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Reverse-counting enumerate environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etaremune
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etaremune.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package implements the etaremune environment which is an enumerate
environment in which the labels decrease instead of increasing. The
package is noticeably more efficient than the revnum package, which uses
painfully many counters.

