#!/bin/bash
set -ex

# Platform-specific configuration
source /etc/os-release

# On CentOS, install EPEL
if [ "$ID" == "centos" ]; then
  yum install -y epel-release
  # Need powertools on CentOS8
  if [ "$VERSION_ID" -ge 8 ]; then
    sed -i "s/enabled=0/enabled=1/" /etc/yum.repos.d/CentOS-PowerTools.repo
  fi
fi

# Astrorama repository
cat >/etc/yum.repos.d/astrorama.repo <<EOF
[bintray--astrorama-fedora]
name=bintray--astrorama-fedora
baseurl=https://dl.bintray.com/astrorama/travis/master/${ID}/\$releasever/\$basearch
gpgcheck=0
repo_gpgcheck=0
enabled=1
EOF

# Develop repository if not building for master
if [ "${GITHUB_REF#refs/heads/}" != "master" ]; then
  cat >>/etc/yum.repos.d/astrorama.repo <<EOF
[bintray--astrorama-fedora-develop]
name=bintray--astrorama-fedora-develop
baseurl=https://dl.bintray.com/astrorama/travis/develop/${ID}/\$releasever/\$basearch
gpgcheck=0
repo_gpgcheck=0
enabled=1
EOF
fi
