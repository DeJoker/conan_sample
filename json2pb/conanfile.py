from conans import ConanFile, CMake, tools
import os, shutil

class JanssonConan(ConanFile):
    name = "json2pb"
    version = "master"
    url = "https://github.com/DeJoker/json2pb"   
    license     = "MIT"
    description = "<Description of Jansson here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt", "master.zip"]
    generators  = "cmake", "txt"

    _source_subfolder = "source_subfolder"

    def requirements(self):
        self.requires.add("protobuf/2.6.1@seewoMC/testing")
        self.requires.add("jansson/2.12@seewoMC/testing")

    def source(self):
        """
        checksum = "799463bd7f2f4cb1a1523963fd66bc09bc7aec27b2526277a3660d53c248bf96"
        # 使用get命令 zip会自动解压
        tools.get("https://github.com/DeJoker/json2pb/archive/%s.zip" % self.version, filename="json2pb-%s.zip" % self.version, sha256=checksum)
        """

        tools.download("https://github.com/DeJoker/json2pb/archive/%s.zip" % self.version, filename="json2pb-%s.zip" % self.version)
        tools.unzip("json2pb-%s.zip" % self.version)
        os.rename("json2pb-%s" % self.version, self._source_subfolder)

        # 如果需要修改源码才使用该命令
        # tools.patch(patch_file="json2pb.patch", base_path=self._source_subfolder)

        # os.rename(os.path.join(self._source_subfolder, "CMakeLists.txt"),
        #           os.path.join(self._source_subfolder, "CMakeListsOriginal.txt"))
        # shutil.copy("CMakeLists.txt",
        #             os.path.join(self._source_subfolder, "CMakeLists.txt"))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("license*", src=self._source_subfolder, dst="licenses", ignore_case=True, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["jansson"]

