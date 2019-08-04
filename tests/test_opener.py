import fs
from nose.tools import assert_in


def test_open_fs():
    folder = fs.open_fs("pypi://pypi-mobans-pkg/resources/templates")
    content = folder.readtext(u"README.rst.jj2")
    assert_in("installation.rst.jj2", content)
