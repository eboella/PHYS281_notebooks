# Fortran Mandelbrot module name.
FMANDEL:=fmandel

# Extension for library to be created.
EXT_SUFFIX:=$(shell python3-config --extension-suffix)

# F2PY command.
F2PY:=f2py3

# GFortran flags.
FFLAGS:=-Ofast -fpeel-loops -fprotect-parens -march=native -mtune=native \
 -fopenmp
#FFLAGS:=-Og -std=f2003 -pedantic -Wall -Wextra -Wimplicit-interface \
# -Wimplicit-procedure -Wunderflow -fimplicit-none -fbacktrace -fcheck=all -g\
# -fopenmp

# Name of c2cmap file, specifying precision declarations.
F2CMAP:=f2cmap.py

# Name of library to be created.
LIBFILE:=$(FMANDEL)$(EXT_SUFFIX)

.SUFFIXES:
.PHONY: all clean tidy

all: $(LIBFILE)

$(LIBFILE): $(FMANDEL).f90 $(F2CMAP)
	$(F2PY) --f90flags="$(FFLAGS)" -lgomp --f2cmap="$(F2CMAP)" -c\
	 -m $(FMANDEL) $<

clean:
	-rm -f $(LIBFILE) *.mod *~

tidy:
	-rm -f *.mod *~
