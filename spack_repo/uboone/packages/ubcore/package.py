import sys, os
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *
from spack_repo.fnal_art.packages.fnal_github_package.package import *

class Ubcore(CMakePackage, FnalGithubPackage):
    """MicroBooNE framework plugins and core reconstruction utilities."""

    homepage = "https://github.com/uboone/ubcore"
    url = "https://github.com/uboone/ubcore/archive/refs/tags/v10_20_02.tar.gz"
    git = "https://github.com/uboone/ubcore.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.07", sha256="5a51fd78526a46998f56e29e315e8a5a927f7fdfab83300ed2dd539087fe7adb") 
    version("10.20.02", sha256="9350fcf4ee886d4c5f241ef0daa79689bc8188a1d13fd77283e6c6965c5f1fd1")

    depends_on("cmake@3.20:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")

    depends_on("art", type=("build", "link", "run"))
    depends_on("art-root-io", type=("build", "link", "run"))
    depends_on("canvas", type=("build", "link", "run"))
    depends_on("cetlib", type=("build", "link", "run"))
    depends_on("cetlib-except", type=("build", "link", "run"))
    depends_on("fhicl-cpp", type=("build", "link", "run"))
    depends_on("larcore", type=("build", "link", "run"))
    depends_on("lardata", type=("build", "link", "run"))
    depends_on("lardataobj", type=("build", "link", "run"))
    depends_on("nusimdata", type=("build", "link", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("ubobj", type=("build", "link", "run"))

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
        return f"https://github.com/uboone/ubcore/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"

    def setup_run_environment(self, env):
        print("Setting up ubcore run environment.", file=sys.stderr)

        env.prepend_path("FHICL_FILE_PATH", os.path.join(self.prefix, "job"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "gdml"))

        env.prune_duplicate_paths("FHICL_FILE_PATH")
        env.prune_duplicate_paths("FW_SEARCH_PATH")
