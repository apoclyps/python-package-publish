# python-package-publish

How to push a Poetry package to a private Gemfury PyPI server

## Pushing to Gemfury

### Environmental variables

Environmental variables are a good way to keep our tokens secret and our options configurable using a `.env` file

## Setup

```shell
cp .env.example to .env
```

Add your token for Gemfury to `.env`

```shell
poetry config repositories.gemfury https://push.fury.io/apoclyps
poetry config http-basic.gemfury $GEMFURY_PUBLISH_TOKEN NOPASS
```

Confirm it exists within `ls ~/.config/pypoetry/`.

> auth.toml

```toml
[http-basic.gemfury]
username = "SECRET-TOKEN"
password = "NOPASS"
```

> config.toml

```toml
[repositories.gemfury]
url = "https://push.fury.io/apoclyps"

```

> pyproject.toml

```toml
[tool.poetry]
name = "poetry-instance"
version = "1.3.2"
description = ""
authors = []
license = ""

[tool.poetry.dependencies]
python = "3.11.1"
poetry = "1.3.2"

```

## Build the package

```shell
poetry build
```

## Publish the package

```shell
poetry publish -r gemfury -vvv
```

## Getting Started with Development

1. Run `poetry install` to install the env.
2. Run `poetry run pre-commit install` to initialize the git hooks.
3. Run `poetry run pre-commit run --all-files` if there are files that were committed before adding the git hooks.
4. Activate the shell with `poetry shell`
5. Test with: `poetry run pytest
