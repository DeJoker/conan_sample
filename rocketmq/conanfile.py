from conans import ConanFile, CMake, tools
import os, shutil


class RocketmqConan(ConanFile):
    name = "rocketmq"
    version = "release-1.2.3"
    license = "Apache 2"
    author = "<Put your name here> <And your email here>"
    url = "https://github.com/Dejokcer/rocketmq-client-cpp"
    description = "<Description of Rocketmq here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake", "txt"

    exports_sources = ["CMakeLists.txt", "rocketmq-client-cpp-release-1.2.3.zip"]
    _source_subfolder = "source_subfolder"

    def requirements(self):
        self.requires.add("boost/1.69.0@conan/stable")
        self.requires.add("zlib/1.2.11@conan/stable")
        self.requires.add("libevent/2.8.1@1602/stable")
        self.requires.add("jsoncpp/1.9.0@seewoMC/testing")
        # self.requires.add("jsoncpp/1.8.3@1602/stable")
        
    def source(self):
        # tools.download("https://github.com/Dejokcer/rocketmq-client-cpp/archive/%s.zip" % self.version, filename="rocketmq.zip")
        tools.unzip("rocketmq-client-cpp-%s.zip" % self.version)
        os.rename("rocketmq-client-cpp-%s" % self.version, self._source_subfolder)

        os.rename(os.path.join(self._source_subfolder, "CMakeLists.txt"),
                  os.path.join(self._source_subfolder, "CMakeListsOriginal.txt"))
        shutil.copy("CMakeLists.txt",
                   os.path.join(self._source_subfolder, "CMakeLists.txt"))
        

    def build(self):
        # tools.chdir(self._source_subfolder)

        cmake = CMake(self)
        cmake.configure(source_dir=self._source_subfolder)
        cmake.build()
        # cmake.install()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rocketmq"]

