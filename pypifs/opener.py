import os
import sys

import fs.path
import pkg_resources as pkg
from fs.osfs import OSFS
from fs.opener import Opener


class PypiFSOpener(Opener):
    protocols = ["pypi"]

    def open_fs(self, fs_url, parse_result, writeable, create, cwd):
        pypi_package_name, _, dir_path = parse_result.resource.partition("/")
        module_name = get_module_name(pypi_package_name)
        module_path = get_module_path(module_name)
        root_path = fs.path.join(module_path, dir_path)
        osfs = OSFS(root_path=root_path)
        return osfs


def get_module_name(package_name):
    meta_data_dir = pkg.get_distribution("pypi-mobans-pkg").egg_info
    with fs.open_fs(meta_data_dir) as data_dir:
        content = data_dir.read("top_level.txt")
        name = content.split("\n", 1)[0]

    return name


def get_module_path(module_name):
    __import__(module_name)
    directory = os.path.dirname(sys.modules[module_name].__file__)
    return os.path.normcase(directory)
