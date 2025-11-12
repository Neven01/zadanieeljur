import copy
import random

class Polynomial:
    """Класс полинома на основе односвязного списка с внутренним классом"""
    
    class _Node:
        """Внутренний класс для узла списка"""
        def __init__(self, coefficient, exponent, next_node=None):
            self.coefficient = coefficient
            self.exponent = exponent
            self.next = next_node
        
        def __str__(self):
            if self.exponent == 0:
                return f"{self.coefficient}"
            elif self.exponent == 1:
                return f"{self.coefficient}x"
            else:
                return f"{self.coefficient}x^{self.exponent}"
    
    def __init__(self, coefficients=None):
        self.head = None
        self._size = 0
        
        if coefficients:
            for exp, coef in enumerate(coefficients):
                if coef != 0:
                    self.add_term(coef, exp)
    
    def add_term(self, coefficient, exponent):
        """Добавление члена полинома"""
        if coefficient == 0:
            return
        
        new_node = self._Node(coefficient, exponent)
        
        # Если список пуст или добавляем член с наибольшей степенью
        if self.head is None or exponent > self.head.exponent:
            new_node.next = self.head
            self.head = new_node
            self._size += 1
        else:
            current = self.head
            prev = None
            
            # Поиск позиции для вставки
            while current and current.exponent > exponent:
                prev = current
                current = current.next
            
            # Если член с такой степенью уже существует
            if current and current.exponent == exponent:
                current.coefficient += coefficient
                if current.coefficient == 0:  # Удаляем нулевой член
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                    self._size -= 1
            else:
                # Вставка нового узла
                new_node.next = current
                if prev:
                    prev.next = new_node
                else:
                    self.head = new_node
                self._size += 1
    
    def __add__(self, other):
        """Сложение полиномов"""
        result = Polynomial()
        
        # Копируем первый полином
        current = self.head
        while current:
            result.add_term(current.coefficient, current.exponent)
            current = current.next
        
        # Добавляем второй полином
        current = other.head
        while current:
            result.add_term(current.coefficient, current.exponent)
            current = current.next
        
        return result
    
    def __mul__(self, other):
        """Умножение полиномов"""
        result = Polynomial()
        
        current_self = self.head
        while current_self:
            current_other = other.head
            while current_other:
                coef = current_self.coefficient * current_other.coefficient
                exp = current_self.exponent + current_other.exponent
                result.add_term(coef, exp)
                current_other = current_other.next
            current_self = current_self.next
        
        return result
    
    def __eq__(self, other):
        """Сравнение полиномов на равенство"""
        if self._size != other._size:
            return False
        
        current_self = self.head
        current_other = other.head
        
        while current_self and current_other:
            if (current_self.coefficient != current_other.coefficient or 
                current_self.exponent != current_other.exponent):
                return False
            current_self = current_self.next
            current_other = current_other.next
        
        return current_self is None and current_other is None
    
    def differentiate(self):
        """Дифференцирование полинома"""
        result = Polynomial()
        current = self.head
        
        while current:
            if current.exponent > 0:
                new_coef = current.coefficient * current.exponent
                new_exp = current.exponent - 1
                result.add_term(new_coef, new_exp)
            current = current.next
        
        return result
    
    def clone(self):
        """Реализация паттерна Прототип - создание копии"""
        return copy.deepcopy(self)
    
    def __str__(self):
        """Строковое представление полинома"""
        if self.head is None:
            return "0"
        
        terms = []
        current = self.head
        
        while current:
            terms.append(str(current))
            current = current.next
        
        result = " + ".join(terms)
        return result.replace("+ -", "- ")
    
    def to_list(self):
        """Представление полинома в виде списка коэффициентов"""
        if self.head is None:
            return []
        
        max_exp = self.head.exponent
        result = [0] * (max_exp + 1)
        
        current = self.head
        while current:
            result[current.exponent] = current.coefficient
            current = current.next
        
        return result


# Демонстрационная программа
def demonstrate_polynomial_operations():
    """Демонстрация операций с полиномами"""
    
    print("=== ДЕМОНСТРАЦИЯ ОПЕРАЦИЙ С ПОЛИНОМАМИ ===\n")
    
    # Создание случайных полиномов
    def create_random_polynomial(max_degree=3):
        coefficients = [random.randint(-5, 5) for _ in range(random.randint(2, max_degree + 1))]
        return Polynomial(coefficients)
    
    # Создание и вывод случайных полиномов
    p1 = create_random_polynomial()
    p2 = create_random_polynomial()
    
    print(f"Полином 1: {p1}")
    print(f"Полином 2: {p2}")
    print()
    
    # Сложение
    sum_poly = p1 + p2
    print(f"Сумма: {p1} + {p2} = {sum_poly}")
    
    # Умножение
    product_poly = p1 * p2
    print(f"Произведение: ({p1}) * ({p2}) = {product_poly}")
    
    # Сравнение
    p3 = Polynomial(p1.to_list())  # Копия p1
    print(f"Полином 1 == Копия полинома 1: {p1 == p3}")
    print(f"Полином 1 == Полином 2: {p1 == p2}")
    
    # Дифференцирование
    derivative_p1 = p1.differentiate()
    derivative_p2 = p2.differentiate()
    print(f"Производная полинома 1: {derivative_p1}")
    print(f"Производная полинома 2: {derivative_p2}")


# Демонстрация паттерна Прототип
def demonstrate_prototype():
    print("\n=== ДЕМОНСТРАЦИЯ ПАТТЕРНА ПРОТОТИП ===")
    
    original = Polynomial([1, 2, 3])  # 3x² + 2x + 1
    prototype_clone = original.clone()
    
    print(f"Оригинал: {original}")
    print(f"Клон: {prototype_clone}")
    print(f"Оригинал == Клон: {original == prototype_clone}")
    
    # Модифицируем клон
    prototype_clone.add_term(4, 3)  # Добавляем 4x³
    print(f"\nПосле модификации клона:")
    print(f"Оригинал: {original}")
    print(f"Клон: {prototype_clone}")
    print(f"Оригинал == Клон: {original == prototype_clone}")


# Тесты
def test_polynomial():
    """Простая функция тестирования"""
    print("\n=== ТЕСТИРОВАНИЕ ===")
    
    # Тест создания
    p1 = Polynomial([2, 3, 1])  # 1x² + 3x + 2
    print(f"Тест создания: {p1}")
    
    # Тест сложения
    p2 = Polynomial([4, 5, 6])  # 6x² + 5x + 4
    result = p1 + p2            # 7x² + 8x + 6
    print(f"Тест сложения: {p1} + {p2} = {result}")
    
    # Тест умножения
    p3 = Polynomial([1, 1])     # x + 1
    p4 = Polynomial([1, 1])     # x + 1
    result_mul = p3 * p4        # x² + 2x + 1
    print(f"Тест умножения: ({p3}) * ({p4}) = {result_mul}")
    
    # Тест дифференцирования
    p5 = Polynomial([1, 2, 3])  # 3x² + 2x + 1
    derivative = p5.differentiate()  # 6x + 2
    print(f"Тест дифференцирования: производная от {p5} = {derivative}")
    
    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    # Запуск демонстрации
    demonstrate_polynomial_operations()
    demonstrate_prototype()
    test_polynomial()