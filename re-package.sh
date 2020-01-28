#!/usr/bin/env bash

echo "rebuild"
echo "-"

python3 setup.py sdist bdist_wheel

echo "upload"
echo "-"

# upload to test pypi
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# upload to real pypi
#python3 -m twine upload https://test.pypi.org/legacy/ dist/*