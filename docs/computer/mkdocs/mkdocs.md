# Mkdocs key command setting

## Installation

```
pip install mkdocs
```

```
pip install mkdocs-material
```

```
pip install mkdocs-encryptcontent-plugin
```

## Setting

```
mkdocs new .
```

```
mkdocs serve
```

## File

``.github/workflows/ci.yml``

- Sample

```yml
name: ci

on:
  push:
    branches:
      - master
      - main

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - uses: actions/cache@v2
        with:
          key: ${{ github.ref }}
          path: .cache
      - run: pip install mkdocs-material
      - run: pip install pillow cairosvg
      - run: pip install mkdocs-encryptcontent-plugin  # Install plugin from PyPI
      - run: mkdocs gh-deploy --force
```

## Git

```
git add .
```

```
git commit -m $'Adding initial documentation files'
```

```
git push origin main
```
!!! info
    [set up encry](https://pypi.org/project/mkdocs-encryptcontent-plugin/#:~:text=Add%20an%20meta%20tag%20password,yml%22.)