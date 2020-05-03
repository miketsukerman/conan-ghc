from conans import ConanFile,AutoToolsBuildEnvironment, tools
import os

class GHCConan(ConanFile):
    name = "ghc"
    version = "8.10.1"
    license = "GPL"
    author = "Michael Tsukerman <miketsukerman@gmail.com>"
    url = "https://github.com/miketsukerman/conan-ghc"
    description = "GHC is a state-of-the-art, open source, compiler and interactive environment for the functional language Haskell."
    topics = ("ghc", "haskell", "compiler")
    settings = "os", "compiler", "build_type", "arch"
    generators = "virtualrunenv"
    
    def source(self):
        if self.settings.os == "Linux":
            url = "https://downloads.haskell.org/~ghc/{}/ghc-{}-{}-deb9-linux.tar.xz".format(self.version,self.version,self.settings.arch)
        else:
            raise Exception("GHC binary does not exist for these settings")
        tools.get(url, md5='3d886e9b304d36efb8a71f706dbd8ffa')

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        os.chdir("{}/{}".format(os.getcwd(),"ghc-{}".format(self.version)))
        autotools.configure()
        autotools.install()

    def package(self):
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
