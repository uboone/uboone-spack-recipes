# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ubcv(CMakePackage):
    """MicroBooNE computer vision reconstruction modules."""

    homepage = "https://github.com/uboone/ubcv"
    url = "https://github.com/uboone/ubcv/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/ubcv.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.03", sha256="0b940fd144a3109a0c012e63311718e89968f14a8818cf7d6f3b5d800b50cb5d")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("larevt", type=("build", "link", "run"))
    depends_on("nusimdata", type=("build", "link", "run"))
    depends_on("ubevt", type=("build", "link", "run"))
    depends_on("ubreco", type=("build", "link", "run"))
    depends_on("ubsim", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubcv/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
