%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/galactic/.*$
%global __requires_exclude_from ^/opt/ros/galactic/.*$

Name:           ros-galactic-microstrain-inertial-rqt
Version:        2.4.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS microstrain_inertial_rqt package

License:        BSD
URL:            https://github.com/LORD-MicroStrain/microstrain_inertial
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-galactic-geometry-msgs
Requires:       ros-galactic-microstrain-inertial-msgs
Requires:       ros-galactic-nav-msgs
Requires:       ros-galactic-rclpy
Requires:       ros-galactic-rqt-gui
Requires:       ros-galactic-rqt-gui-py
Requires:       ros-galactic-std-msgs
Requires:       ros-galactic-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-galactic-geometry-msgs
BuildRequires:  ros-galactic-microstrain-inertial-msgs
BuildRequires:  ros-galactic-nav-msgs
BuildRequires:  ros-galactic-rclpy
BuildRequires:  ros-galactic-ros-workspace
BuildRequires:  ros-galactic-rqt-gui
BuildRequires:  ros-galactic-rqt-gui-py
BuildRequires:  ros-galactic-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The microstrain_inertial_rqt package provides several RQT widgets to view the
status of Microstrain devices

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/galactic"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/galactic/setup.sh" ]; then . "/opt/ros/galactic/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/galactic

%changelog
* Wed Jan 05 2022 Rob Fisher <rob.fisher@parker.com> - 2.4.0-1
- Autogenerated by Bloom

* Wed Dec 22 2021 Rob Fisher <rob.fisher@parker.com> - 2.3.0-1
- Autogenerated by Bloom

