A collection of MCP tools to be used with tools/IDEs which support the MCP protocol.

## Why "aiducts"?

Conduits (ducts) specifically for AI (ai) communications and data flow.

## Features

TBD

## Technologies

- `Python` 3.13 and `mcp` SDK

- `uv` for packaging (requirements, additional tooling)

- `Makefile` to wrap the most common operations and ease project management, with commands to run the development server, shell, etc...

- code style and quality: `ruff` as the linter and formatter (customized with `pyproject.toml`)

- environment variables for configuration (`.env` file)

## How to run this project locally (development environment)

- This requires the installation of python's `uv` package manager. To install it:

``` bash

$ curl -LsSf https://astral.sh/uv/install.sh | sh

```

- Create a virtualenv to the project. If you want to use the default provided using uv on the Makefile:

``` bash

$ make dev-setup-uv

```

- Install the development requirements (also using uv):

``` bash

$ make requirements

```


- Run the make command to create the sample configuration file:

``` bash

$ make init-env

```

- Run the formatter and linter:

NOTE: We use "ruff" as a python linter and formatter, due to its' speed.

If you do not have it installed, you can run this command first:

``` bash

$ make dev-setup-ruff

```

This will install ruff globally, but do not worry. It needs to be explicitly called and you can customize its' behavior per project if you need.

``` bash

$ make style; make style-autofix && make style
$ make lint; make lint-autofix && make lint

```

## Future enhancements

TBD

### Infrastructure

- CI pipeline (github actions):
    - ruff lint/format check
    - tests (with coverage report)


## References

The repository was bootstrapped with code from [this article](https://www.datacamp.com/tutorial/mcp-model-context-protocol).
