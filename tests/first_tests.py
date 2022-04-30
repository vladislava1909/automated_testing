import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_calculate_correctly(self):  # Проверка умножения
        assert self.calculator.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):  # Проверка деления
        assert self.calculator.division(self, 6, 2) == 3

    def test_subtraction_calculate_correctly(self):  # Проверка вычитания
        assert self.calculator.subtraction(self, 7, 2) == 5

    def test_adding_calculate_correctly(self):  # Проверка сложения
        assert self.calculator.adding(self, 8, 2) == 10
