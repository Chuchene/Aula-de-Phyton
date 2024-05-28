import pytest #Importar o Módulo pytest
from math_operation import mult, division #Importar Funções do Módulo hello
 
def test_add(): #Definir o Teste test_add:
    assert mult(2, 3) == 6
    assert mult(5, 5) == 25
    assert mult(15, 3) == 45
 
def test_subtract(): #Definir o Teste test_subtract
    assert division(3, 3) == 1
    assert division(6, 2) == 2
    assert division(10, 2) == 5
        
