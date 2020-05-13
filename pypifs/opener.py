import os
import sys

import fs.path
from fs.osfs import OSFS
from fs.opener import Opener

import importlib_metadata as im


class PypiFSOpener(Opener):
    protocols = ["pypi"]
    installed_packages = set()

    def open_fs(self, fs_url, parse_result, writeable, create, cwd):
        pypi_package_name, _, dir_path = parse_result.resource.partition("/")
        if pypi_package_name not in PypiFSOpener.installed_packages:
            pip_install([pypi_package_name])
            PypiFSOpener.installed_packages.add(pypi_package_name)
        module_name = get_module_name(pypi_package_name)
        module_path = get_module_path(module_name)
        root_path = fs.path.join(module_path, dir_path)
        osfs = OSFS(root_path=root_path)
        return osfs


def pip_install(packages):
    import subprocess

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", " ".join(packages)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def get_module_name(package_name):
    content = im.distribution(package_name).read_text("top_level.txt")
    name = content.split("\n", 1)[0]

    return name


def get_module_path(module_name):
    __import__(module_name)
    directory = os.path.dirname(sys.modules[module_name].__file__)
    return os.path.normcase(directory)
