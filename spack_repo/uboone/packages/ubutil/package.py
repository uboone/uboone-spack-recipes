from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ubutil(CMakePackage):
    """MicroBooNE offline software utilities and analysis helpers."""

    homepage = "https://github.com/uboone/ubutil"
    url = "https://github.com/uboone/ubutil/archive/refs/tags/v10_20_04.tar.gz"
    git = "https://github.com/uboone/ubutil.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.04", sha256="ea090d871168bd3dfd45f821360715c13a8ede245e40e4e390b00f7758de2db1")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")
    depends_on("art", type=("build", "link", "run"))
    depends_on("cetlib", type=("build", "link", "run"))
    depends_on("cetlib-except", type=("build", "link", "run"))
    depends_on("fhicl-cpp", type=("build", "link", "run"))
    depends_on("python", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubutil/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
