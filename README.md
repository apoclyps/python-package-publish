# python-package-publish

How to push a Poetry package to a private Gemfury PyPI server

## Automatic release process

The process to publish to Gemfury has been automated by this Github action workflow in this Repository.

Following [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) a release will be created for all features and fixes after a pull request following these conventions are merged.

| Increment | Description                 | Conventional commit map |
| --------- | --------------------------- | ----------------------- |
| MAJOR     | Breaking changes introduced | BREAKING CHANGE         |
| MINOR     | New features                | feat                    |
| PATCH     | Fixes                       | fix + everything else   |

As soon as a new version is detected a pull request is opened for that release. Each subsequent merged change will be appended to that release until it has been merged which will trigger a new release candidate to be created on GitHub and then pushed to Gemfury.
