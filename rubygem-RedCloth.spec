#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-RedCloth
Version  : 4.2.9
Release  : 6
URL      : https://rubygems.org/downloads/RedCloth-4.2.9.gem
Source0  : https://rubygems.org/downloads/RedCloth-4.2.9.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-RedCloth-bin
Requires: rubygem-RedCloth-lib
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-rvm

%description
= RedCloth - Textile parser for Ruby
Homepage::  http://redcloth.org
Author::    Jason Garber
License::   MIT

%package bin
Summary: bin components for the rubygem-RedCloth package.
Group: Binaries

%description bin
bin components for the rubygem-RedCloth package.


%package lib
Summary: lib components for the rubygem-RedCloth package.
Group: Libraries

%description lib
lib components for the rubygem-RedCloth package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n RedCloth-4.2.9
gem spec %{SOURCE0} -l --ruby > rubygem-RedCloth.gemspec

%build
gem build rubygem-RedCloth.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
RedCloth-4.2.9.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/RedCloth-4.2.9
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/RedCloth-4.2.9.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/RedCloth-4.2.9/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/RedCloth-4.2.9/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/RedCloth-4.2.9/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/.gemtest
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/CHANGELOG
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/bin/redcloth
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/doc/textile_reference.html
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/redcloth.h
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/redcloth_attributes.c
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/redcloth_attributes.o
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/redcloth_inline.c
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/redcloth_inline.o
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/redcloth_scan.c
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/redcloth_scan.o
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/case_sensitive_require/RedCloth.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth/erb_extension.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth/formatters/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth/formatters/html.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth/formatters/latex.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth/formatters/latex_entities.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth/textile_doc.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth_scan.jar
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/tasks/pureruby.rake
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/redcloth.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/benchmark_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/custom_tags_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/erb_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/extension_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/basic.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/code.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/definitions.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/extra_whitespace.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/filter_html.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/filter_pba.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/html.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/images.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/instiki.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/links.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/lists.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/poignant.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/sanitize_html.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/table.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/textism.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/fixtures/threshold.yml
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/class_filtered_html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/filtered_html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/html_no_breaks_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/id_filtered_html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/latex_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/lite_mode_html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/no_span_caps_html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/sanitized_html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/formatters/style_filtered_html_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/parser_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/tasks/compile.rake
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/tasks/gems.rake
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/tasks/ragel_extension_task.rb
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/tasks/release.rake
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/tasks/rspec.rake
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/tasks/rvm.rake
/usr/lib64/ruby/gems/2.3.0/specifications/RedCloth-4.2.9.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/redcloth

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/RedCloth-4.2.9/redcloth_scan.so
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/ext/redcloth_scan/redcloth_scan.so
/usr/lib64/ruby/gems/2.3.0/gems/RedCloth-4.2.9/lib/redcloth_scan.so
