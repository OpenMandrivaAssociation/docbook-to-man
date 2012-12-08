%define name		docbook-to-man
%define deb_release	26
%define version		2.0.0
%define release     %mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Converter from DocBook SGML into roff man macros
License:	MIT
Group:		Publishing
URL:		http://www.oasis-open.org/docbook/tools/dtm/
Source0:	http://ftp.debian.org/debian/pool/main/d/docbook-to-man/%{name}_%{version}.orig.tar.gz
Patch0:		%{name}_%{version}-%{deb_release}.diff.gz
Patch10:	%{name}-debian.patch
Patch11:	%{name}-opt.patch
Patch12:	%{name}-PLD.patch
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
	OPT="%{optflags}" \
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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-7mdv2011.0
+ Revision: 663843
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-6mdv2011.0
+ Revision: 604809
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-5mdv2010.1
+ Revision: 520694
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-4mdv2010.0
+ Revision: 413372
- rebuild

* Thu Feb 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-3mdv2009.1
+ Revision: 342941
- fix optimisations

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-2mdv2009.0
+ Revision: 266572
- rebuild early 2009.0 package (before pixel changes)

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2009.0
+ Revision: 200873
- import from pclinuxos
- Created package structure for docbook-to-man.

