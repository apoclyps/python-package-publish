# Publishing a dependency manually to Gemfury

## Environmental variables

Environmental variables are a good way to keep our tokens secret and our options configurable using a `.env` file

You will first need to configure the secrets within the `.env` file.

```shell
cp .env.example to .env
```

Add your token for Gemfury to `.env` as `GEMFUTY_PUBLISH_TOKEN`

```shell
poetry config repositories.gemfury $GEMFURY_REPOSITORY_URL
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

### Build the package

```shell
poetry build
```

### Publish the package

```shell
poetry publish -r gemfury -vvv
```

### Getting Started with Development

1. Run `poetry install` to install the env.
2. Run `poetry run pre-commit install` to initialize the git hooks.
3. Run `poetry run pre-commit run --all-files` if there are files that were committed before adding the git hooks.
4. Activate the shell with `poetry shell`
5. Test with: `poetry run pytest

### Installing package

Add your token to the session:

```shell
export GEMFURY_DEPLOY_TOKEN=YOUR-TOKEN
```

```shell
pip install python-package-publish --extra-index-url https://${GEMFURY_DEPLOY_TOKEN}:@pypi.fury.io/apoclyps/
```

### Using the Package

```shell
>>> from python_package_publish import chunk

>>> data = [1, 2, 3, 4, 5, 6, 7, 8]

>>> list(chunk(data, 4))
[[1, 2, 3, 4], [5, 6, 7, 8]]

>>> list(chunk(data, 2))
[[1, 2], [3, 4], [5, 6], [7, 8]]
```
