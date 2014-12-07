%define _build_pkgcheck_srpm %{nil}

%define mname pygpgme
%define _exclude_files_from_autoprov %{python2_sitearch}/.*\\.so
%define _exclude_files_from_autoprov %{python_sitearch}/.*\\.so

Name:           python-gpgme
Version:        0.3
Release:        2
Summary:        Python module for working with OpenPGP messages
License:        LGPLv2+
Group:          Development/Python
URL:            https://launchpad.net/pygpgme
Source0:        https://pypi.python.org/packages/source/p/%{mname}/%{mname}-%{version}.tar.gz
Source100:      python-gpgme.rpmlintrc
BuildRequires:  pkgconfig(python3)
BuildRequires:  gpgme-devel

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and decrypt
files using the OpenPGP format.  It is built on top of GNU Privacy Guard and
the GPGME library.

%package -n python2-gpgme
Summary:	Python 3 module for working with OpenPGP messages
Group:		Development/Python
BuildRequires:	pkgconfig(python2)

%description -n python2-gpgme
PyGPGME is a Python 3 module that lets you sign, verify, encrypt and decrypt
files using the OpenPGP format.  It is built on top of GNU Privacy Guard and
the GPGME library.

%prep
%setup -q -n %{mname}-%{version}
cp -a . %{py3dir} 

%build
CFLAGS="$RPM_OPT_FLAGS" python2 setup.py build

pushd %{py3dir} 
CFLAGS="$RPM_OPT_FLAGS" python setup.py build
popd


%install
pushd %{py3dir}
python setup.py install -O1 --skip-build --root %{buildroot}
popd

python2 setup.py install -O1 --skip-build --root %{buildroot}
# No need to ship the tests
rm -rf %buildroot/%{python2_sitearch}/gpgme/tests/
rm -rf %buildroot/%{python_sitearch}/gpgme/tests/


%files
%doc README PKG-INFO
%{python_sitearch}/*

%files -n python2-gpgme
%{python2_sitearch}/*






