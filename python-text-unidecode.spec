%global srcname text-unidecode

Name:           python-%{srcname}
Version:        1.2
Release:        1%{?dist}
Summary:        text-unidecode is the most basic port of the Text::Unidecode Perl library

License:        Artistic
URL:            https://github.com/kmike/text-unidecode
Source0:        %{pypi_source}

BuildArch:      noarch

%description
%{summary}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/text_unidecode-*.egg-info/
%{python3_sitelib}/text_unidecode
