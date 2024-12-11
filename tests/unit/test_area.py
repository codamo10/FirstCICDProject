import pytest
from src.project import area_cuadrado

def test_calculate_area_square():
    assert area_cuadrado(2) == 4
    assert area_cuadrado(2.5) == 6.25

def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        area_cuadrado(-2)

def test_calculate_area_square_string():
    with pytest.raises(TypeError):
        area_cuadrado("2")

def test_calculate_area_square_list():
    with pytest.raises(TypeError):
        area_cuadrado([2])
        
