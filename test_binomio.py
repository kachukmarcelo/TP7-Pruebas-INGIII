from Calculos import binomio
import pytest

def test_binomio():
    assert binomio(2,2) == 16


#TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
#TypeError: can't multiply sequence by non-int of type 'str'