# Configuring a Project to Use Gemfury Package

## 1. Environment Variables

Add the required environment variables `GEMFURY_DOWNLOAD_TOKEN` and `GEMFURY_REPOSITORY_URL` to your project environment. This can be achieved by either setting them as environmental variables or by including them in a `.env` file. If you opt for the latter, ensure that the `.env` file is excluded from version control using a `.gitignore` file.

## 2. Configure Poetry for Gemfury

Use the following commands to configure Poetry to use Gemfury as a repository:

```bash
poetry config virtualenvs.create false && \
poetry config repositories.gemfury $GEMFURY_REPOSITORY_URL && \
poetry config http-basic.fury $GEMFURY_DOWNLOAD_TOKEN NOPASS
```

## 3. Additional Configuration for Docker

When building your Docker container, pass the build arguments for your Gemfury credentials:

```bash
docker build \
    --build-arg GEMFURY_DOWNLOAD_TOKEN=$(GEMFURY_DOWNLOAD_TOKEN) \
    --build-arg GEMFURY_DOWNLOAD_TOKEN=$(GEMFURY_REPOSITORY_URL) \
    -t $(DOCKER_REPOTAG) .
```

Example Dockerfile:

```dockerfile
ENV POETRY_VERSION=1.6.1

ARG GEMFURY_DOWNLOAD_TOKEN

RUN pip3 install "poetry==$POETRY_VERSION" --no-cache-dir && \
    poetry config virtualenvs.create false && \
    poetry config repositories.gemfury $GEMFURY_REPOSITORY_URL && \
    poetry config http-basic.fury $GEMFURY_DOWNLOAD_TOKEN NOPASS
```

## 4. Adding Dependency to pyproject.toml

Update your pyproject.toml to include Gemfury as a source:

```toml
[[tool.poetry.source]]
name = "fury"
url = "https://pypi.fury.io/apoclyps/"
priority = "primary"

[[tool.poetry.source]]
name = "PyPI"
priority = "primary"

[tool.poetry.dependencies]
python-package-publish = { version = "0.3.0", source = "fury" }
```

## 5. Importing Your Package

Now, you can import your package into your source code:

```python
from python_package_publish.utils import get_utc_now

now = get_utc_now()
```

By following these steps, you should have successfully configured your project to use the Gemfury package.
