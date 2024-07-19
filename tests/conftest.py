
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# IMPORT

import pytest

import pywildmatch
import pywildmatch.error


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# DATA

def get_name(module):
    if module.__name__.startswith(('test_', 'validate_')):
        return module.__name__.split('_', maxsplit=1)
    pytest.exit(f'DATA NAME NOT FOUND: {module.__name__}', 1)


def get_data(name):
    data = __import__(f'data.{name}', None, None, ['DATA'], 0)
    return data.DATA


def pytest_generate_tests(metafunc):
    parameters = []
    prefix, name = get_name(metafunc.module)
    data = get_data(name)
    for testcase in data:
        pattern,text,results = testcase
        for flag,expected in enumerate(results[prefix]):
            parameters.append(
                pytest.param(pattern, text, flag, expected)
            )
    metafunc.parametrize('pattern,text,flag,expected', parameters)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# TEST MATCH

@pytest.fixture
def match(pattern, text, flag, expected):
    if isinstance(expected, bool):
        match = pywildmatch.Match(pattern, flag)
        result = match(text)
        assert bool(result) == expected
    else:
        with pytest.raises(pywildmatch.error.PywildmatchError) as e:
            pywildmatch.Match(pattern, flag)
        assert e.typename == expected


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# TEST IGNORE

@pytest.fixture
def ignore(pattern, text, flag, expected):
    if isinstance(expected, bool):
        ignore = pywildmatch.Ignore(pattern, flag)
        result = ignore(text)
        assert bool(result) == expected
    else:
        with pytest.raises(pywildmatch.error.PywildmatchError) as e:
            pywildmatch.Ignore(pattern, flag)
        assert e.typename == expected

