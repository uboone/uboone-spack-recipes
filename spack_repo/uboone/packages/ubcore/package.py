# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ubcore(CMakePackage):
    """MicroBooNE framework plugins and core reconstruction utilities."""

    homepage = "https://github.com/uboone/ubcore"
    url = "https://github.com/uboone/ubcore/archive/refs/tags/v10_20_02.tar.gz"
    git = "https://github.com/uboone/ubcore.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.02", sha256="9350fcf4ee886d4c5f241ef0daa79689bc8188a1d13fd77283e6c6965c5f1fd1")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("art", type=("build", "link", "run"))
    depends_on("art-root-io", type=("build", "link", "run"))
    depends_on("canvas", type=("build", "link", "run"))
    depends_on("cetlib", type=("build", "link", "run"))
    depends_on("cetlib-except", type=("build", "link", "run"))
    depends_on("fhicl-cpp", type=("build", "link", "run"))
    depends_on("larcore", type=("build", "link", "run"))
    depends_on("lardata", type=("build", "link", "run"))
    depends_on("lardataobj", type=("build", "link", "run"))
    depends_on("nusimdata", type=("build", "link", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("ubobj", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubcore/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
