# Run tests in check section
%bcond_without check

%global goipath         github.com/rfjakob/eme
Version:                1.1

%global common_description %{expand:
Encrypt-Mix-Encrypt for Go.}

%gometa

Name:    %{goname}
Release: 4%{?dist}
Summary: Encrypt-Mix-Encrypt for Go
License: MIT
URL:     %{gourl}
Source:  %{gosource}

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1-3
- Update with the new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.1-1
- First package for Fedora

