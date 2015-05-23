# bcloud.spec
# Used to build rpm for bcloud on Fedora
# Released by wangjiezhe <wangjiezhe@gmail.com>
# This spec file is published under the GPLv3 license

# Template is originally generated by "rpmdev-newspec -t python"

%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           bcloud
Version:        3.7.1
Release:        1%{?dist}
Summary:        Baidu Pan client for Linux Desktop users

License:        GPLv3
URL:            https://github.com/LiuLang/bcloud
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:  python3-gobject
Requires:  python3-urllib3
Requires:  gnome-icon-theme-symbolic
Requires:  python3-keyring
Requires:  python3-dbus
Requires:  libnotify
Requires:  python3-crypto
Requires:  python3-lxml
Requires:  python3-cssselect

%description
Baidu Pan client for Linux Desktop users.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc LICENSE README.md HISTORY
%{python3_sitelib}/*
%{_datadir}/icons/*
%{_datadir}/bcloud/*
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
# generated by python3
%exclude %{python3_sitelib}/bcloud/__pycache__

%post
cd ${python3_sitelib}
for file in bcloud*
do
    if [ -f $file ] && [[ $file != "bcloud-%{version}-py%{python3_version}.egg-info" ]]
    then
        rm $file
    fi
done

