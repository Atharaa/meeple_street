import pytest
from maths.algebra import multiplication
from maths.algebra import addition
from maths.algebra import soustraction
from maths.algebra import division


def test_multiplication():
    assert 4 == multiplication(2,2)
    assert 21 == multiplication(3,7)
    assert 4 == addition(2,2)
    assert 0 == soustraction(2,2)
    assert 1 == division(2,2)