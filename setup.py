from setuptools import find_packages, setup

setup(
    name="baseball-utilities",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "sqlalchemy"
    ],
)
