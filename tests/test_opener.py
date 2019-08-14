import fs
from mock import patch
from nose.tools import eq_, assert_in


def test_open_fs():
    folder = fs.open_fs("pypi://pypi-mobans-pkg/resources/templates")
    content = folder.readtext(u"README.rst.jj2")
    assert_in("installation.rst.jj2", content)


@patch("pypifs.opener.pip_install")
def test_pip_install(fake_pip):
    fs.open_fs("pypi://abc/resources/templates")
    fs.open_fs("pypi://abc/resources/templates")
    eq_(fake_pip.call_count, 1)


@patch("pypifs.opener.pip_install")
def test_pip_install_the_right_package(fake_pip):
    fs.open_fs("pypi://package_name/resources/templates")
    fake_pip.assert_called_with(["package_name"])
