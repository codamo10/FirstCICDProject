import pytest
from src.project import area_cuadrado

def test_area_cuadrado():
    assert area_cuadrado(3) == 9
    assert area_cuadrado(4) == 16
    assert area_cuadrado(8.4) == 70.56
    
def test_area_cuadrado_string():
    with pytest.raises(TypeError):
        area_cuadrado("56")


def test_cuadrado_area_list():
    with pytest.raises(TypeError):
        area_cuadrado([43])

def test_area_cuadrado_negative():
    with pytest.raises(TypeError):
        area_cuadrado(-7)


