from setuptools import find_packages, setup, Extension
from setuptools.command.build_ext import build_ext
from pathlib import Path
import os
import sys
import subprocess


class PyPegLibExtension(Extension):
    """
    An extension to run the cmake build

    This simply overrides the base extension class so that setuptools
    doesn't try to build your sources for you
    """

    def __init__(self, name, sources=[]):
        super().__init__(name = name, sources = sources)

class PyPegLibBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError(
                "CMake must be installed to build the following extensions: " +
                ", ".join(e.name for e in self.extensions))

        ext = self.extensions[0]
        projectName = self.get_ext_fullpath(ext.name)
        projectName = os.path.basename(projectName)
        projectName = projectName[:projectName.rfind('.')]

        build_directory = os.path.abspath(self.build_temp)
        cmake_args = [
            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + build_directory,
            '-DPYTHON_EXECUTABLE=' + sys.executable
        ]

        print()

        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]
        cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]

        # Assuming Makefiles
        build_args += ['--', '-j2']

        self.build_args = build_args

        env = os.environ.copy()
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        env['PROJECT_NAME'] = projectName;

        # CMakeLists.txt is in the same directory as this setup.py file
        cmake_list_dir = os.path.abspath(os.path.dirname(__file__))
        print('-'*10, 'Running CMake prepare', '-'*40)
        subprocess.check_call(['cmake', cmake_list_dir] + cmake_args,
                              cwd=self.build_temp, env=env)

        print('-'*10, 'Building extensions', '-'*40)
        cmake_cmd = ['cmake', '--build', '.'] + self.build_args
        subprocess.check_call(cmake_cmd,
                              cwd=self.build_temp)

        # Move from build temp to final position
        self.move_output(ext)

    def move_output(self, ext):
        build_temp = Path(self.build_temp).resolve()
        dest_path = Path(self.get_ext_fullpath(ext.name)).resolve()
        source_path = build_temp / self.get_ext_filename(ext.name)
        dest_directory = dest_path.parents[0]
        dest_directory.mkdir(parents=True, exist_ok=True)
        self.copy_file(source_path, dest_path)

setup(name='py_peglib',
      version='1.0.0',
      packages=find_packages(),
      ext_modules=[PyPegLibExtension(name="py_peglib")],
      description='It\'s a C++ binding to the wonderfull yhriose cpp-peglib.',
      long_description=open("./README.md", 'r').read(),
      long_description_content_type="text/markdown",
      keywords="peglib, extension",
      classifiers=["Intended Audience :: Developers",
                   "Programming Language :: C",
                   "Programming Language :: C++",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: Implementation :: CPython"],
      license='MIT',
      cmdclass={
            'build_ext': PyPegLibBuild,
      }
    )