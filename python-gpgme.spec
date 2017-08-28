%define _build_pkgcheck_srpm %{nil}

%define mname pygpgme
%define _exclude_files_from_autoprov %{python2_sitearch}/.*\\.so
%define _exclude_files_from_autoprov %{python_sitearch}/.*\\.so

Name:           python-gpgme
Version:        0.3
Release:        7
Summary:        Python module for working with OpenPGP messages
License:        LGPLv2+
Group:          Development/Python
URL:            https://launchpad.net/pygpgme
Source0:        https://pypi.python.org/packages/source/p/%{mname}/%{mname}-%{version}.tar.gz
Source100:      python-gpgme.rpmlintrc

# Upstream is dead, but Fedora maintains a fork
# All patches tracked at: https://pagure.io/pygpgme
# Patches for working with gnupg >= 2.1
Patch0001:      0001-reflect-2.1-reporting-for-key-imports.patch
Patch0002:      0002-passphrase_cb-is-deprecated.patch
Patch0003:      0003-handle-generic-error-when-no-passphrase-callback-pre.patch
Patch0004:      0004-add-pubkey_algo-and-hash_algo-attributes-to-signatur.patch
Patch0005:      0005-add-ENCRYPT_NO_ENCRYPT_TO-constant.patch
Patch0006:      0006-ignore-STATUS_KEY_CONSIDERED-when-editing.patch


BuildRequires:  pkgconfig(python3)
BuildRequires:  gpgme-devel

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and decrypt
files using the OpenPGP format.  It is built on top of GNU Privacy Guard and
the GPGME library.

%package -n python2-gpgme
Summary:	Python 2 module for working with OpenPGP messages
Group:		Development/Python
BuildRequires:	pkgconfig(python2)

%description -n python2-gpgme
PyGPGME is a Python 2 module that lets you sign, verify, encrypt and decrypt
files using the OpenPGP format.  It is built on top of GNU Privacy Guard and
the GPGME library.

%prep
%setup -q -n %{mname}-%{version}
%apply_patches

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

