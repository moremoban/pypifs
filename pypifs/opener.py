import os
import sys

from fs.opener import Opener
from fs.osfs import OSFS
import fs.path


class PypiFSOpener(Opener):
    protocols = ["pypi"]

    def open_fs(self, fs_url, parse_result, writeable, create, cwd):
        pypi_package_name, _, dir_path = parse_result.resource.partition("/")
        __import__(pypi_package_name)
        directory = os.path.dirname(sys.modules[pypi_package_name].__file__)
        directory = os.path.normcase(directory)
        root_path = fs.path.join(directory, dir_path)
        osfs = OSFS(root_path=root_path)
        return osfs
