import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oxo_pkg",
    version="2.0.11",
    author="Adam Harrison",
    author_email="author@example.com",
    description="naughts and crosses game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/add-harris/oxo_pkg",
    scripts=["oxo"],
    packages=setuptools.find_packages(),
    # non of these are currently working - need to include these files in distributed app
    data_files=[("", ['README.md', 'LICENSE'])],
    # if True should include files specified in MANIFEST.in
    include_package_data=True,
    package_data={
        '': ['README.md', 'LICENSE']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
