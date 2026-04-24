# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ubreco(CMakePackage):
    """MicroBooNE reconstruction modules."""

    homepage = "https://github.com/uboone/ubreco"
    url = "https://github.com/uboone/ubreco/archive/refs/tags/v10_20_03.tar.gz"
    git = "https://github.com/uboone/ubreco.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.03", sha256="dbec8ed66aa9fcbe0121da70711b0274ed29b7207434476e5c6d3bc49fd3f01a")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("eigen", type=("build", "link", "run"))
    depends_on("larreco", type=("build", "link", "run"))
    depends_on("larpandora", type=("build", "link", "run"))
    depends_on("nugen", type=("build", "link", "run"))
    depends_on("nutools", type=("build", "link", "run"))
    depends_on("ubsim", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubreco/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"

    def cmake_args(self):
        args = ["-Dubreco_FW_DIR=fw"]
        return args

