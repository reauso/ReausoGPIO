# ReausoGPIO Project

## Coding Standards

@CODING_STYLE.md

## Architecture

This is a Python GPIO wrapper library that enables unified usage of different GPIO libraries.

@Idea.md

## Tests

You can find unit tests in rgpio_unittests directory and integration tests in rgpio_integrationtests directory.

You can run all tests with `pixi run test` and you can check the coverage with `pixi run coverage`

## Important Notes

- Always run tests before committing and also ensure a very good coverage
- Always check and update the documentation and documentation files before comitting
- Use pixi for dependency management defined in pyproject.toml
