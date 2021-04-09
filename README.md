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
$: poetry run python ./eve_tools/exploration/runner.py

$: poetry run python ./eve_tools/runner.py
```

### tests

```
$: poetry run pytest --durations=0
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
* [pyswagger](https://github.com/pyopenapi/pyswagger): doesn't cache easily into a file; implements swagger api !!! hasn't been updated for a very long time!
* [diskcache](http://www.grantjenks.com/docs/diskcache/): can cache files

Alternatives:
* [esipy](https://github.com/Kyria/EsiPy): the author abandoned an adjacent project, has poor documentation and short lived cache; easy EVE API access, implemented security, implements swagger api, retries, ETag, ...
* [swagger-codegen](https://github.com/swagger-api/swagger-codegen): generates an enormous code overhead; creates a whole python project, tests, data models and api function

### More notes

* Differential caching
* sort BPCs
* what happens when a contract expires? update cache? ignore (current, but bad)?
* longer caching (30 days)
* account for errors like the API returning ([], 200)
* SDE is required - analyze it
* do more research

### EVE IPH

* Update Prices - select all items and click Download Prices
* Blueprints - select one - tick calculate build/buy - see if you should buy or build a component
* File - add character - login - set as default
* Manufacturing list - compare all owned blueprints to figure out which one you should build first
* SVR stands for Sales Volume Ratio

### Plan

* Python <-> SQLite (sqlite3 lib)
* Describe EVE SDE
* list SDE locations, headers and description
* explore the SDE
* Get data from the SQLite DB
* Blueprint cost? Example, Vigilant



https://developers.eveonline.com/ - register a token

Importants bits of the agreemant:
Although the rights granted under this Agreement are intended for non-commercial and non-profit use, CCP recognizes that Developer may want to use the Application to increase Developer's status or resources as a Player of EVE. In addition, CCP recognizes that Developer may incur costs to host, maintain, and support the Application. Therefore, the following methods of monetizing an Application are permitted by CCP: (a) Developer may condition the access or use of an Application on payment or other transfer of EVE's valid in-game currency (e.g., ISK) to Developer or to any registered EVE corporation of which Developer is a member; (b) Developer may solicit voluntary donations of money from Players (i.e., U.S. dollars, British Pounds Sterling, etc.) solely to offset Developer's costs of maintaining and supporting an Application, provided that use of the Application is not in any way restricted or conditioned on providing such a donation; or (c) Developer may generate revenue from displaying general advertisements that do not interfere with a Player's access to, or use of, the Application. Revenue from general advertisements includes revenue from partner programs such as Google AdSense, YouTube, Twitch.tv, Ustream.tv, or similar sites. Each of the monetization activities above will be permitted provided they are not carried out in a manner that would otherwise violate EVE's end user license agreement, terms of service, or other rules and conditions accepted as a condition to access EVE. In addition, receipt of advertising revenue must comply with any guidelines published by CCP from time to time. CCP reserves the right, in its sole discretion, to determine whether any method of monetizing an Application complies with the Purpose and the conditions of this Section 4.4.


    Developer shall not pay CCP any royalties or fees for the rights granted herein. CCP shall not pay Developer any royalties or fees for the rights granted herein.
    At a later date, CCP may choose to begin charging fees or collecting royalties for the rights granted herein. However, CCP shall provide Developer of no less than ninety (90) calendar days' notice prior to doing so, and in accordance with Section 6.4, Developer may terminate this Agreement upon written notice to CCP.

Developer shall ensure that EVE and the Licensed Materials retain all proprietary notices necessary to protect CCP's intellectual property rights in the foregoing, including without limitation ownership of all Derivative Works, such notice to be substantially as follows: "© 2014 CCP hf. All rights reserved. "EVE", "EVE Online", "CCP", and all related logos and images are trademarks or registered trademarks of CCP hf."

CCP recognizes that it is not the owner of the Applications(s), and CCP will not contest ownership of the Application(s). In addition, CCP will not register or attempt to register any intellectual property right or other ownership right in the Application(s) (except to the extent necessary to protect CCP's ownership of EVE, the CCP Marks, and the Licensed Materials).


Go through the https://developers.eveonline.com/blog as it explains a lot! :D

https://developers.eveonline.com/blog/article/updated-esi-quick-reference-for-new-developers
