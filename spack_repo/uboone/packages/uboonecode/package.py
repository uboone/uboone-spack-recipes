# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Uboonecode(CMakePackage):
    """MicroBooNE top-level configuration and FHiCL tools package."""

    homepage = "https://github.com/uboone/uboonecode"
    url = "https://github.com/uboone/uboonecode/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/uboonecode.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.05", sha256="8941ddb191c5e3895a283e5f4f729cbbb07d3a7eb053ef13e1e24b16228c6cea")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("genie", type=("build", "link", "run"))
    depends_on("lardata", type=("build", "link", "run"))
    depends_on("nugen", type=("build", "link", "run"))
    depends_on("nurandom", type=("build", "link", "run"))
    depends_on("ubobj", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/uboonecode/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
