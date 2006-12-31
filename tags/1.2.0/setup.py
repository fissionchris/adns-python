#!/usr/bin/env python

"""Setup script for the adns module distribution."""

import os, sys
from distutils.core import setup
from distutils.extension import Extension

# You probably don't have to do anything past this point. If you
# do, please mail me the configuration for your platform. Don't
# forget to include the value of sys.platform and os.name.

include_dirs = []
library_dirs = []
runtime_library_dirs = []
extra_objects = []

if os.name == "posix": # most Linux/UNIX platforms
    libraries = ["adns"]
else:
    raise "UnknownPlatform", "sys.platform=%s, os.name=%s" % \
          (sys.platform, os.name)
    
long_description = \
"""adns-python is a Python module that interfaces to the adns asynchronous
resolver library.

http://www.gnu.org/software/adns/
"""
setup (# Distribution meta-data
    name = "adns-python",
    version = "1.2.0",
    description = "An interface to GNU adns",
    author = "Andy Dustman",
    author_email = "farcepest@gmail.com",
    url = "http://code.google.com/p/adns-python",
    download_url = "http://adns-python.googlecode.com/files/adns-python-1.2.0.tar.gz",
    long_description=long_description,
    license = "GPL",
    classifiers = [
    "Development Status :: 6 - Mature",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: POSIX",
    "Topic :: Internet :: Name Service (DNS)",
    "Topic :: Software Development :: Libraries",
    ],

    # Description of the modules and packages in the distribution
    
    py_modules = ["DNSBL", "ADNS"],
    
    ext_modules = [
    Extension(
    name='adns',
    sources=['adnsmodule.c'],
    include_dirs=include_dirs,
    library_dirs=library_dirs,
    runtime_library_dirs=runtime_library_dirs,
    libraries=libraries,
    extra_objects=extra_objects,
    )],
)
