all:
	@echo "make package - to build the conan package for fpp"

package:
	conan create --build missing . 

.PHONY: package