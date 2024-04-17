#  Copyright (c) 2024. OCX Consortium https://3docx.org. See the LICENSE
""" CLI script tests."""
import pytest
from typer.testing import CliRunner

from ocx_geometry_tests import __version__
from ocx_geometry_tests.cli import ocx-geometry


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(ocx-geometry, ['version'])
    assert result.exit_code == 0
    assert __version__ in result.output

def test_cli_greet():
    runner = CliRunner()
    name = 'John'
    surname = 'Doe'
    result = runner.invoke(ocx-geometry, ['greet', name, '--surname', surname])
    assert result.exit_code == 0
    assert surname in result.stdout
