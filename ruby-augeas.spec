Name:           ruby-augeas
Version:        0.4.1
Release:        %mkrel 1
Summary:        Ruby bindings for Augeas
Group:          Development/Ruby

License:        LGPLv2+
URL:            http://augeas.net
Source0:        http://augeas.net/download/ruby/ruby-augeas-%{version}.tgz
BuildRequires:  ruby-devel
BuildRequires:  ruby-rake
BuildRequires:  ruby-RubyGems
BuildRequires:  augeas-devel >= 0.5.1
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING README.rdoc NEWS
%{ruby_sitelibdir}/augeas.rb
%{ruby_sitearchdir}/_augeas.so

