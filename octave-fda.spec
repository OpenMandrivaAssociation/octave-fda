%global octpkg fda

# use actual latest commit because there is not official release yet
%define commit 99f733cfa284fc0fdf911e7da97269197c4dec94

Summary:	Functional data analysis extension for Octave
Name:		octave-%{octpkg}
Version:	1.0.0
Release:	1
Source0:	https://gitlab.com/kakila/fda/-/archive/%{commit}/fda-%{commit}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://gitlab.com/kakila/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.4.0
BuildRequires:	octave-io >= 2.4.11
BuildRequires:	octave-statistics >= 1.4.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-io >= 2.4.11
Requires:	octave-statistics >= 1.4.0

Requires(post): octave
Requires(postun): octave

%description
These functions were developed to support functional data analysis as
described in Ramsay, J. O. and Silverman, B. W. (2005) Functional Data
Analysis. New York: Springer. 

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{commit}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

