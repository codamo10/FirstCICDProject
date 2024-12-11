import pytest
from src.project import cuadrado_area

def cuadrado_area_prueba():
    assert cuadrado_area(3) == 9
    assert cuadrado_area(4) == 16
    assert cuadrado_area(8.4) == 70.56
    
def cuadrado_area_prueba_string():
    with pytest.raises(TypeError):
        cuadrado_area("56")


def cuadrado_area_prueba_lista():
    with pytest.raises(TypeError):
        cuadrado_area([43])

def cuadrado_area_prueba_neg():
    with pytest.raises(TypeError):
        cuadrado_area(-7)


