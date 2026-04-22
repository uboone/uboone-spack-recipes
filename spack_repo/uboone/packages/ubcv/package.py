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
    version("10.20.05", sha256="eed26a67ae6586f555d47ffad2710176c844c4532c1ef5af4ca4b98a2a3f2920")

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
