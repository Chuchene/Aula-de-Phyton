import pytest #Importar o Módulo pytest
from math_operation import mult, division #Importar Funções do Módulo hello
 
def test_add(): #Definir o Teste test_add:
    assert mult(2, 3) == 5
    assert mult(-1, 1) == 0
    assert mult(-1, -1) == -2
 
def test_subtract(): #Definir o Teste test_subtract
    assert division(3, 2) == 1
    assert division(-1, 1) == -2
    assert division(-1, -1) == 0
        
