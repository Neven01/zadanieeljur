import pytest
from polynomial import Polynomial  # предполагая, что основной код в polynomial.py

class TestPolynomial:
    def test_creation(self):
        p = Polynomial([2, 3, 1])  # 1x² + 3x + 2
        assert str(p) == "1x^2 + 3x + 2"
    
    def test_addition(self):
        p1 = Polynomial([1, 2, 3])  # 3x² + 2x + 1
        p2 = Polynomial([4, 5, 6])  # 6x² + 5x + 4
        result = p1 + p2            # 9x² + 7x + 5
        assert str(result) == "9x^2 + 7x + 5"
    
    def test_multiplication(self):
        p1 = Polynomial([1, 1])     # x + 1
        p2 = Polynomial([1, 1])     # x + 1
        result = p1 * p2            # x² + 2x + 1
        assert str(result) == "1x^2 + 2x + 1"
    
    def test_equality(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 2, 3])
        p3 = Polynomial([1, 2, 4])
        assert p1 == p2
        assert p1 != p3
    
    def test_differentiation(self):
        p = Polynomial([1, 2, 3])  # 3x² + 2x + 1
        derivative = p.differentiate()  # 6x + 2
        assert str(derivative) == "6x + 2"
    
    def test_zero_polynomial(self):
        p = Polynomial()
        assert str(p) == "0"
        derivative = p.differentiate()
        assert str(derivative) == "0"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])