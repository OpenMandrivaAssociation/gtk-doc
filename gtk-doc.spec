%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif
Summary: API documentation generation tool for GTK+ and GNOME
Name: 		gtk-doc
Version: 1.8
Release: 	%mkrel 1
License: 	LGPL
Group: 		Development/GNOME and GTK+
Source:		http://ftp.gnome.org/pub/GNOME/sources/gtk-doc/%{name}-%{version}.tar.bz2
BuildRequires:	libxslt-proc
BuildRequires:	openjade
BuildRequires:  docbook-dtd412-xml
BuildRequires:  docbook-style-xsl
BuildRequires:  scrollkeeper
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch: 	noarch
URL: 		http://www.gtk.org/rdp
Requires:   libxslt-proc
Requires: 	docbook-utils
Requires:   docbook-dtd412-xml
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
%configure2_5x

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std pkgconfigdir=%pkgconfigdir

# include shared directory
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html

rm -rf %buildroot/var/lib/scrollkeeper

%post
%update_scrollkeeper

%postun
%clean_scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS README doc/* examples
%{_bindir}/*
%{_datadir}/gtk-doc
%{_datadir}/sgml/gtk-doc
%pkgconfigdir/*
%{_datadir}/aclocal/*
%_datadir/gnome/help/gtk-doc-manual/
%dir %_datadir/omf/%name
%_datadir/omf/%name/*-C.omf


