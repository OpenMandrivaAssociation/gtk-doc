Summary:	API documentation generation tool for GTK+ and GNOME
Name:		gtk-doc
Version:	1.20
Release: 	1
License: 	GPLv2+ and GFDL
Group: 		Development/GNOME and GTK+
Url: 		http://www.gtk.org/gtk-doc/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-doc/%{version}/%{name}-%{version}.tar.xz
BuildArch: 	noarch

BuildRequires:  dblatex
BuildRequires:  docbook-dtd43-xml
BuildRequires:  docbook-style-xsl
BuildRequires:  gnome-doc-utils
BuildRequires:	openjade
BuildRequires:  rarian
BuildRequires:  source-highlight
BuildRequires:	xsltproc
#gw for building the checks
BuildRequires:  pkgconfig(glib-2.0)

Requires:	diffutils
Requires:	docbook-utils
Requires:	docbook-dtd412-xml
Requires:	docbook-dtd43-xml
Requires: 	docbook-style-xsl
Requires:	source-highlight
Requires:	xsltproc
%define __noautoreq 'perl\\(gtkdoc-common.pl\\)'
Requires(post,postun): rarian

%description
gtk-doc is a tool for generating API reference documentation.
it is used for generating the documentation for GTK+, GLib
and GNOME.

%package	mkpdf
Summary:	API documentation PDF format generation tool for GTK+ and GNOME
Group:		Development/GNOME and GTK+
Requires:	%{name} = %{version}
Requires:	dblatex
Conflicts:	%{name} < 1.17-3

%description	mkpdf
gtkdoc-mkpdf is a tool for generating API reference documentation in PDF 
format. It is used for generating the documentation for GTK+, GLib and 
GNOME.

%prep
%setup -q
# Move this doc file to avoid name collisions
mv doc/README doc/README.docs

%build
%configure2_5x \
	--build=%{_build} \
	--disable-scrollkeeper

%make

%install
%makeinstall_std 

# include shared directory
install -d -m 755 %{buildroot}%{_datadir}/gtk-doc/html

%check
PERL5LIB=$(pwd) PATH=$PATH:$(pwd) make check

%files 
%doc AUTHORS README doc/* examples
%{_bindir}/gtkdoc-check
%{_bindir}/gtkdoc-depscan
%{_bindir}/gtkdoc-fixxref
%{_bindir}/gtkdoc-mkdb
%{_bindir}/gtkdoc-mkhtml
%{_bindir}/gtkdoc-mkman
%{_bindir}/gtkdoc-mktmpl
%{_bindir}/gtkdoc-rebase
%{_bindir}/gtkdoc-scan
%{_bindir}/gtkdoc-scangobj
%{_bindir}/gtkdoc-scanobj
%{_bindir}/gtkdocize
%{_datadir}/gtk-doc
%{_datadir}/sgml/gtk-doc
%{_datadir}/pkgconfig/gtk-doc.pc
%{_datadir}/aclocal/*

%files mkpdf
%{_bindir}/gtkdoc-mkpdf

