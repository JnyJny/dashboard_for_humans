
[![Release][badge-release]][release]
![Version][badge-pypi-version]
![Release Date][badge-release-date]
![Python Version][badge-python-version]
![License][badge-license]
![Monthly Downloads][badge-monthly-downloads]
# dashboard_for_humans - Dashboard for Humans

> Dashboard for humans.

<!-- project description -->

## Features

<!-- project features --> 

## Installation

### pip

```console
python3 -m pip install dashboard_for_humans
```

### uvx
```console
uvx --from dashboard_for_humans dashboard
```

### uv

```console
uvx pip install dashboard_for_humans
```

## Usage

```console
dashboard --help
```


## Development

This project and it's virtual environment is managed using [uv][uv] and
is configured to support automatic activation of virtual environments
using [direnv][direnv]. Development activites such as linting and testing
are automated via [Poe The Poet][poethepoet], run `poe` after cloning
this repo.

### Clone
```console
git clone https://github.com/JnyJny/dashboard_for_humans
cd dashboard_for_humans
```
### Allow Direnv _optional_ but recommended
```console
direnv allow
```

### Create a Virtual Environment
```console
uv venv
```
### Install Dependencies
```console
uv sync
```
### Run `poe`
```console
poe --help
```

<hr>

[![gh:JnyJny/python-package-cookiecutter][python-package-cookiecutter-badge]][python-package-cookiecutter]

<!-- End Links -->

[python-package-cookiecutter-badge]: https://img.shields.io/badge/Made_With_Cookiecutter-python--package--cookiecutter-green?style=for-the-badge
[python-package-cookiecutter]: https://github.com/JnyJny/python-package-cookiecutter
[badge-release]: https://github.com/JnyJny/dashboard_for_humans/actions/workflows/release.yaml/badge.svg
[release]: https://github.com/JnyJny/dashboard_for_humans/actions/workflows/release.yaml
[badge-pypi-version]: https://img.shields.io/pypi/v/dashboard_for_humans
[badge-release-date]: https://img.shields.io/github/release-date/JnyJny/dashboard_for_humans
[badge-python-version]: https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FJnyJny%2Fdashboard_for_humans%2Fmain%2Fpyproject.toml
[badge-license]: https://img.shields.io/github/license/JnyJny/dashboard_for_humans
[badge-monthly-downloads]: https://img.shields.io/pypi/dm/dashboard_for_humans
[poe]: https://poethepoet.natn.io
[uv]: https://docs.astral.sh/uv/
[direnv]: https://direnv.net
