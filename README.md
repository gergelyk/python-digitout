# digitout

Seek data structures of your Python application.

## Installation

```sh
pip install digitout
```

## Usage

```python
def foobar() -> 123:
    pass

import digitout
digitout(foobar)
```

## Documentation

<https://gergelyk.github.io/python-digitout/>

## Author

Grzegorz Krason <grzegorz.krason@gmail.com>

## Development

### Preparing Environment

```sh
pip install --user poetry  # unless already installed
poetry install
```

### Running Application

```sh
poetry run python -m digitout
```

### Rendering Documentation

```sh
poetry run mkdocs serve
```

### Testing

```sh
poetry run pytest
```

### Bumping Version

```sh
poetry version minor  # increment selected component
git tag ${$(poetry version)[2]}
git push --tags
```

### Building Package

```sh
poetry build
```

### Publishing Documentation

```sh
poetry run mkdocs gh-deploy -b gh-pages
```

### Publishing Package

```sh
read -s PASS
poetry publish --build -u <username> -p $PASS
unset PASS
```

### Compatibility with `setuptools`

Looking for `setup.py`? Try using `poetry`, or if you really need `setup.py`, invoke:

```sh
pip install --user dephell  # unless already installed
dephell deps convert --from pyproject.toml --to setup.py
```
