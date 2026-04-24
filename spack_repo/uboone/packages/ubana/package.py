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
    version("10.20.03", sha256="9522cf3b23dc77972730c4b5d06af820ef7b0bd588599a918ee0429ec4f4ac05")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("eigen", type=("build", "link", "run"))
    depends_on("larana", type=("build", "link", "run"))
    depends_on("larpandora", type=("build", "link", "run"))
    depends_on("ubcv", type=("build", "link", "run"))
    depends_on("ubraw", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubana/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
