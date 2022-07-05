from Calculos import cuadrado
import pytest

def test_cuadrado():
    assert cuadrado(2) == 4

@pytest.mark.parametrize(
    "valor_a, resultado",
    [
        (-2,4),
        (0,0),
        (1,1),
        (None,None),
        ("2",None),
    ]
)

def test_potencia_parametrizada(valor_a, resultado):
    assert cuadrado(valor_a) == resultado

#TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
#TypeError: can't multiply sequence by non-int of type 'str'