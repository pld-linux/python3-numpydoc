#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension to support docstrings in Numpy format
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do obsług docstringów w formacie Numpy
Name:		python-numpydoc
Version:	0.9.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/numpydoc/
Source0:	https://files.pythonhosted.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz
# Source0-md5:	d3320d808b8776727bac05b32fb24c82
URL:		https://pypi.org/project/numpydoc/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.6.5
BuildRequires:	python-jinja2 >= 2.3
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.6.5
BuildRequires:	python3-jinja2 >= 2.3
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
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

%package -n python3-numpydoc
Summary:	Sphinx extension to support docstrings in Numpy format
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do obsług docstringów w formacie Numpy
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-numpydoc
This package provides the numpydoc Sphinx extension for handling
docstrings formatted according to the NumPy documentation format. The
extension also adds the code description directives "np:function",
"np-c:function", etc.

%description -n python3-numpydoc -l pl.UTF-8
Ten pakiet zawiera rozszerzenie Sphinksa do obsługi docstringów
sformatowanych zgodnie z formatem dokumentacji NumPy. Rozszerzenie
dodaje także dyrektywy opisu kodu "np:function", "np-c:function" itp.

%prep
%setup -q -n numpydoc-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest numpydoc/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest numpydoc/tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/numpydoc/tests
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/numpydoc/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py_sitescriptdir}/numpydoc
%{py_sitescriptdir}/numpydoc-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-numpydoc
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/numpydoc
%{py3_sitescriptdir}/numpydoc-%{version}-py*.egg-info
%endif
