import pytest
from src.project import cuadrado_area

def test_cuadrado_area():
    assert cuadrado_area(3) == 9
    assert cuadrado_area(4) == 16
    assert cuadrado_area(8.4) == 70.56
    
def test_cuadrado_area_string():
    with pytest.raises(TypeError):
        cuadrado_area("56")


def test_cuadrado_area_list():
    with pytest.raises(TypeError):
        cuadrado_area([43])

def test_cuadrado_area_negative():
    with pytest.raises(TypeError):
        cuadrado_area(-7)


