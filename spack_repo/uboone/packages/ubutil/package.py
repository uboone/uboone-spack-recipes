import sys, os
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Ubutil(CMakePackage):
    """MicroBooNE offline software utilities and analysis helpers."""

    homepage = "https://github.com/uboone/ubutil"
    url = "https://github.com/uboone/ubutil/archive/refs/tags/v10_20_04.tar.gz"
    git = "https://github.com/uboone/ubutil.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.21.02", sha256="aa53f8fc3950d3321fc100c7a59027e4f206b75fc66acbab8393bca6d6ba1e0a")
    version("10.20.07", sha256="836a1afd2536087153a9027257f4aa08d3fd0526c4f3efe061d18ab8f16244c5") 
    version("10.20.04", sha256="ea090d871168bd3dfd45f821360715c13a8ede245e40e4e390b00f7758de2db1")

    depends_on("cmake@3.20:", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("nufinder", type="build")
    depends_on("larfinder", type="build")
    depends_on("art", type=("build", "link", "run"))
    depends_on("cetlib", type=("build", "link", "run"))
    depends_on("cetlib-except", type=("build", "link", "run"))
    depends_on("fhicl-cpp", type=("build", "link", "run"))
    depends_on("python", type=("build", "link", "run"))
    depends_on("larbatch", type=("build", "link", "run"))

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
            self.define("CMAKE_MODULE_PATH", "%s/Modules;%s/Modules" %
                       (self.spec['nufinder'].prefix, self.spec['larfinder'].prefix)),
        ] 
        return args


    def url_for_version(self, version):
        return f"https://github.com/uboone/ubutil/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"

    def setup_run_environment(self, env):
        print("Setting up ubutil run environment.", file=sys.stderr)

        env.prepend_path("PATH", os.path.join(self.prefix, "bin"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "bin"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "python"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "lib"))
        env.set("JOBSUB_GROUP", "uboone")
        env.set("GROUP", "uboone")
        env.set("SAM_EXPERIMENT", "uboone")
