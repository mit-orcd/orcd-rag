-- -*- lua -*-
--

whatis([[Name : vasp]])
whatis([[Version : 6.4.3]])
whatis([[Target : x86_64]])
whatis([[Short description : The Vienna Ab initio Simulation Package (VASP) is a computer program for atomic scale materials modelling, e.g. electronic structure calculations and quantum-mechanical molecular dynamics, from first principles.]])

local base = pathJoin(os.getenv("HOME"),"software/VASP/vasp.6.4.3") 

depends_on("gcc/12.2.0")
depends_on("openmpi/4.1.4")

prepend_path("LD_LIBRARY_PATH","/orcd/software/core/001/spack/pkg/openblas/0.3.26/ro5tivv/lib:/orcd/software/core/001/spack/pkg/fftw/3.3.10/dg7y4ph/lib:/orcd/software/core/001/spack/pkg/netlib-scalapack/2.2.0/ff5iskg/./lib")
prepend_path("PATH", pathJoin(base,"bin/"), ":")