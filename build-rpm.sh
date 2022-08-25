#!/bin/bash
#
# This can be run as:
# $ OS_TYPE=fedora OS_VERSION=36
# $ podman run --privileged -ti --replace --name "builder${OS_VERSION}" --volume "$(pwd):/src" "${OS_TYPE}:${OS_VERSION}" bash "/src/build-rpm.sh"
#
# An optional parameter can be passed to be used as the rpm release number, which should be increased when
# the rpm is re-built for a given OS (i.e. after a gcc update)
#
# The artifacts can be copied out as
# $ podman cp "builder${OS_VERSION}:/build/Packages/RPM/RPMS/x86_64" "./packages${OS_VERSION}"
#
set -ex

RELEASE=${1:-1}

cd /src

BASEURL=https://raw.githubusercontent.com/astrorama/actions/v3

# Repositories
curl ${BASEURL}/setup-dependencies/setup-repositories.sh | bash

# Dependencies
curl ${BASEURL}/setup-dependencies/install-dependencies.sh | bash -s /src/.github/workflows/dependencies.txt

# Build rpm
curl ${BASEURL}/elements-build-rpm/build-rpm.sh | bash -s /build "${RELEASE}"

