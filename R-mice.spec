%global packname  mice
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.11
Release:          1
Summary:          Multivariate Imputation by Chained Equations
Group:            Sciences/Mathematics
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-MASS R-nnet R-methods R-lattice 
Requires:         R-VIM R-lattice R-mitools R-nlme R-Zelig R-lme4 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS R-nnet R-methods R-lattice
BuildRequires:    R-VIM R-lattice R-mitools R-nlme R-Zelig R-lme4 

%description
Multiple Imputation using Fully Conditional Specification

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
