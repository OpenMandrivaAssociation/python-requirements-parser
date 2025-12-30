Name:		python-requirements-parser
Version:	0.13.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/r/requirements-parser/requirements_parser-%{version}.tar.gz
Summary:	This is a small Python module for parsing Pip requirement files.
URL:		https://pypi.org/project/requirements-parser/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python%{pyver}dist(poetry-core)
BuildSystem:	python
BuildArch:	noarch

%description
This is a small Python module for parsing Pip requirement files.

%files
%{py_sitedir}/requirements
%{py_sitedir}/requirements_parser-*.*-info
