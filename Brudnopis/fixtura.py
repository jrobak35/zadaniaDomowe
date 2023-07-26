import pytest

# Definicja fixtury
@pytest.fixture()
def przygotowanie_danych():
    dane = [1, 2, 3, 4]
    return dane

# Test wykorzystujacy fixture
def test_suma(przygotowanie_danych):
    suma = sum(przygotowanie_danych)
    assert suma == 10

# Inny test, rowniez wykorzystujacy fixture
def test_dlugosc_listy(przygotowanie_danych):
    dlugosc = len(przygotowanie_danych)
    assert dlugosc == 2