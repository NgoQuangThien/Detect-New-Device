#!/bin/bash

#
sudo rpm -i centos-release-scl/dependencies/centos-release-scl-rh-2-3.el7.centos.noarch.rpm
sudo rpm -i centos-release-scl/centos-release-scl-2-3.el7.centos.noarch.rpm

#
sudo rpm -i llvm-toolset-7/dependencies/scl-utils-20130529-19.rpm
sudo rpm -i llvm-toolset-7/dependencies/llvm-toolset-7-runtime-5.0.1.rpm
sudo rpm -i llvm-toolset-7/dependencies/devtoolset-7-runtime-7.1.rpm
sudo rpm -i llvm-toolset-7/dependencies/mpfr-3.1.1-4.rpm
sudo rpm -i llvm-toolset-7/dependencies/llvm-toolset-7-compiler-rt-5.0.1-2.rpm
sudo rpm -i llvm-toolset-7/dependencies/llvm-toolset-7-libomp-5.0.1.rpm
sudo rpm -i llvm-toolset-7/dependencies/llvm-toolset-7-llvm-libs-5.0.1-8.rpm
sudo rpm -i llvm-toolset-7/dependencies/llvm-toolset-7-llvm-5.0.1-8.rpm
sudo rpm -i llvm-toolset-7/dependencies/python-backports-1.0-8.rpm
sudo rpm -i llvm-toolset-7/dependencies/python-ipaddress-1.0.16-2.rpm
sudo rpm -i llvm-toolset-7/dependencies/python-backports-ssl_match_hostname-3.5.0.1.rpm
sudo rpm -i llvm-toolset-7/dependencies/python-setuptools-0.9.8-7.rpm
sudo rpm -i llvm-toolset-7/dependencies/llvm-toolset-7-python2-lit-0.5.1.rpm
sudo rpm -i llvm-toolset-7/dependencies/devtoolset-7-libstdc++-devel-7.3.1.rpm
sudo rpm -i llvm-toolset-7/dependencies/kernel-headers-3.10.0-1160.45.rpm
sudo rpm -i llvm-toolset-7/dependencies/glibc-headers-2.17-325.rpm
sudo rpm -i llvm-toolset-7/dependencies/glibc-devel-2.17-325.rpm
sudo rpm -i llvm-toolset-7/dependencies/libmpc-1.0.1-3.rpm
sudo rpm -i llvm-toolset-7/dependencies/devtoolset-7-binutils-2.28-11.el7.x86_64.rpm
sudo rpm -i llvm-toolset-7/dependencies/devtoolset-7-gcc-7.3.1.rpm
sudo rpm -i llvm-toolset-7/dependencies/devtoolset-7-gcc-c++-7.3.1.rpm
sudo rpm -i llvm-toolset-7/dependencies/llvm-toolset-7-clang-libs-5.0.1-4.rpm
sudo rpm -i llvm-toolset-7/dependencies/llvm-toolset-7-clang-5.0.1-4.rpm
sudo rpm -i llvm-toolset-7/dependencies/llvm-toolset-7-lldb-5.0.1-4.rpm

sudo rpm -i llvm-toolset-7/llvm-toolset-7-5.0.1-4.el7.x86_64.rpm

#
sudo rpm -i xdp/elfutils-libelf-devel-0.176-5.el7.x86_64.rpm
sudo rpm -i xdp/bpftool-3.10.0-1160.45.1.el7.x86_64.rpm

sudo cp xdp/stubs-32.h /usr/include/gnu/

#
sudo rpm -i kernel/kernel-ml-5.15.3-1.el7.elrepo.x86_64.rpm

#
cd ../kernel_program/
sudo bash chmod_x.sh

#
cd ../userspace_program/
sudo bash install.sh
