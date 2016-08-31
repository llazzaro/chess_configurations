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


Recommended Installations steps
--------

pip install virtualenvwrapper
mkvirtualenv chess_configuration
pip install git+https://github.com/llazzaro/chess_configurations.git

After all installation is done in the virtualenv a new command will be available to generate configurations.

How to use
--------

workon chess_configuration
configurations -m 7 -n 7 --pieces_types=K,Q,B,R

Unit test execution
--------

python setup.py test

More arguments
--------

configurations command also supports the following arguments:

* --output : which will save the configuration to the specified file.

Ideas
--------

* 30/08/2016: First idea is to use a backtracking algo using cuts
              to make the code more legible I will use some objects for pieces and for the table.
              A python package to easily handling deps and code installation
*


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

