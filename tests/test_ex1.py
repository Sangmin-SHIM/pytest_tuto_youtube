import pytest

@pytest.mark.skip
def test_example():
    assert 1 == 1 

def test_example1():
    assert 1 == 1 

@pytest.mark.slow
def test_example2():
    print("test_example2 quoi")
    assert 1 == 1     

def test_example3():
    assert 1 == 1