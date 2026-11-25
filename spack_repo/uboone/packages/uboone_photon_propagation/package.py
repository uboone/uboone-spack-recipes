import sys, os
from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class UboonePhotonPropagation(Package):
    """MicroBooNE photon visibility library."""

    version("01.01.00",
            url="https://scisoft.fnal.gov/scisoft/packages/uboone_photon_propagation/v01_01_00/uboone_photon_propagation-01.01.00-noarch.tar.bz2",
            sha256="1a20182ae718775077d8abc406d0458223f6329641d37f354f6301d49cd976d7")

    def install(self, spec, prefix):
        print("Building uboone_photon_propagation.", file=sys.stderr)
        install_tree(os.path.join(self.stage.source_path, "v01_01_00"), prefix)

    def setup_build_environment(self, env):
        print("Setting up uboone_photon_propagation build environment.", file=sys.stderr)
        prefix = Prefix(self.build_directory)
        env.prepend_path("FW_SEARCH_PATH", prefix)

        env.prune_duplicate_paths("FW_SEARCH_PATH")

    def setup_run_environment(self, env):
        print("Setting up uboone_photon_propagation run environment.", file=sys.stderr)

        env.prepend_path("FW_SEARCH_PATH", self.prefix)

        env.prune_duplicate_paths("FW_SEARCH_PATH")
