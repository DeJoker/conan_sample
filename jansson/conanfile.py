from conans import ConanFile, CMake, tools
import os, shutil

class JanssonConan(ConanFile):
    name = "jansson"
    version = "2.12"
    url = "https://github.com/akheron/jansson"   
    license     = "MIT"
    description = "<Description of Jansson here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt", "jansson-2.12.zip"]
    generators  = "cmake", "txt"

    _source_subfolder = "source_subfolder"

    def source(self):
        
        checksum = "2e537edb60fd37cf5c7bc257a804bf4e6d1bea8075878a2ea301f307c9b609fe"
        tools.get("https://github.com/akheron/jansson/archive/%s.zip" % self.version, filename="jansson-%s.zip" % self.version, sha256=checksum)
        
        # zip自动解压无需调用该命令
        # tools.unzip("jansson-%s.zip" % self.version)
        os.rename("jansson-%s" % self.version, self._source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("license*", src=self._source_subfolder, dst="licenses", ignore_case=True, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["jansson"]

