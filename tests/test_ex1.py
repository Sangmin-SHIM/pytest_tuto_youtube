import pytest

@pytest.fixture(scope="session")
def fixture_1():
    print('run-fixture-1')
    return 1

def test_fixture_example1(fixture_1):
    print('run-test_fixture-1')
    num = fixture_1
    assert num == 1

def test_fixture_example2(fixture_1):
    print('run-test_fixture-2')
    num = fixture_1
    assert num == 1


@pytest.mark.skip
def test_example():
    assert 1 == 1 

def test_example1():
    assert 2 == 2 

@pytest.mark.slow
def test_example2():
    print("test_example2 quoi")
    assert 3 == 3    

def test_example3():
    assert 8 == 8