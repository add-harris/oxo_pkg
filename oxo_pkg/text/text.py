
version_text = "oxo version: 2.0.11"

help_text = """
here is a list of accepted arguments: 
    --hard     :  activates hard-mode
    --s-hard   :  activates super-hard-mode
    --version  :  show current version number
    --help     :  show help options
    --license  :  show license
    --readme   :  show readme
"""

# not currently working in distributed version
try:
    with open("README.md") as fh:
        readme = fh.read()
except:
    readme = "README not found"

try:
    with open("LICENSE") as fh:
        license_txt = fh.read()
except:
    license_txt = "LICENSE not found"
