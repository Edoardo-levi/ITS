from my_project.calculator import *
import pytest

@pytest.fixture
def calculation():
    return Calculator(10,5)
def test_addition(calculation):
    
    assert calculation.addition() == 15,'The sum is wrong'

def test_subtraction(calculation):
    
    assert calculation.subtraction() == 5, 'The subrtraction is wrong'

def test_multiplication(calculation):

    assert calculation.multiplication() == 50, 'The multiplication is wrong'

def test_divisioncalculation(calculation):
    
    assert calculation.division() == 2.00, 'The quotient is wrong'