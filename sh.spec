Summary:	Shell
Summary(pl.UTF-8):	Powłoka
Name:		sh
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Shells
Requires(preun):	fileutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		interpreter		ksh

%description
This dummy package provides /bin/sh.

%description -l pl.UTF-8
Ten niby-pakiet udostępnia /bin/sh.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

ln -sf %{interpreter} $RPM_BUILD_ROOT/bin/sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
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
umask 022
if [ "$1" = "0" ]; then
	while read SHNAME; do
		[ "$SHNAME" = "/bin/sh" ] || echo "$SHNAME"
	done < /etc/shells > /etc/shells.new
	mv -f /etc/shells.new /etc/shells
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) /bin/sh
