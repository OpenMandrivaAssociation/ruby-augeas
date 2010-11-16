Name:           ruby-augeas
Version:        0.3.0
Release:        %mkrel 1
Summary:        Ruby bindings for Augeas
Group:          Development/Ruby

License:        LGPLv2+
URL:            http://augeas.net
Source0:        http://augeas.net/download/ruby/ruby-augeas-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  ruby ruby-devel rubygem(rake)
BuildRequires:  augeas-devel >= 0.5.1
BuildRequires:  pkgconfig
Requires:       ruby(abi) = 1.8
Requires:       augeas-libs >= 0.5.1
Provides:       ruby(augeas) = %{version}

%description
Ruby bindings for augeas.

%prep
%setup -q


%build
export CFLAGS="$RPM_OPT_FLAGS"
rake build

%install
rm -rf %{buildroot}
install -d -m0755 %{buildroot}%{ruby_sitelibdir}
install -d -m0755 %{buildroot}%{ruby_sitearchdir}
install -p -m0644 lib/augeas.rb %{buildroot}%{ruby_sitelibdir}
install -p -m0755 ext/augeas/_augeas.so %{buildroot}%{ruby_sitearchdir}

%check
rake test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README.rdoc NEWS
%{ruby_sitelibdir}/augeas.rb
%{ruby_sitearchdir}/_augeas.so

