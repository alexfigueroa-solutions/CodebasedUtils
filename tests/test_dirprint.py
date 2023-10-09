import pytest
from click.testing import CliRunner
from ..codespace_utils import dirprint

@pytest.fixture
def runner():
    return CliRunner()

def test_dirprint(runner):
    result = runner.invoke(dirprint, ['--path', '.'])
    assert result.exit_code == 0
    assert 'codespace_utils.py' in result.output

def test_dirprint_exclude(runner):
    result = runner.invoke(dirprint, ['--path', '.', '--exclude', '.py'])
    assert result.exit_code == 0
    assert 'codespace_utils.py' not in result.output
