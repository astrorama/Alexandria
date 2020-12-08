#!/bin/bash
set -ex

# Platform-specific configuration
source /etc/os-release

# Figure out the python version to use
PYTHON="python3"
if [ "$ID" == "fedora" ] && [ "$VERSION_ID" -lt 30 ]; then
  PYTHON="python"
elif [ "$ID" == "centos" ] && [ "$VERSION_ID" -lt 8 ]; then
  PYTHON="python"
fi

# From the CMakeLists.txt, retrieve the list of dependencies
cmake_deps=$(grep -oP 'elements_project\(\S+\s+\S+ USE \K(\S+ \S+)*(?=\))' CMakeLists.txt)
rpm_dev_deps=$(echo ${cmake_deps} | awk '{for(i=1;i<NF;i+=2){print $i "-devel-" $(i+1)}}')
rpm_doc_deps=$(echo ${cmake_deps} | awk '{for(i=1;i<NF;i+=2){print $i "-doc-" $(i+1)}}')
yum install -y ${rpm_dev_deps} ${rpm_doc_deps}

# Common dependencies
yum install -y cmake make gcc-c++ rpm-build

# Install explicit dependency list
xargs -a "$1" yum install -y

# Install python dependencies with the proper prefix
sed -e "s/^/$PYTHON-/" "$2" | xargs yum install -y
