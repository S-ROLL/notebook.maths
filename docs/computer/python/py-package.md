# Python Package
## File creating:
```
run.py
```
```
setup.py
```
## Setuptool
### Initial Installation
```
pip install wheel
```

```
pip install setuptools
```

### File setting
- ``setup.py``

```py
from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()
    
setup(
    name="TiLearn",
    version="0.0.10",
    description="Abaisodjoasinvoidnsv",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="asdasdasd",
    author="Bancie",
    author_email="chibangn1@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
```

- ``run.py``

```py
from x import (
    y,
    z,
)

print(x())

print(y())
```

### Setup
```
python setup.py bdist_wheel
```

```
python setup.py sdist
```

```
python setup.py bdist_wheel sdist
```

### Test time
```
pip install .
```

## PyPI publishing
### Check
```
pip install twine
```
```
twine check dist/*
```
### Publishing
```
twine upload dist/*
```

!!! tip
    - Test PyPI
    ```
    twine upload -r testpypi dist/*
    ```

#### Upgraded
- Fix & Dev...
- Delete ``dist`` file. 
- [Set up time](#setup)
- [Publish](#pypi-publishing)
- Done!

!!! note
    - In PyPI web, let create an **another** token.
    - Chose scope: *the project you developing*.

!!! tip 
    Putting ``import`` to ``__init__.py`` for short calling.