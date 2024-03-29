# Alexandria
[![RPM - Repository](https://github.com/astrorama/Alexandria/actions/workflows/main.yml/badge.svg?branch=develop)](https://github.com/astrorama/Alexandria/actions/workflows/main.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/astrorama/alexandria/badge)](https://www.codefactor.io/repository/github/astrorama/alexandria)

SDC-CH common library for the Euclid project

## Build Instruction

Alexandria projects uses the Elements build framework, which has to be pre-installed.
Elements framework can be found here:

https://github.com/astrorama/Elements

After Elements is installed, Alexandria can be installed using standard CMake build
instructions:

```
> git clone https://github.com/astrorama/Alexandria.git
> cd Alexandria
> mkdir build
> cd build
> cmake -DCMAKE_INSTALL_PREFIX=/usr ..
> make
> make install
```
