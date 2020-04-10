import os
import shutil
from conans import ConanFile, tools
from ghc import GHCBuild


class PythonRequires(ConanFile):
    name = "ghc-build-helper"
    version = "0.1"
    exports = "ghc.py"