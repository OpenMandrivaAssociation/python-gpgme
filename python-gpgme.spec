%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"
%define mname pygpgme

Summary:	Python module for working with OpenPGP messages
Name:		python-gpgme
Version:	0.1
Release:	9
Group:		Development/Python
License:	LGPLv2+
Url:		http://cheeseshop.python.org/pypi/pygpgme/0.1
Source0:	http://cheeseshop.python.org/packages/source/p/%{mname}/%{mname}-%{version}.tar.gz
# upstream patch to fix gpgme intialization
# https://bugs.launchpad.net/pygpgme/+bug/452194
Patch0:		python-gpgme-0.1-fix-gpgme-initialization.patch
BuildRequires:	gpgme-devel
BuildRequires:	pkgconfig(python)

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and decrypt
files using the OpenPGP format.  It is built on top of GNU Privacy Guard and
the GPGME library.

%prep
%setup -qn %{mname}-%{version}
%patch0 -p0

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# No need to ship the tests
rm -rf %{buildroot}%{python_sitearch}/gpgme/tests/

%files
%doc README PKG-INFO
%{python_sitearch}/*

