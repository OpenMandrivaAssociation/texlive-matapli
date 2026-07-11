%global tl_name matapli
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.0
Release:	%{tl_revision}.1
Summary:	Class for the french journal MATAPLI
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/matapli
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/matapli.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/matapli.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a class for the french journal "MATAPLI" of the Societe de
Mathematiques Appliquees et Industrielles (SMAI).

