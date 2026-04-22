# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Ubcrt(CMakePackage):
    """MicroBooNE CRT reconstruction and filtering modules."""

    homepage = "https://github.com/uboone/ubcrt"
    url = "https://github.com/uboone/ubcrt/archive/refs/tags/v10_20_05.tar.gz"
    git = "https://github.com/uboone/ubcrt.git"

    license("Apache-2.0")

    version("develop", branch="develop")
    version("10.20.05", sha256="60f7c858a5d24964cebd6def29547fe8b8a2fd41d627cb5b0f2f219bd8cfc95a")

    depends_on("cmake@3.20:", type="build")
    depends_on("cxx", type="build")
    depends_on("cetmodules", type="build")

    depends_on("art", type=("build", "link", "run"))
    depends_on("art-root-io", type=("build", "link", "run"))
    depends_on("artdaq-core", type=("build", "link", "run"))
    depends_on("gallery", type=("build", "link", "run"))
    depends_on("ifdh-art", type=("build", "link", "run"))
    depends_on("larcore", type=("build", "link", "run"))
    depends_on("larcorealg", type=("build", "link", "run"))
    depends_on("lardata", type=("build", "link", "run"))
    depends_on("lardataobj", type=("build", "link", "run"))
    depends_on("larevt", type=("build", "link", "run"))
    depends_on("larpandora", type=("build", "link", "run"))
    depends_on("messagefacility", type=("build", "link", "run"))
    depends_on("nurandom", type=("build", "link", "run"))
    depends_on("nusimdata", type=("build", "link", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("ubevt", type=("build", "link", "run"))
    depends_on("ubobj", type=("build", "link", "run"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/ubcrt/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
