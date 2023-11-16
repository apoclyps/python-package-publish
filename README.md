# python-package-publish

This example repository will outline how to push a Poetry package to a private Gemfury PyPI server using Github Actions, Commitizen, and Release Please to help automate as the release process

## Gemfury Publishing Workflow

The Gemfury publishing process has been automated through the implementation of a GitHub Action workflow in this repository.

Adhering to the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) pattern in commit messages and pull request titles will automatically trigger the creation of a release upon merging the pull request.

Semantic versioning is applied to new releases according to the following criteria:

| Increment | Description                 | Conventional Commit Map |
| --------- | --------------------------- | ----------------------- |
| MAJOR     | Breaking changes introduced | BREAKING CHANGE         |
| MINOR     | New features                | feat                    |
| PATCH     | Fixes                       | fix + all other types   |

Upon merging a change, a pull request is initiated for that particular release. Each subsequent merged change appends to this release until completion. This process triggers the creation of a new release candidate on GitHub, subsequently pushing the changes to Gemfury.
