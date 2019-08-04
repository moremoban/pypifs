pip freeze
python setup.py develop
nosetests --with-coverage --cover-package pypifs --cover-package tests tests  docs/source pypifs
