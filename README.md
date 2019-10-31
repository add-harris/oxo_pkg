# OXO

A naughts & crosses game.

# Install

To install run command:

`python3 -m pip install --user --upgrade oxo_pkg` (not yet available, use TestPyPi)

if installing from [TestPyPi](https://test.pypi.org/project/oxo-pkg/) run:

`python3 -m pip install --user --index-url https://test.pypi.org/simple/ oxo_pkg`

# Run

Oxo can either by ran as a commandline script or as a python package ran in the Python3 REPL.

#### run in python REPL :

Open the python3 REPL

`python3`

import and run the package

\>`import oxo_pkg`

\>`oxo_pkg.run()`

#### run in commandline :

run `oxo` in a commandline terminal.

#### troubleshooting

try `which oxo`

This should print something like `/Users/your.username/Library/Python/3.7/bin/oxo`

If not find the equivalent location in your filesystem (where pip installs applications to), check that `oxo` binary file is present, & add the location to your PATH.

# Build

`python3 -m pip install --user --upgrade setuptools wheel` (install / update wheel & setuptools)

`python3 setup.py sdist bdist_wheel`

Produces a .whl built distribution & a tar file of the source code in `dist/` directory.

# Release

Increment release number in `setup.py` file.

Build a new release with steps above.

`python3 -m pip install --user --upgrade twine` (install / update twine)

`python3 -m twine upload dist/*` 

To upload to [TestPyPi](https://test.pypi.org/project/oxo-pkg/) run:

`python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*` 