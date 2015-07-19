%define deb_release	26

Summary:	Converter from DocBook SGML into roff man macros
Name:		docbook-to-man
Version:	2.0.0
Release:	16
License:	MIT
Group:		Publishing
Url:		http://www.oasis-open.org/docbook/tools/dtm/
Source0:	http://ftp.debian.org/debian/pool/main/d/docbook-to-man/%{name}_%{version}.orig.tar.gz
Patch0:		%{name}_%{version}-%{deb_release}.diff.gz
Patch10:	%{name}-debian.patch
Patch11:	%{name}-opt.patch
Patch12:	%{name}-PLD.patch

BuildRequires:	docbook-dtd41-sgml
BuildRequires:	OpenSP
Requires:	docbook-dtd41-sgml
Requires:	OpenSP

%description
docbook-to-man is a batch converter that transforms UNIX-style
manpages from the DocBook SGML format into nroff/troff man macros.

This is not the original version by Fred Dalrymple, but one with the
modifications by David Bolen with Debian changes.

%prep
%setup -qn %{name}-%{version}.orig
%patch0
%patch10 -p1
patch -p1 -s < debian/patches/01-conglomeration.dpatch
%patch11 -p1
%patch12 -p1

%build
%make \
	CC="%{__cc}" \
	OPT="%{optflags}" \
	ROOT=%{_prefix}

%install
install -d %{buildroot}{%{_bindir},%{_datadir}/sgml,%{_mandir}/man{1,5}}

%{__make} install \
	ROOT=%{buildroot}%{_prefix}

install Doc/{docbook-to-man.1,instant.1} %{buildroot}%{_mandir}/man1
install Doc/transpec.1 %{buildroot}%{_mandir}/man5/transpec.5

%files
%doc README README.ANS
%{_bindir}/docbook-to-man
%{_bindir}/instant
%{_datadir}/sgml/transpec
%{_mandir}/man1/docbook-to-man.1*
%{_mandir}/man1/instant.1*
%{_mandir}/man5/transpec.5*

