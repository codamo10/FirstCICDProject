import pytest
from src.project import x

def test_area_cuadrado():
    assert x(3) == 9
    assert x(4) == 16
    assert x(8.4) == 70.56
    
def test_area_cuadrado_string():
    with pytest.raises(TypeError):
        x("56")


def test_area_cuadrado_list():
    with pytest.raises(TypeError):
        x([43])

def test_area_cuadrado_negative():
    with pytest.raises(TypeError):
        x(-7)


