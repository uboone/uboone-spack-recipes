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

    @cmake_preset
    def cmake_args(self):
        args = [] 
        return args

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubooonedata/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"

