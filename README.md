# Alexandria
[![Build Status](https://travis-ci.org/astrorama/Alexandria.svg?branch=deuclidized%2F2.10)](https://travis-ci.org/astrorama/Alexandria)

SDC-CH common library for the Euclid project

## Build Instruction

Alexandria projects uses the Elements build framework, which has to be pre-installed.
Elements framework can be found here:

https://github.com/degauden/Elements

After Elements is installed, Alexandria can be installed using standard CMake build
instructions:

```
> git clone https://github.com/nikoapos/Alexandria.git
> cd Alexandria
> mkdir build
> cd build
> cmake -DCMAKE_INSTALL_PREFIX=/usr ..
> make
> make install
```
