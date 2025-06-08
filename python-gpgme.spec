%define beta b4

Name:		python-gpgme
Version:	2.0.0%{?beta:~%{beta}}
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/gpgme/gpgme-%(echo %{version} |sed -e 's,~,,').tar.gz
Summary:	Python bindings to the GPGME API of the GnuPG cryptography library.
URL:		https://pypi.org/project/gpgme/
License:	LGPL2.1+ (the library), GPL2+ (tests and examples)
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python

%patchlist
python-gpgme-2.0.0b4-compile.patch

%description
Python bindings to the GPGME API of the GnuPG cryptography library.

%files
%{py_platsitedir}/gpg
%{py_platsitedir}/*.{i,c,h,py}
%{py_platsitedir}/gpgme-*.*-info
