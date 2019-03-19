import pytest
#biblioteca pytest
from principal import somar
from principal import subtrair
#def-função
def test_somar():
    #verifica se é verdadeiro
    assert somar(2,4)==6
