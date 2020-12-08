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
  if [ "$VERSION_ID" -lt 8 ]; then
    PYTHON="python"
  fi
fi

if [ "$PYTHON" == "python3" ]; then
  CMAKEFLAGS="$CMAKEFLAGS -DPYTHON_EXPLICIT_VERSION=3"
fi

# Build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DINSTALL_TESTS=OFF -DRPM_NO_CHECK=OFF $CMAKEFLAGS ..
make $MAKEFLAGS rpm
