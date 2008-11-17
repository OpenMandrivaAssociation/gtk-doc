%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif
Summary: API documentation generation tool for GTK+ and GNOME
Name: 		gtk-doc
Version: 1.11
Release: 	%mkrel 1
License: 	GPLv2+ and GFDL
Group: 		Development/GNOME and GTK+
Source:		http://ftp.gnome.org/pub/GNOME/sources/gtk-doc/%{name}-%{version}.tar.bz2
BuildRequires:	libxslt-proc
BuildRequires:	openjade
BuildRequires:  docbook-dtd43-xml
BuildRequires:  docbook-style-xsl
BuildRequires:  scrollkeeper
BuildRequires:  gnome-doc-utils
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch: 	noarch
URL: 		http://www.gtk.org/rdp
Requires:   libxslt-proc
Requires: 	docbook-utils
Requires:   docbook-dtd43-xml
Requires: 	docbook-style-xsl
Requires:	diffutils
%define _requires_exceptions perl(gtkdoc-common.pl)
Requires(post)  : scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3

%description
gtk-doc is a tool for generating API reference documentation.
it is used for generating the documentation for GTK+, GLib
and GNOME.

%prep
%setup -q

# Move this doc file to avoid name collisions
mv doc/README doc/README.docs

%build
./configure --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std pkgconfigdir=%pkgconfigdir

# include shared directory
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html

rm -rf %buildroot/var/lib/scrollkeeper

%find_lang %name-manual --with-gnome

%post
%update_scrollkeeper

%postun
%clean_scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name-manual.lang
%defattr(-, root, root)
%doc AUTHORS README doc/* examples
%{_bindir}/*
%{_datadir}/gtk-doc
%{_datadir}/sgml/gtk-doc
%pkgconfigdir/*
%{_datadir}/aclocal/*
%dir %_datadir/omf/%name-manual
%_datadir/omf/%name-manual/*-C.omf


