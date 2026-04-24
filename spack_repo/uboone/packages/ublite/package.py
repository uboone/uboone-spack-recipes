# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ublite(CMakePackage):
    """MicroBooNE light reconstruction modules."""

    homepage = "https://github.com/uboone/ublite"
    url = "https://github.com/uboone/ublite/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/ublite.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.03", sha256="1cb8acd6a866651793059b255592d598b78cb7ab4960a7b7cc4ea9baceec76e9")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("larsim", type=("build", "link", "run"))
    depends_on("ubana", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ublite/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
