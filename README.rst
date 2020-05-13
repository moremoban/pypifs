================================================================================
pypifs
================================================================================

.. image:: https://api.travis-ci.org/moremoban/pypifs.svg
   :target: http://travis-ci.org/moremoban/pypifs

.. image:: https://codecov.io/github/moremoban/pypifs/coverage.png
   :target: https://codecov.io/github/moremoban/pypifs
.. image:: https://badge.fury.io/py/pypifs.svg
   :target: https://pypi.org/project/pypifs

.. image:: https://pepy.tech/badge/pypifs/month
   :target: https://pepy.tech/project/pypifs/month

.. image:: https://img.shields.io/github/stars/moremoban/pypifs.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/pypifs/stargazers

.. image:: https://dev.azure.com/moremoban/pypifs/_apis/build/status/moremoban.pypifs?branchName=master
   :target: https://dev.azure.com/moremoban/pypifs/_build/latest?definitionId=2&branchName=master


It helps perform `file operations <https://docs.pyfilesystem.org/en/latest/guide.html>`_ over the python package.
It installs the python package and returns python file system 2's `OSFS <https://docs.pyfilesystem.org/en/latest/reference/osfs.html>`_ instance.

The idea originates from `moban <https://github.com/moremoban/moban>`_, which uses python package as
a vehicle to have versioned templates for the creation of a new python package. Surely, it can be implemented
in any other ways but moban v0.6.0 mandates python file system 2 interface. Hence this library is written.

Get a file inside a python package
--------------------------------------------------------------------------------

.. code-block:: python

    >>> import fs
    >>> pypi_fs = fs.open_fs("pypi://pypi-mobans-pkg/resources/templates")
    >>> pypi_fs.readtext("_version.py.jj2")
    '__version__ = "0.0.2"\n__author__ = "C.W."\n'


List files of interest
--------------------------------------------------------------------------------

.. code-block:: python

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


Does it write?
--------------------------------------------------------------------------------

Yes, it will write as you can do so without using pypifs. But, it is never the
intention of pypifs.


Installation
================================================================================


You can install pypifs via pip:

.. code-block:: bash

    $ pip install pypifs


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/pypifs.git
    $ cd pypifs
    $ python setup.py install
