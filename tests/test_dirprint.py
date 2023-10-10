import pytest
from click.testing import CliRunner
from codespace_utils.print_dir import util

@pytest.fixture
def runner():
    return CliRunner()

def test_dirprint(runner):
    result = runner.invoke(util, ['printdir', '.'])  # Changed dirprint to the command name 'printdir'
    if result.exit_code != 0:
        print(result.output)
    assert result.exit_code == 0

def test_dirprint_exclude(runner):
    result = runner.invoke(util, ['printdir', '.', '--exclude', '.py'])  # Again, changed dirprint to 'printdir'
    assert result.exit_code == 0
    assert 'codespace_utils.py' not in result.output
