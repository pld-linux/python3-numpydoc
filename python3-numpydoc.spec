#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (TODO)
%bcond_without	tests	# unit tests

Summary:	Sphinx extension to support docstrings in Numpy format
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do obsług docstringów w formacie Numpy
Name:		python3-numpydoc
Version:	1.8.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/numpydoc/
Source0:	https://files.pythonhosted.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz
# Source0-md5:	f1dcf7f9e10d72680a6ff71607cce99b
URL:		https://pypi.org/project/numpydoc/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 4.2
BuildRequires:	python3-jinja2 >= 2.10
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-tabulate
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-matplotlib >= 3.5
BuildRequires:	python3-numpy >= 1.21
BuildRequires:	python3-pydata-sphinx-theme >= 0.11
BuildRequires:	sphinx-pdg-3 >= 5.2
%endif
Requires:	python3-modules >= 1:3.7
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
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_cov.plugin" \
%{__python3} -m pytest numpydoc/tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/numpydoc/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/numpydoc
%{py3_sitescriptdir}/numpydoc-%{version}.dist-info
