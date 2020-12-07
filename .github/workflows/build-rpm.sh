#!/bin/bash
set -ex

# Environment
export VERBOSE=1
export CTEST_OUTPUT_ON_FAILURE=1
export BRANCH=$1

# Platform-specific configuration
source /etc/os-release

CMAKEFLAGS="-DINSTALL_DOC=ON -DUSE_SPHINX_APIDOC=OFF"

# Default to python 3
PYTHON="python3"

if [ "$ID" == "fedora" ]; then
  if [ "$VERSION_ID" -lt 30 ]; then
    PYTHON="python"
  fi
elif [ "$ID" == "centos" ]; then
  yum install -y epel-release
  if [ "$VERSION_ID" -ge 8 ]; then
    sed -i "s/enabled=0/enabled=1/" /etc/yum.repos.d/CentOS-PowerTools.repo
  else
    PYTHON="python"
  fi
fi

if [ "$PYTHON" == "python3" ]; then
  CMAKEFLAGS="$CMAKEFLAGS -DPYTHON_EXPLICIT_VERSION=3"
fi

# Astrorama repository
cat > /etc/yum.repos.d/astrorama.repo << EOF
[bintray--astrorama-fedora]
name=bintray--astrorama-fedora
baseurl=https://dl.bintray.com/astrorama/travis/master/${ID}/\$releasever/\$basearch
gpgcheck=0
repo_gpgcheck=0
enabled=1
EOF

if [ "${BRANCH}" == "develop" ]; then
  cat >> /etc/yum.repos.d/astrorama.repo <<EOF
[bintray--astrorama-fedora-develop]
name=bintray--astrorama-fedora-develop
baseurl=https://dl.bintray.com/astrorama/travis/develop/${ID}/\$releasever/\$basearch
gpgcheck=0
repo_gpgcheck=0
enabled=1
EOF
  CMAKEFLAGS="$CMAKEFLAGS -DCPACK_PACKAGE_RELEASE=r$(date +%Y%m%d%H%M)"
fi

# From the CMakeLists.txt, retrieve the list of dependencies
cmake_deps=$(grep -oP 'elements_project\(\S+\s+\S+ USE \K(\S+ \S+)*(?=\))' CMakeLists.txt)
rpm_dev_deps=$(echo ${cmake_deps} | awk '{for(i=1;i<NF;i+=2){print $i "-devel-" $(i+1)}}')
rpm_doc_deps=$(echo ${cmake_deps} | awk '{for(i=1;i<NF;i+=2){print $i "-doc-" $(i+1)}}')
yum install -y ${rpm_dev_deps} ${rpm_doc_deps}

# Dependencies
yum install -y cmake make gcc-c++ rpm-build
yum install -y boost-devel $PYTHON-pytest log4cpp-devel doxygen CCfits-devel $PYTHON-numpy
yum install -y graphviz $PYTHON-sphinx

# Build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DINSTALL_TESTS=OFF -DRPM_NO_CHECK=OFF $CMAKEFLAGS ..
make $MAKEFLAGS rpm
