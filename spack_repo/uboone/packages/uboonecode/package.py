import sys, os
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *
from spack_repo.fnal_art.packages.fnal_github_package.package import *

def sanitize(env):
    for var in (
        "PATH",
        "MANPATH",
        "ACLOCAL_PATH",
        "PKG_CONFIG_PATH",
        "PYTHONPATH",
        "C_INCLUDE_PATH",
        "CPLUS_INCLUDE_PATH",
        "CPATH",
        "ROOT_INCLUDE_PATH",
        "ROOT_LIBRARY_PATH",
        "CET_PLUGIN_PATH",
        "SPACK_LOADED_HASHES",
        "XLOCALEDIR",
        "WIRECELL_PATH",
        "FW_SEARCH_PATH",
        "CMAKE_PREFIX_PATH"
    ):
        env.prune_duplicate_paths(var)

class Uboonecode(CMakePackage, FnalGithubPackage):
    """MicroBooNE top-level configuration and FHiCL tools package."""

    homepage = "https://github.com/uboone/uboonecode"
    url = "https://github.com/uboone/uboonecode/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/uboonecode.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.21.00", sha256="bf144e83d783c99665588bd7677b5a5d827563747940f58b0f2eb9fceaaa9817") 
    version("10.20.05", sha256="8941ddb191c5e3895a283e5f4f729cbbb07d3a7eb053ef13e1e24b16228c6cea")

    depends_on("cmake@3.20:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")

    depends_on("genie", type=("build", "link", "run"))
    depends_on("larsoft", type=("build", "link", "run"))
    depends_on("nugen", type=("build", "link", "run"))
    depends_on("nurandom", type=("build", "link", "run"))
    depends_on("ubcrt", type=("build", "link", "run"))
    depends_on("ubcv", type=("build", "link", "run"))
    depends_on("ublite", type=("build", "link", "run"))
    depends_on("uboonedata", type=("build", "run"))
    depends_on("ubutil", type=("build", "run"))

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    @cmake_preset
    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("CMAKE_MODULE_PATH", "%s/Modules;%s/Modules" %
                       (self.spec['nufinder'].prefix, self.spec['larfinder'].prefix)),
        ] 
        return args


    def url_for_version(self, version):
        return f"https://github.com/uboone/uboonecode/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"

    def setup_run_environment(self, env):
        print("Setting up uboonecode run environment.", file=sys.stderr)
        
        env.prepend_path("WIRECELL_PATH", os.path.join(self.spec['wire-cell-toolkit'].prefix, "share/wirecell"))
        env.prepend_path("FHICL_FILE_PATH", os.path.join(self.prefix, "job"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "scripts"))
        
        sanitize(env)
