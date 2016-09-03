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

After all installation done, a new command will be available to generate chess configurations.

How to use
--------

workon chess_configuration

configurations -m 7 -n 7 --pieces=K,Q,B,R

Unit test execution
--------

python setup.py test

Test case generator
--------
When the algorithm reached a point that requried optimization I buildt a script to save inputs and outputs.
With those file I will execute unit test to check if the solution is ok.

To execute the case generator

pythont test/case_generator.py

This script will generate random cases and save all the files in the tests/data directory.
Use with carefull, if the algorithm has a bug all test cases will be invalid!

More arguments
--------

configurations command also supports the following arguments:

* --output : which will save the configuration to the specified file.
* --output_format : text or json can be used.

Ideas
--------

* 30/08/2016: First idea is to use a backtracking algo using cuts
              to make the code more legible I will use some objects for pieces and for the table.
              A python package to easily handling deps and code installation
* 03/09/2016: Working code with 85% coverage. added pytest benchmark to start performance tunning.
              Ideas: more cuts on the backtracking. remove a slow function in the Piece objects
* 03/09/2016: After all unit test done. The idea is to optimize the O(n^2) inside the backtracking.
              I will add a list of available places

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

