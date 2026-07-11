%global tl_name makeindex
%global tl_revision 75712

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Makeindex development sources
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/indexing/makeindexk
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makeindex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(makeindex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains the development sources of makeindex, which is now
maintained as part of TeX Live.

