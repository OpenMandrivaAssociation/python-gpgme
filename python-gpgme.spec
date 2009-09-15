%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"
%define mname pygpgme

Name:           python-gpgme
Version:        0.1
Release:        %mkrel 2
Summary:        Python module for working with OpenPGP messages

Group:          Development/Python
License:        LGPLv2+
URL:            http://cheeseshop.python.org/pypi/pygpgme/0.1
Source0:        http://cheeseshop.python.org/packages/source/p/%{mname}/%{mname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  python-devel
BuildRequires:  gpgme-devel

%description
PyGPGME is a Python module that lets you sign, verify, encrypt and decrypt
files using the OpenPGP format.  It is built on top of GNU Privacy Guard and
the GPGME library.

%prep
%setup -q -n %{mname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# No need to ship the tests
rm -rf $RPM_BUILD_ROOT%{python_sitearch}/gpgme/tests/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README PKG-INFO
%{python_sitearch}/*

