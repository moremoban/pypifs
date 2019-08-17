================================================================================
pypifs
================================================================================

.. image:: https://api.travis-ci.org/moremoban/pypifs.svg
   :target: http://travis-ci.org/moremoban/pypifs

.. image:: https://codecov.io/github/moremoban/pypifs/coverage.png
   :target: https://codecov.io/github/moremoban/pypifs


.. image:: https://dev.azure.com//pypifs/_apis/build/status/.pypifs?branchName=master
   :target: https://dev.azure.com/moremoban/pypifs/_build/latest?definitionId=2&branchName=master


It will install the python package if it is not present. Then it help perform file
operations over the installed python package.

Get a file inside a python package::

    >>> import fs
    >>> pypi_fs = fs.open_fs("pypi://pypi-mobans-pkg/resources/templates")
    >>> pypi_fs.read("_versions.py.jj2")
    '__version__ = "0.0.1"\n__author__ = "C.W."\n'


List files of interest::

    >>> pypi_fs = fs.open_fs("pypi://pypi-mobans-pkg/resources")
    >>> for path in pypi_fs.walk.files(filter=['*.jj2']):
    ...     print(path)
    ... 
    /templates/requirements.txt.jj2
    /templates/installation.rst.jj2
    /templates/test.script.jj2
    /templates/conf.py.jj2
    /templates/_version.py.jj2
    /templates/Pipfile.jj2
    /templates/min_requirements.txt.jj2
    /templates/README.rst.jj2
    /templates/badges.rst.jj2
    /templates/__init__.py.jj2
    /templates/NEW_BSD_LICENSE.jj2
    /templates/MANIFEST.in.jj2
    /templates/CHANGELOG.rst.jj2
    /templates/travis.yml.jj2
    /templates/setup.py.jj2
    /templates/gitignore.jj2
    /templates/lint.script.jj2
    /templates/tests/requirements.txt.jj2
    /templates/docs/make.bat.jj2
    /templates/docs/Makefile.jj2
    /templates/docs/index.rst.jj2
    /templates/docs/source/conf.py.jj2
    /templates/docs/source/index.rst.jj2


Installation
================================================================================

You can get it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/pypifs.git
    $ cd pypifs
    $ python setup.py install
