%define oname gpgmepy
%define module gpg

Name:		python-gpgme
Version:	2.0.0
Release:	1
Summary:	Python bindings to the GPGME API of the GnuPG cryptography library.
License:	LGPL-2.1-or-later
Group:		Development/Python
URL:		https://gnupg.org/software/gpgme/index.html
Source0:	https://www.gnupg.org/ftp/gcrypt/%{oname}/%{oname}-%{version}.tar.bz2
BuildSystem:	python

BuildRequires:	autoconf automake slibtool
BuildRequires:	libtool-base
BuildRequires:	pkgconfig
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:	pkgconfig(gpgme)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:  swig

%patchlist
python-gpgme-COPY_FILES.patch
python-gpgme-no-beta-suffix.patch
python-gpgme-pep621-pyproject.patch
python-gpgme-2.0.0b4-compile.patch

%description
Python bindings to the GPGME API of the GnuPG cryptography library.

%build
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
autoreconf -fiv
%configure \
    --with-libgpg-error-prefix=%{_libdir} \
    --with-gpgme-prefix=%{_libdir} \
    %{nil}

ln -sf "./src" gpg
touch copystamp
%py_build

%files
%doc README
%license COPYING COPYING.LESSER
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
