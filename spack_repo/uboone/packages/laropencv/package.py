# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Laropencv(Package):
    """LArOpenCV image-processing framework for liquid argon TPC data."""

    homepage = "https://github.com/NevisUB/LArOpenCV"
    git = "https://github.com/NevisUB/LArOpenCV.git"

    license("UNKNOWN")

    version("2.me.06.03.prod.01", commit="18f1d18dc42afe22d087b9e1c0914adaa641c4d5")

    depends_on("gmake", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("larlite", type=("build", "link", "run"))
    depends_on("opencv@:3+imgproc+imgcodecs", type=("build", "link", "run"))
    depends_on("python@3:", type=("build", "link", "run"))
    depends_on("py-numpy", type=("build", "run"))

    phases = ("build", "install")

    def setup_build_environment(self, env):
        base = self.stage.source_path
        larlite_prefix = self.spec["larlite"].prefix

        env.set("LAROPENCV_BASEDIR", base)
        env.set("LAROPENCV_IMAGECLUSTERDIR", join_path(base, "ImageCluster"))

        env.set("LARLITE_BASEDIR", larlite_prefix)
        env.set("LARLITE_COREDIR", join_path(larlite_prefix, "core"))
        env.set("LARLITE_USERDEVDIR", join_path(larlite_prefix, "UserDev"))
        # Redirect lib output to a writeable location inside the stage
        env.set("LARLITE_LIBDIR", join_path(base, "lib"))

        env.set("OPENCV_INCDIR", self.spec["opencv"].prefix.include)
        opencv_lib = self.spec["opencv"].prefix.lib
        env.set("OPENCV_LIBDIR", opencv_lib)
        env.prepend_path("LD_LIBRARY_PATH", opencv_lib)

        env.set("LAROPENCV_PYTHON_VERSION", str(self.spec["python"].version.up_to(1)))
        env.set("LAROPENCV_PYTHON", "python%s" % str(self.spec["python"].version.up_to(1)))

        env.prepend_path("PATH", self.spec["python"].prefix.bin)
        env.prepend_path("PATH", join_path(larlite_prefix, "bin"))
        env.prepend_path("PATH", join_path(base, "bin"))

        mkdirp(join_path(base, "lib"))

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set("LAROPENCV_BASEDIR", self.prefix)
        env.set("LAROPENCV_IMAGECLUSTERDIR", join_path(self.prefix, "ImageCluster"))

    def setup_run_environment(self, env):
        env.set("LAROPENCV_BASEDIR", self.prefix)
        env.set("LAROPENCV_IMAGECLUSTERDIR", join_path(self.prefix, "ImageCluster"))

        env.prepend_path("PATH", join_path(self.prefix, "bin"))
        env.prepend_path("LD_LIBRARY_PATH", join_path(self.prefix, "lib"))
        env.prepend_path("PYTHONPATH", join_path(self.prefix, "python"))
