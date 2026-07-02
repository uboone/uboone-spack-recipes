import sys, os
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *
from spack_repo.fnal_art.packages.fnal_github_package.package import *

class Ublite(CMakePackage, FnalGithubPackage):
    """MicroBooNE light reconstruction modules."""

    homepage = "https://github.com/uboone/ublite"
    url = "https://github.com/uboone/ublite/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/ublite.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.21.00", sha256="6cf5604f77cc51258859f0e84d4e47644ba147989e13c8d557ea8b737f201943") 
    version("10.20.05", sha256="626676fc396a3c97717374a2cec1de7de6a501f9a1ad7564e0e72c2228cf8b86")

    depends_on("cmake@3.20:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")

    depends_on("larsim", type=("build", "link", "run"))
    depends_on("ubana", type=("build", "link", "run"))

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
        return f"https://github.com/uboone/ublite/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"

    def setup_run_environment(self, env):
        print("Setting up ublite run environment.", file=sys.stderr)

        env.prepend_path("FHICL_FILE_PATH", os.path.join(self.prefix, "job"))

        env.prune_duplicate_paths("FHICL_FILE_PATH")
