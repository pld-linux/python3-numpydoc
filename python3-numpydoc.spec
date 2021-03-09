#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension to support docstrings in Numpy format
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do obsług docstringów w formacie Numpy
Name:		python3-numpydoc
Version:	1.1.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/numpydoc/
Source0:	https://files.pythonhosted.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz
# Source0-md5:	2f05c4592e007b7a1fa37ddcb7e0e91b
URL:		https://pypi.org/project/numpydoc/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.6.5
BuildRequires:	python3-jinja2 >= 2.3
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides the numpydoc Sphinx extension for handling
docstrings formatted according to the NumPy documentation format. The
extension also adds the code description directives "np:function",
"np-c:function", etc.

%description -l pl.UTF-8
Ten pakiet zawiera rozszerzenie Sphinksa do obsługi docstringów
sformatowanych zgodnie z formatem dokumentacji NumPy. Rozszerzenie
dodaje także dyrektywy opisu kodu "np:function", "np-c:function" itp.

%prep
%setup -q -n numpydoc-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m pytest numpydoc/tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/numpydoc/tests

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/numpydoc
%{py3_sitescriptdir}/numpydoc-%{version}-py*.egg-info
%endif
