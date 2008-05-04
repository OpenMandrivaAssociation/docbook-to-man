%define name		docbook-to-man
%define deb_release	26
%define version		2.0.0
%define release %mkrel	1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Converter from DocBook SGML into roff man macros
License:	MIT
Group:		Publishing
Source0:	http://ftp.debian.org/debian/pool/main/d/docbook-to-man/%{name}_%{version}.orig.tar.gz
Patch0:		%{name}_%{version}-%{deb_release}.diff.gz
Patch10:	%{name}-debian.patch
Patch11:	%{name}-opt.patch
Patch12:	%{name}-PLD.patch
URL:		http://www.oasis-open.org/docbook/tools/dtm/
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	OpenSP
Requires:	docbook-dtd41-sgml
Requires:	OpenSP
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
docbook-to-man is a batch converter that transforms UNIX-style
manpages from the DocBook SGML format into nroff/troff man macros.

This is not the original version by Fred Dalrymple, but one with the
modifications by David Bolen with Debian changes.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0
%patch10 -p1
%{__patch} -p1 -s < debian/patches/01-conglomeration.dpatch
%patch11 -p1
%patch12 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	ROOT=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/sgml,%{_mandir}/man{1,5}}

%{__make} install \
	ROOT=$RPM_BUILD_ROOT%{_prefix}

install Doc/{docbook-to-man.1,instant.1} $RPM_BUILD_ROOT%{_mandir}/man1
install Doc/transpec.1 $RPM_BUILD_ROOT%{_mandir}/man5/transpec.5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.ANS
%attr(755,root,root) %{_bindir}/docbook-to-man
%attr(755,root,root) %{_bindir}/instant
%{_datadir}/sgml/transpec
%{_mandir}/man1/docbook-to-man.1*
%{_mandir}/man1/instant.1*
%{_mandir}/man5/transpec.5*