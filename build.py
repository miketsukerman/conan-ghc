import os
import subprocess
import sys


def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Failed command: %s" % cmd)


def main(argv):
    run("conan create ghc haskell/testing")
    run("conan create ghc-build haskell/testing")


if __name__ == '__main__':
    main(sys.argv[1:])