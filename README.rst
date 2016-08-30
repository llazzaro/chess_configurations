===============================
chess_configurations
===============================


.. image:: https://img.shields.io/pypi/v/chess_configurations.svg
        :target: https://pypi.python.org/pypi/chess_configurations

.. image:: https://img.shields.io/travis/llazzaro/chess_configurations.svg
        :target: https://travis-ci.org/llazzaro/chess_configurations

.. image:: https://readthedocs.org/projects/chess-configurations/badge/?version=latest
        :target: https://chess-configurations.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/llazzaro/chess_configurations/shield.svg
     :target: https://pyup.io/repos/github/llazzaro/chess_configurations/
     :alt: Updates


Finds all unique configurations of a set of normal chess pieces on a chess boa


* Free software: MIT license
* Documentation: https://chess-configurations.readthedocs.io.


Features
--------

* TODO


Recommended Installations steps
--------

pip install virtualenvwrapper
mkvirtualenv chess_configuration
python setup.py install

After all installation is done in the virtualenv a new command will be available to generate configurations.

How to use
--------

workon chess_configuration
configurations -m 7 -n 7 --pieces_types=K,Q,B,R

More arguments
--------

configurations command also supports the following arguments:

* --output : which will save the configuration to the specified file.


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

