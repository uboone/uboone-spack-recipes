import sys, os
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *
from spack_repo.fnal_art.packages.fnal_github_package.package import *

class Uboonedata(CMakePackage):
    """MicroBooNE uboone suite data package."""

    homepage = "https://www.github.com/uboone/uboonedata"
    url = "https://github.com/uboone/uboonedata/archive/refs/tags/v10_20_04.tar.gz"
    git = "https://github.com/uboone/uboonedata.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10_20_04", sha256="a7593637e1dfd8b07ff3b5f62f09af31e9797b522731103b7a1ad871835c534e")

    depends_on("cmake@3.20:", type="build")
    depends_on("cetmodules", type="build")
    depends_on("uboone-photon-propagation@01.01.00", type=("build", "run"))

    @cmake_preset
    def cmake_args(self):
        args = [] 
        return args

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubooonedata/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"

    def setup_run_environment(self, env):
        print("Setting up uboonedata run environment.", file=sys.stderr)

        env.prepend_path("WIRECELL_PATH", os.path.join(self.prefix, "WireCellData"))
        env.prepend_path("GXMLPATH", os.path.join(self.prefix, "genie"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "Response"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "Calibration"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "CRT"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "PandoraData"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "ppfx"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "SinglePhotonAnalysis"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "searchingfornues"))
        env.prepend_path("FW_SEARCH_PATH", os.path.join(self.prefix, "Eventgenerator/TwoBodyDecayGen"))

        env.prune_duplicate_paths("WIRECELL_PATH")
        env.prune_duplicate_paths("GXMLPATH")
        env.prune_duplicate_paths("FW_SEARCH_PATH")
