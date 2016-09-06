===============================
chess_configurations
===============================
Finds all unique configurations of a set of normal chess pieces on a chess board

.. image:: https://travis-ci.org/llazzaro/chess_configurations.svg?branch=master
    :target: https://travis-ci.org/llazzaro/chess_configurations
    
.. image:: https://landscape.io/github/llazzaro/chess_configurations/master/landscape.svg?style=flat
   :target: https://landscape.io/github/llazzaro/chess_configurations/master
   :alt: Code Health

.. image:: http://g.recordit.co/L8QfU5McUZ.gif
     :alt: Preview



* Free software: MIT license


Recommended Installations steps
--------

pip install virtualenvwrapper

. /usr/local/bin/virtualenvwrapper.sh (works in ubuntu)

mkvirtualenv chess_configuration

pip install git+https://github.com/llazzaro/chess_configurations.git

After all installation done, a new command will be available to generate chess configurations.




How to use
--------

workon chess_configuration

manage -m 7 -n 7 --pieces=K,Q,B,R


Unit test execution
--------

python setup.py test

Test case generator
--------
When the algorithm reached a point that requried optimization I buildt a script to save inputs and outputs.
With those file I will execute unit test to check if the solution is ok.

To execute the case generator

python test/case_generator.py

This script will generate random cases and save all the files in the tests/data directory.
Use with carefull, if the algorithm has a bug all test cases will be invalid!

More arguments
--------

configurations command also supports the following arguments:

* --animation : will show every board, even invalid ones!
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

TODO
---------

* piece type optimization: For example we can optimize the queen like it is usually done with the N-queens problems.

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
