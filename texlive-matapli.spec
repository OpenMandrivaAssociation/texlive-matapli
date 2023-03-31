Name:		texlive-matapli
Version:	62632
Release:	2
Summary:	Class for the french journal "MATAPLI"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/matapli
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matapli.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/matapli.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a class for the french journal "MATAPLI" of the Societe
de Mathematiques Appliquees et Industrielles (SMAI).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/matapli
%doc %{_texmfdistdir}/doc/latex/matapli

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
