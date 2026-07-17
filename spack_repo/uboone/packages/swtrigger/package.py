import sys, os
from spack.package import *

class Swtrigger(Package):
    """MicroBooNE FEM-based beam trigger emulator and software trigger algorithms."""

    homepage = "https://github.com/uboone/fememulator"
    url = "https://github.com/uboone/fememulator/archive/refs/tags/v02_03_00.tar.gz"
    git = "https://github.com/uboone/fememulator.git"

    license("UNKNOWN")

    #version("develop", branch="master")
    version("02.03.00", sha256="47be2db01c26f7fb0af790bfed674b4b6e79f3b7f84b2b7327692358f3860668")

    depends_on("cmake", type="build")
    depends_on("gmake", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("root", type=("build", "link", "run"))

    phases = ("build", "install") 

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", "20"),
        multi=False,
        description="Use the specified C++ standard when building.",
    )


    def setup_build_environment(self, env):
        env.set("SWTRIGGER_BUILDDIR", os.path.join(self.stage.source_path, "build"))
        env.set("SWTRIGGER_INCDIR", self.stage.source_path)
        env.set("SWTRIGGER_LIBDIR", os.path.join(self.stage.source_path, "build", "lib"))
        env.unset("LARLITE_LIBDIR")
        env.unset("UBOONEDAQ_DATATYPES_INC")

    def build(self, spec, prefix):
        mkdirp(os.path.join(self.stage.source_path, 'build'))
        with working_dir(os.path.join(self.stage.source_path, 'build')):
            cmake = Executable('cmake')
            cmake('../')
            make()


    def install(self, spec, prefix):
        source_dir = os.path.join(prefix, "source")
        lib_dir = os.path.join(prefix, "lib")
        install_tree(os.path.join(self.stage.source_path, "build/lib"), lib_dir)
        install_tree(os.path.join(self.stage.source_path, "FEMBeamTrigger"),
                     os.path.join(source_dir, "FEMBeamTrigger"))
        install_tree(os.path.join(self.stage.source_path, "SWTriggerBase"),
                     os.path.join(source_dir, "SWTriggerBase"))

    def setup_run_environment(self, env):
        print("Setting up swtrigger run environment.", file=sys.stderr)

        env.set("SWTRIGGER_INCDIR", os.path.join(self.prefix, "source"))
        env.set("SWTRIGGER_LIBDIR", os.path.join(self.prefix, "lib"))

    def url_for_version(self, version):
        return f"https://github.com/uboone/fememulator/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
