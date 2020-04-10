import os
import shutil
from conans import ConanFile, tools
from conans.client.tools.oss import args_to_string
from conans.util.files import normalize, save
from conans.client.build.compiler_flags import libcxx_flag, libcxx_define, format_defines
from conans.client.build.cppstd_flags import cppstd_flag, cppstd_from_settings
from conans.errors import ConanException


class GHCBuild(object):
    def __init__(self, conanfile):
        self._conanfile = conanfile
        self._arch = self._ss("arch")
        self._os = self._ss("os")
        self._compiler = self._ss("compiler")
        self._compiler_version = self._ss("compiler.version")
        self._compiler_libcxx = self._ss("compiler.libcxx")
        self._compiler_cppstd = self._ss("compiler.cppstd")
        self._build_type = self._ss("build_type")
        self._compiler_runtime = self._ss("compiler.runtime")

    def setup(self, args=None):
        args = args or []
        command = "ghc -threaded --make Setup" + " ".join(arg for arg in args)   
        with tools.vcvars(self._conanfile.settings):
            self._conanfile.run(command, run_environment=True)

    def configure(self, user=None, prefix=None):
        command = ".{}Setup configure ".format(os.sep)
        if user:
            command += "--user "
        if prefix: 
            command += "--prefix={} ".format(prefix)            
        with tools.vcvars(self._conanfile.settings):
            self._conanfile.run(command, run_environment=True)

    def build(self, args=None):
        args = args or []
        command = ".{}Setup build ".format(os.sep) + " ".join(arg for arg in args)
        with tools.vcvars(self._conanfile.settings):
            self._conanfile.run(command, run_environment=True)

    def build(self, args=None):
        args = args or []
        command = ".{}Setup install ".format(os.sep) + " ".join(arg for arg in args)
        with tools.vcvars(self._conanfile.settings):
            self._conanfile.run(command, run_environment=True)

    def _run(self, command):
        try:
            self._conanfile.run(command)
        except Exception as e:
            raise ConanException("Error running: {} ({})".format(command, str(e)))

    def _ss(self, setname):
        """safe setting"""
        return self._conanfile.settings.get_safe(setname)

    def _so(self, setname):
        """safe option"""
        return self._conanfile.options.get_safe(setname)