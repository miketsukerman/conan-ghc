from conans import ConanFile, CMake, tools
import os, subprocess

class HelloTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    requires =   "ghc/8.8.3"

    def build(self):
        currentDirectory = os.path.dirname(os.path.realpath(__file__))
        self.run("ghc -o example {}{}example.hs".format(currentDirectory,os.sep))

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            output = subprocess.check_output([".{}example".format(os.sep)])
            if not b'Hello, World!\n' in output:
                raise Exception(output)