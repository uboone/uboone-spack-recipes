# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ubdl(Package):
    """MicroBooNE deep-learning reconstruction chain meta-repository."""

    homepage = "https://github.com/LArbys/ubdl"
    url = "https://github.com/LArbys/ubdl/archive/refs/tags/v2_me_06_03_prod_01.tar.gz"
    git = "https://github.com/LArbys/ubdl.git"

    license("UNKNOWN")

    version("trunk", branch="master")
    version("2.me.06.03.prod.01", sha256="b12086b090b0a50d1e343dbb5fe46c9f02ddd698dd264390a4101be31673dd79")

    depends_on("cxx", type="build")
    depends_on("python", type=("build", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("boost", type=("build", "link", "run"))
    depends_on("eigen", type=("build", "link", "run"))
    depends_on("opencv", type=("build", "link", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))
    depends_on("larlite", type=("build", "link", "run"))
    depends_on("larcv", type=("build", "link", "run"))

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        env.set("UBDL_BASEDIR", self.prefix)
        env.prepend_path("PATH", join_path(self.prefix, "scripts"))

        env.prepend_path("PYTHONPATH", join_path(self.prefix, "python"))
        env.prepend_path("PYTHONPATH", join_path(self.prefix, "ublarcvserver", "python"))
        env.prepend_path("PYTHONPATH", join_path(self.prefix, "ublarcvserver", "networks", "infill"))

    def url_for_version(self, version):
        return f"https://github.com/LArbys/ubdl/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
