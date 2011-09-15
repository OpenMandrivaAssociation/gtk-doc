%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif
Summary: API documentation generation tool for GTK+ and GNOME
Name: 		gtk-doc
Version: 1.18
Release: 	%mkrel 1
License: 	GPLv2+ and GFDL
Group: 		Development/GNOME and GTK+
Source:		http://ftp.gnome.org/pub/GNOME/sources/gtk-doc/%{name}-%{version}.tar.xz
BuildRequires:	libxslt-proc
BuildRequires:	openjade
BuildRequires:  docbook-dtd43-xml
BuildRequires:  docbook-style-xsl
BuildRequires:  scrollkeeper
BuildRequires:  gnome-doc-utils
BuildRequires:  dblatex
BuildRequires:  source-highlight
#gw for building the checks
BuildRequires:  glib2-devel
BuildRequires:  rarian
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch: 	noarch
URL: 		http://www.gtk.org/gtk-doc/
Requires:   libxslt-proc
Requires: 	docbook-utils
Requires:   docbook-dtd43-xml
Requires: 	docbook-style-xsl
Requires:	diffutils
Requires:  source-highlight
%define _requires_exceptions perl(gtkdoc-common.pl)
Requires(post)  : scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3

%description
gtk-doc is a tool for generating API reference documentation.
it is used for generating the documentation for GTK+, GLib
and GNOME.

%package mkpdf
Summary: API documentation PDF format generation tool for GTK+ and GNOME
Group: Development/GNOME and GTK+
Requires: %{name} = %version
Requires: dblatex
Conflicts: %{name} < 1.17-3

%description mkpdf
gtkdoc-mkpdf is a tool for generating API reference documentation in PDF format.
it is used for generating the documentation for GTK+, GLib and GNOME.

%prep
%setup -q
# Move this doc file to avoid name collisions
mv doc/README doc/README.docs

%build
./configure --prefix=%_prefix --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std pkgconfigdir=%pkgconfigdir

# include shared directory
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html

%find_lang %name-manual --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-manual.lang
done


%check
PERL5LIB=$(pwd) PATH=$PATH:$(pwd) make check

%post
%update_scrollkeeper

%postun
%clean_scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name-manual.lang
%defattr(-, root, root)
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
%pkgconfigdir/*
%{_datadir}/aclocal/*
%dir %_datadir/omf/%name-manual
%_datadir/omf/%name-manual/*-C.omf

%files mkpdf
%defattr(-, root, root)
%{_bindir}/gtkdoc-mkpdf
