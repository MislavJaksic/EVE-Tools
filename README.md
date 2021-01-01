## Python Project Template
```
# Note: Install Python 3

# Note: install Poetry for Linux
$: curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Note: install Poetry for Windows
$: (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python

$: python get-poetry.py --uninstall
```

```
$: poetry install  # install all dependencies
```

### dist

```
$: pip install dist/eve-0.0.1-py3-none.any.whl

$: poetry-template
```

### docs

```
$: poetry shell
$: cd docs
# Note: review source/conf.py and source/index.rst
$: make html
# Note: see docs in docs/build/apidocs/index.html
```

### eve

```
$: poetry run python ./eve/exploration/runner.py

$: poetry run python ./eve/runner.py
```

### tests

```
$: poetry run pytest
```

```
$: poetry run pytest --cov=eve --cov-report=html tests
#: Note: see coverage report in htmlcov/index.html
```

### poetry.lock

Dependencies, Python version and the virtual environment are managed by `Poetry`.

```
$: poetry search Package-Name
$: poetry add Package-Name[==Package-Version]
```

### pyproject.toml

Define project entry point and metadata.  

### setup.cfg

Configure Python libraries.  

### Linters

```
$: poetry run black .
```

### Publish

```
$: poetry config pypi-token.pypi PyPI-API-Access-Token

$: poetry publish --build
```

```
https://pypi.org/project/poetry-template/
```

### Notes

Choice:
* [pyswagger](https://github.com/pyopenapi/pyswagger): doesn't cache easily into a file; implements swagger api
* [diskcache](http://www.grantjenks.com/docs/diskcache/): can cache files

Alternatives:
* [esipy](https://github.com/Kyria/EsiPy): the author abandoned an adjacent project, has poor documentation and short lived cache; easy EVE API access, implemented security, implements swagger api, retries, ETag, ...
* [swagger-codegen](https://github.com/swagger-api/swagger-codegen): generates an enormous code overhead; creates a whole python project, tests, data models and api function
