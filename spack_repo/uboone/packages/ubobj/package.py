from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ubobj(CMakePackage):
    """MicroBooNE event data object definitions."""

    homepage = "https://github.com/uboone/ubobj"
    url = "https://github.com/uboone/ubobj/archive/refs/tags/v10_16_00.tar.gz"
    git = "https://github.com/uboone/ubobj.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.16.00", sha256="b95ab4ceea7592dd318f19087cad3d0d997fd41fd05b18c6c3c07715ecd70db3")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("canvas", type=("build", "link", "run"))
    depends_on("cetlib-except", type=("build", "link", "run"))
    depends_on("lardataobj", type=("build", "link", "run"))
    depends_on("nusimdata", type=("build", "link", "run"))
    depends_on("root", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubobj/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
