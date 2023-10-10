import pytest
from click.testing import CliRunner
from codespace_utils.core.print_dir import util

@pytest.fixture
def runner():
    return CliRunner()

def test_dirprint(runner):
    result = runner.invoke(util, ['printdir', '.'])  # Using the command 'printdir' from the 'util' click group
    assert result.exit_code == 0, f"Unexpected output:\n{result.output}"  # Combined the print and assert for simplicity

def test_dirprint_exclude(runner):
    result = runner.invoke(util, ['printdir', '.', '--exclude', '.py'])  # Using 'printdir' from 'util'
    assert result.exit_code == 0
    assert 'codespace_utils.py' not in result.output
