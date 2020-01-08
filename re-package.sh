#!/usr/bin/env bash

echo "rebuild"
echo "-"

python3 setup.py sdist bdist_wheel

echo "upload"
echo "-"

python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*