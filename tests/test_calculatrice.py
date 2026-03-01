from src.calculatrice import addition, soustraction, multiplication, division


def test_addition():
    resultat = addition(2, 3)
    assert resultat == 5


def test_soustraction():
    resultat = soustraction(10, 4)
    assert resultat == 6


def test_multiplication():
    resultat = multiplication(3, 4)
    assert resultat == 12


def test_division():
    resultat = division(10, 2)
    assert resultat == 5


def test_division():
    resultat = division(10, 2)
    assert resultat == 5
