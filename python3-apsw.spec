#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define		module	apsw
%define		sqlite_ver 3.38.5

Summary:	Another Python SQLite Wrapper
Summary(pl.UTF-8):	Another Python SQLite Wrapper - jeszcze jeden pythonowy wrapper dla SQLite
Name:		python3-%{module}
Version:	3.49.1.0
Release:	1
License:	Free
Group:		Libraries/Python
Source0:	https://github.com/rogerbinns/apsw/releases/download/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	7cbb9dc1029b29511e00a6f10eea3e69
URL:		http://rogerbinns.github.io/apsw/
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	sqlite3-devel >= %{sqlite_ver}
BuildRequires:	unzip
Requires:	sqlite3 >= %{sqlite_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
APSW provides an SQLite 3 wrapper that provides the thinnest layer
over SQLite 3 possible. Everything you can do from the C API to SQLite
3, you can do from Python. Although APSW looks vaguely similar to the
DBAPI, it is not compliant with that API and instead works the way
SQLite 3 does.

%description -l pl.UTF-8
APSW udostępnia wrapper SQLite 3 dostarczający najcieńszą jak to tylko
możliwe warstwę ponad SQLite 3. Wszystko co można zrobić z poziomu API
C SQLite 3 można zrobić także z poziomu Pythona. Chociaż APSQ wygląda
dosyć podobnie do DBAPI, nie jest kompatybilne z tym API, natomiast
działa tak, jak SQLite 3.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build --enable=load_extension %{?with_tests:test}

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/apsw
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/*.pyi
%{py3_sitedir}/%{module}/fts_test_strings
%{py3_sitedir}/%{module}/py.typed
%{py3_sitedir}/%{module}-%{version}*-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
