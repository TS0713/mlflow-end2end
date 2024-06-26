import setuptools


with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "mlflow-end2end"
AUTHOR_USER_NAME = "TS0713"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "tsp0713@gmail.com"

# It will look for src/mlproject and look for __init__.py inside each subfolder
# and convert those subfolders into packages

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package setup for mlflow",
    long_description = long_description,
    url = f"htpps://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)


#print (long_description)