# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ubana(CMakePackage):
    """MicroBooNE analysis modules."""

    homepage = "https://github.com/uboone/ubana"
    url = "https://github.com/uboone/ubana/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/ubana.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.05", sha256="019e329075b3c8d5616cf3ce1d84ff663a4441ed42240066459612c2dd655e6e")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("eigen", type=("build", "link", "run"))
    depends_on("larana", type=("build", "link", "run"))
    depends_on("larpandora", type=("build", "link", "run"))
    depends_on("femulator", type=("build", "link", "run"))
    depends_on("ubcv", type=("build", "link", "run"))
    depends_on("ubreco", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubana/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
