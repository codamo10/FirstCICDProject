import pytest
from src.project import get_area

def test_area_cuadrado():
    assert get_area(3) == 9
    assert get_area(4) == 16
    assert get_area(8.4) == 70.56
    
def test_area_cuadrado_string():
    with pytest.raises(TypeError):
        get_area("56")


def test_area_cuadrado_list():
    with pytest.raises(TypeError):
        get_area([43])

def test_area_cuadrado_negative():
    with pytest.raises(TypeError):
        get_area(-7)


