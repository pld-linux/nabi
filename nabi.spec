Summary:	Nabi - The Easy Hangul XIM
Summary(pl.UTF-8):	Nabi - The Easy Hangul XIM - łatwa metoda XIM oparta na silniku Hangul
Name:		nabi
Version:	1.0.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/choehwanjin/nabi/releases
Source0:	https://github.com/choehwanjin/nabi/archive/%{name}-%{version}.tar.gz
# Source0-md5:	45bf90d10c448c5b5785dc9f4c1117c5
URL:		https://github.com/choehwanjin/nabi
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.4.0
BuildRequires:	libhangul-devel >= 0.1.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	gtk+2 >= 1:2.4.0
Requires:	libhangul >= 0.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nabi is the easy Hangul XIM for Korean characters.

%description -l pl.UTF-8
Nabi to łatwa metoda wprowadzania znaków dla X (XIM) dla znaków
koreańskich, wykorzystująca silnik Hangul.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%{__glib_gettextize}
%{__autopoint}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/nabi
%{_datadir}/nabi
