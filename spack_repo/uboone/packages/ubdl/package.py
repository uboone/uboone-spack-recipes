import sys, os
from spack.package import *


class Ubdl(Package):
    """MicroBooNE deep-learning reconstruction chain meta-repository."""

    homepage = "https://github.com/LArbys/ubdl"
    url = "https://github.com/LArbys/ubdl/archive/refs/tags/v2_me_06_03_prod_01.tar.gz"
    git = "https://github.com/LArbys/ubdl.git"

    license("UNKNOWN")

    phases = ("build", "install")

    version("trunk", branch="master")
    version("2.me.06.03.prod.01", tag="v2_me_06_03_prod_01", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")
    depends_on("cmake", type="build")
    depends_on("python", type=("build", "run"))
    depends_on("root", type=("build", "link", "run"))
    depends_on("boost", type=("build", "link", "run"))
    depends_on("eigen", type=("build", "link", "run"))
    depends_on("opencv", type=("build", "link", "run"))
    depends_on("nlohmann-json", type=("build", "link", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-pyzmq", type=("build", "run"))

    #def patch(self):
    #    filter_file('setup cmake v3_27_4', '', 'buildall_fnal_py3.sh')

    def setup_build_environment(self, env):

        env.set("UBDL_BASEDIR", self.stage.source_path)
        env.set("OPENCV_INCDIR", self.spec["opencv"].prefix.include)
        opencv_lib = self.spec["opencv"].prefix.lib
        if not os.path.exists(opencv_lib):
            opencv_lib = self.spec["opencv"].prefix.lib64
        if not os.path.exists(opencv_lib):
            print("OpenCV library directory not found.")
            sys.exit(1)
        env.set("OPENCV_LIBDIR", opencv_lib)
        cxx = ''
        if self.spec.compiler.name == "gcc":
            cxx = "g++"
        elif self.spec.compiler.name == "clang":
            cxx = "clang++"
        else:
            print("Unknown compiler %s" % self.spec.compiler.name)
            sys.exit(1)
    
        # Larlite
        
        larlite_basedir = os.path.join(self.stage.source_path, 'larlite')
        env.set("LARLITE_BASEDIR", larlite_basedir)
        env.set("LARLITE_INCDIR", os.path.join(larlite_basedir, "build/installed/include"))
        env.set("LARLITE_LIBDIR", os.path.join(larlite_basedir, "build/installed/lib"))
        env.set("LARLITE_COREDIR", os.path.join(larlite_basedir, "larlite"))
        env.prepend_path("PATH", os.path.join(larlite_basedir, "bin"))
        env.prepend_path("CMAKE_PREFIX_PATH", os.path.join(larlite_basedir, "build/installed/lib/cmake/larlite"))
        env.set("LARLITE_CXX", cxx)
        env.set("ENABLE_LARLITE_ALIAS", "1")
        env.set("LARLITE_ROOT6", "1")
        env.set("USER_MODULE", "")

        # Geo2D

        geo2d_basedir = os.path.join(self.stage.source_path, 'Geo2D')
        env.set("GEO2D_BASEDIR", geo2d_basedir)
        env.set("GEO2D_INCDIR", geo2d_basedir)
        env.set("GEO2D_LIBDIR", os.path.join(geo2d_basedir, "lib"))
        env.set("GEO2D_BINDIR", os.path.join(geo2d_basedir, "bin"))
        env.set("GEO2D_COREDIR", os.path.join(geo2d_basedir, "Geo2D/Core"))
        env.set("GEO2D_CXX", cxx)
        env.set("GEO2D_PYTHON", "python")
        env.set("ENABLE_GEO2D_ALIAS", "1")
        env.set("GEO2D_ROOT6", "1")

        # LArOpenCV

        laropencv_basedir = os.path.join(self.stage.source_path, 'LArOpenCV')
        env.set("LAROPENCV_BASEDIR", laropencv_basedir)
        env.set("LAROPENCV_BUILDDIR", os.path.join(laropencv_basedir, "build"))
        env.set("LAROPENCV_IMAGECLUSTERDIR", os.path.join(laropencv_basedir, "ImageCluster"))
        env.set("LAROPENCV_PYTHON", "python")

        # Larcv

        larcv_basedir = os.path.join(self.stage.source_path, 'larcv')
        env.set("LARCV_BASEDIR", larcv_basedir)
        env.set("LARCV_COREDIR", os.path.join(larcv_basedir, "larcv/core"))
        env.set("LARCV_APPDIR", os.path.join(larcv_basedir, "larcv/app"))
        env.set("LARCV_LIBDIR", os.path.join(larcv_basedir, "build/installed/lib"))
        env.set("LARCV_INCDIR", os.path.join(larcv_basedir, "build/installed/include"))
        env.set("LARCV_BINDIR", os.path.join(larcv_basedir, "bin"))
        env.prepend_path("PATH", os.path.join(larcv_basedir, "bin"))
        env.prepend_path("PATH", os.path.join(larcv_basedir, "mac"))
        env.prepend_path("CMAKE_PREFIX_PATH", os.path.join(larcv_basedir, "build/installed/lib/cmake/larcv"))
        env.prepend_path("CMAKE_PREFIX_PATH",
                         "{0}/lib/python{1}/site-packages/torch".format(
                             self.spec["py-torch"].prefix,
                             self.spec["python"].version.up_to(2)))
        env.set("LARCV_CXX", cxx)
        env.set("LARCV_VERSION", "1")
        env.set("LARCV_OPENCV", "1")
        env.set("LARCV_NUMPY", "1")
        env.set("LARCV_LIBTORCH", "1")
        env.set("LARCV_ANN", "1")
        env.set("ANN_INCDIR", os.path.join(larcv_basedir, "larcv/app/ann_1.1.2/include"))
        env.set("ANN_LIBDIR", os.path.join(larcv_basedir, "larcv/app/ann_1.1.2/lib"))
        env.set("LARCV_ROOT6", "1")
        env.set("LARCV_PYTHON", "python")
        env.set("NLOHMANN_JSON_DIR", self.spec["nlohmann-json"].prefix)
        env.set("NLOHMANN_JSON_INC", self.spec["nlohmann-json"].prefix.include)


        # Cilantro

        cilantro_basedir = os.path.join(self.stage.source_path, 'cilantro')
        env.set("CILANTRO_BASEDIR", cilantro_basedir)
        env.set("CILANTRO_INC_DIR", os.path.join(cilantro_basedir, "include"))
        env.set("CILANTRO_LIB_DIR", os.path.join(cilantro_basedir, "build"))
        env.set("CILANTRO_BIN_DIR", os.path.join(cilantro_basedir, "bin"))
        env.prepend_path("PATH", os.path.join(cilantro_basedir, "bin"))

        # Ublarcvapp

        ublarcvapp_basedir = os.path.join(self.stage.source_path, 'ublarcvapp')
        env.set("UBLARCVAPP_BASEDIR", ublarcvapp_basedir)
        env.set("UBLARCVAPP_INCDIR", os.path.join(ublarcvapp_basedir, "build/include"))
        env.set("UBLARCVAPP_LIBDIR", os.path.join(ublarcvapp_basedir, "build/lib"))
        env.prepend_path("PATH", os.path.join(ublarcvapp_basedir, "bin"))
        env.prepend_path("CMAKE_PREFIX_PATH", os.path.join(ublarcvapp_basedir, "build/lib/cmake/ublarcvapp"))

        # Larflow

        larflow_basedir = os.path.join(self.stage.source_path, 'larflow')
        env.set("LARFLOW_BASEDIR", larflow_basedir)
        env.set("LARFLOW_BUILDDIR", os.path.join(larflow_basedir, "build"))
        env.set("LARFLOW_LIBDIR", os.path.join(larflow_basedir, "build/lib"))
        env.set("LARFLOW_INCDIR", os.path.join(larflow_basedir, "build/include"))
        env.set("PYTORCH_LARFLOW_BASEDIR", os.path.join(larflow_basedir, "pytorch-larflow"))
        env.set("LARFLOW_MODELDIR", os.path.join(larflow_basedir, "models"))
        env.set("LARFLOW_SPARSEDIR", os.path.join(larflow_basedir, "sparse_larflow"))
        env.set("LARFLOW_UTILSDIR", os.path.join(larflow_basedir, "utils"))

        
    def build(self, spec, prefix):

        # Larlite
        
        mkdirp(os.path.join(self.stage.source_path, 'larlite/build'))
        with working_dir(os.path.join(self.stage.source_path, 'larlite/build')):
            cmake = Executable('cmake')
            cmake('-DUSE_PYTHON3=ON', '../')
            make('install')

        # Geo2D
            
        with working_dir(os.path.join(self.stage.source_path, 'Geo2D')):
            make()

        # LArOpenCV
            
        with working_dir(os.path.join(self.stage.source_path, 'LArOpenCV')):
            make()

        # Larcv

        mkdirp(os.path.join(self.stage.source_path, 'larcv/build'))
        with working_dir(os.path.join(self.stage.source_path, 'larcv/build')):
            cmake = Executable('cmake')
            cmake('-DUSE_PYTHON3=ON', '-DUSE_OPENCV=ON', '-DUSE_TORCH=ON', '../')
            make('install')

        # Cilantro

        mkdirp(os.path.join(self.stage.source_path, 'cilantro/build'))
        with working_dir(os.path.join(self.stage.source_path, 'cilantro/build')):
            cmake = Executable('cmake')
            cmake('../')
            make()

        # Ublarcvapp

        mkdirp(os.path.join(self.stage.source_path, 'ublarcvapp/build'))
        with working_dir(os.path.join(self.stage.source_path, 'ublarcvapp/build')):
            cmake = Executable('cmake')
            cmake('-DUSE_OPENCV=ON', '../')
            make('install')

        # Larflow

        mkdirp(os.path.join(self.stage.source_path, 'larflow/build'))
        with working_dir(os.path.join(self.stage.source_path, 'larflow/build')):
            cmake = Executable('cmake')
            cmake('-DUSE_PYTHON3=ON', '../')
            make('install')

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        
        env.set("UBDL_BASEDIR", self.prefix)
        env.set("OPENCV_INCDIR", self.spec["opencv"].prefix.include)
        opencv_lib = self.spec["opencv"].prefix.lib
        if not os.path.exists(opencv_lib):
            opencv_lib = self.spec["opencv"].prefix.lib64
        if not os.path.exists(opencv_lib):
            print("OpenCV library directory not found.")
            sys.exit(1)
        env.set("OPENCV_LIBDIR", opencv_lib)
        env.prepend_path("PATH", os.path.join(self.prefix, "scripts"))

        # Larlite

        larlite_basedir = os.path.join(self.prefix, 'larlite')
        env.set("LARLITE_BASEDIR", larlite_basedir)
        env.set("LARLITE_INCDIR", os.path.join(larlite_basedir, "build/installed/include"))
        env.set("LARLITE_LIBDIR", os.path.join(larlite_basedir, "build/installed/lib"))
        env.set("LARLITE_COREDIR", os.path.join(larlite_basedir, "larlite"))
        env.prepend_path("PATH", os.path.join(larlite_basedir, "bin"))
        #env.prepend_path("CMAKE_PREFIX_PATH", os.path.join(larlite_basedir, "build/installed/lib/cmake/larlite"))

        # Geo2D

        geo2d_basedir = os.path.join(self.prefix, 'Geo2D')
        env.set("GEO2D_BASEDIR", geo2d_basedir)
        env.set("GEO2D_INCDIR", geo2d_basedir)
        env.set("GEO2D_LIBDIR", os.path.join(geo2d_basedir, "lib"))
        env.set("GEO2D_BINDIR", os.path.join(geo2d_basedir, "bin"))
        env.set("GEO2D_COREDIR", os.path.join(geo2d_basedir, "Geo2D/Core"))

        # LArOpenCV

        laropencv_basedir = os.path.join(self.prefix, 'LArOpenCV')
        env.set("LAROPENCV_BASEDIR", laropencv_basedir)
        env.set("LAROPENCV_IMAGECLUSTERDIR", os.path.join(laropencv_basedir, "ImageCluster"))

        # Larcv

        larcv_basedir = os.path.join(self.prefix, 'larcv')
        env.set("LARCV_BASEDIR", larcv_basedir)
        env.set("LARCV_COREDIR", os.path.join(larcv_basedir, "larcv/core"))
        env.set("LARCV_APPDIR", os.path.join(larcv_basedir, "larcv/app"))
        env.set("LARCV_LIBDIR", os.path.join(larcv_basedir, "build/installed/lib"))
        env.set("LARCV_INCDIR", os.path.join(larcv_basedir, "build/installed/include"))
        env.set("LARCV_BINDIR", os.path.join(larcv_basedir, "bin"))
        env.prepend_path("PATH", os.path.join(larcv_basedir, "bin"))
        env.prepend_path("PATH", os.path.join(larcv_basedir, "mac"))
        #env.prepend_path("CMAKE_PREFIX_PATH", os.path.join(larcv_basedir, "build/installed/lib/cmake/larcv"))
        #env.prepend_path("CMAKE_PREFIX_PATH",
        #                 "{0}/lib/python{1}/site-packages/torch".format(
        #                     self.spec["py-torch"].prefix,
        #                     self.spec["python"].version.up_to(2)))

        # Ublarcvapp

        ublarcvapp_basedir = os.path.join(self.prefix, 'ublarcvapp')
        env.set("UBLARCVAPP_BASEDIR", ublarcvapp_basedir)
        env.set("UBLARCVAPP_INCDIR", os.path.join(ublarcvapp_basedir, "build/include"))
        env.set("UBLARCVAPP_LIBDIR", os.path.join(ublarcvapp_basedir, "build/lib"))

        env.prepend_path("PATH", os.path.join(ublarcvapp_basedir, "bin"))
        #env.prepend_path("CMAKE_PREFIX_PATH", os.path.join(ublarcvapp_basedir, "build/lib/cmake/ublarcvapp"))

        # Larflow

        larflow_basedir = os.path.join(self.prefix, 'larflow')
        env.set("LARFLOW_BASEDIR", larflow_basedir)
        env.set("LARFLOW_LIBDIR", os.path.join(larflow_basedir, "build/lib"))
        env.set("LARFLOW_INCDIR", os.path.join(larflow_basedir, "build/include"))

        # Ublarcvserver

        env.set("UBLARCVSERVER_BASEDIR", os.path.join(self.prefix, 'ublarcvserver'))
        env.set("UBMRCNN_DIR", os.path.join(self.prefix, 'ublarcvserver/networks/mask-rcnn.pytorch'))
        env.set("SPARSE_INFILL_DIR", os.path.join(self.prefix, 'ublarcvserver/networks/infill'))

        # Python path

        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "larlite/python"))
        #env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "Geo2D/python"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "LArOpenCV/python"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "larcv/python"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "ublarlarcvapp/python"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "larflow/python"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "ublarcvserver/python"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "ublarcvserver/networks/mask-rcnn.pytorch"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "ublarcvserver/networks/mask-rcnn.pytorch/lib"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "ublarcvserver/app/ubmrcnn"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "ublarcvserver/networks/infill"))
        env.prepend_path("PYTHONPATH", os.path.join(self.prefix, "ublarcvserver/networks/sparse_ssnet"))

        # Root include path
        
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larlite/build/installed/include"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larlite/build/installed/include/larlite/Analysis"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larlite/build/installed/include/larlite/Base"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larlite/build/installed/include/larlite/BasicTool"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larlite/build/installed/include/larlite/DataFormat"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larlite/build/installed/include/larlite/LArUtil"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "Geo2D"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "Geo2D/Geo2D/Algorithm"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "Geo2D/Geo2D/Core"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "Geo2D/Geo2D/PyUtil"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "LArOpenCV"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "LArOpenCV/LArOpenCV/Core"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "LArOpenCV/LArOpenCV/App"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "LArOpenCV/LArOpenCV/ImageCluster"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "LArOpenCV/LArOpenCV/ImageCluster/Base"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "LArOpenCV/LArOpenCV/ImageCluster/AlgoClass"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "LArOpenCV/LArOpenCV/ImageCluster/AlgoData"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "LArOpenCV/LArOpenCV/ImageCluster/AlgoFunction"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "LArOpenCV/LArOpenCV/ImageCluster/AlgoModule"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/app/ImageMod"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/core/Base"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/core/CPPUtil"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/core/CVUtil"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/core/DataFormat"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/core/Processor"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/core/PyUtil"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/core/ROOTUtil"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/core/TorchUtil"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larcv/build/installed/include/larcv/core/json"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/ContourTools"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/LArOpenCVHandle"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/LArliteHandler"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/LLCVProcessor"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/MCTools"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/Reco3D"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/UBImageMod"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/UBPhotonLib"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/UBWireTool"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/dbscan"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "ublarcvapp/build/include/ublarcvapp/ubdllee"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larflow/build/include"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larflow/build/include/larflow/KeyPoints"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larflow/build/include/larflow/LArFlowConstants"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larflow/build/include/larflow/PrepFlowMatchData"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larflow/build/include/larflow/Reco"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larflow/build/include/larflow/RecoUtils"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larflow/build/include/larflow/SCBoundary"))
        env.prepend_path("ROOT_INCLUDE_PATH", os.path.join(self.prefix, "larflow/build/include/larflow/Voxelizer"))

        env.prune_duplicate_paths("PATH")
        env.prune_duplicate_paths("PYTHONPATH")
        env.prune_duplicate_paths("CMAKE_PREFIX_PATH")
        env.prune_duplicate_paths("ROOT_INCLUDE_PATH")

    def url_for_version(self, version):
        return f"https://github.com/LArbys/ubdl/archive/refs/tags/v{str(version).replace('.', '_')}.tar.gz"
