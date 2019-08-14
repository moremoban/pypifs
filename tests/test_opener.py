import fs
from nose.tools import assert_in, eq_
from mock import patch


def test_open_fs():
    folder = fs.open_fs("pypi://pypi-mobans-pkg/resources/templates")
    content = folder.readtext(u"README.rst.jj2")
    assert_in("installation.rst.jj2", content)


@patch("pypifs.opener.pip_install")
def test_pip_install(fake_pip):
    fs.open_fs("pypi://abc/resources/templates")
    fs.open_fs("pypi://abc/resources/templates")
    eq_(fake_pip.call_count, 1)
