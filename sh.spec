Summary:	Shell
Name:		sh
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Shells
Group(de):	Applikationen/Shells
Group(pl):	Aplikacje/Pow³oki
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		interpreter		ksh

%description
This dummy package provides /bin/sh.

%description -l pl
Ten niby-pakiet udostêpnia /bin/sh.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

ln -sf %{interpreter} $RPM_BUILD_ROOT/bin/sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/sh" >> /etc/shells
else
	while read SHNAME; do
	        if [ "$SHNAME" = "/bin/sh" ]; then
        	        HAS_SH=1
	        fi
	done < /etc/shells
	[ -n "$HAS_SH" ] || echo "/bin/sh" >> /etc/shells
fi

%preun
if [ "$1" = "0" ]; then
	while read SHNAME; do
		[ "$SHNAME" = "/bin/sh" ] || echo "$SHNAME"
	done < /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) /bin/sh
