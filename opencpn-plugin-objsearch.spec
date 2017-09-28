%global commit 2197a4d161cb9c7c377632ec5ee321d79055f17f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner nohal
%global project objsearch_pi
%global plugin objsearch

Name: opencpn-plugin-%{plugin}
Summary: Vector chart search plugin for OpenCPN
Version: 0.0
Release: 0.1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{project}/archive/%{commit}/%{project}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Supplements: opencpn%{_isa}

%description
Allows search of named objects on S-57 and CM93 vector charts.

Note: After the installation, the plugin does not know anything about
your charts.  You must view a chart at least once to populate the
plugin's database with it's content.  This one time operation makes
OpenCPN slower.  During subsequent views of the same chart the speed
of the application is unaffected.  Once the database is populated, the
charts are no longer needed, so if you prefer to use raster charts,
you can populate the database from the ENC chartset and then switch
back to RNC charts and the search capabilities will still be
available.

%prep
%autosetup -n %{project}-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so

%{_datadir}/opencpn/plugins/%{plugin}_pi
