from abc import ABC, abstractmethod
import logging
import sys


class Operation(ABC):
    @abstractmethod
    def operate(self, x, y):
        pass


class Add(Operation):
    def operate(self, x, y):
        result = x + y
        logging.info(f"Add: {x} + {y} = {result}")
        return result


class Subtract(Operation):
    def operate(self, x, y):
        result = x - y
        logging.info(f"Subtract: {x} - {y} = {result}")
        return result


class Multiply(Operation):
    def operate(self, x, y):
        result = x * y
        logging.info(f"Multiply: {x} * {y} = {result}")
        return result


class Divide(Operation):
    def operate(self, x, y):
        try:
            result = x / y
            logging.info(f"Divide: {x} / {y} = {result}")
            return result
        except ZeroDivisionError:
            logging.error("Division by zero")
            return "Ошибка. Вы все еще делите на ноль?"


class CalculatorModel:
    def calculate(self, operation, x, y):
        return operation.operate(x, y)


class CalculatorView:
    def input_number(self, prompt):
        return float(input(prompt))

    def output_result(self, result):
        print(f"Результат: {result}")


class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        x = self.view.input_number("Введите первое число: ")
        y = self.view.input_number("Введите второе число: ")
        operation = input("Выберите операцию (+, -, *, /): ")

        if operation == "+":
            result = self.model.calculate(Add(), x, y)
        elif operation == "-":
            result = self.model.calculate(Subtract(), x, y)
        elif operation == "*":
            result = self.model.calculate(Multiply(), x, y)
        elif operation == "/":
            result = self.model.calculate(Divide(), x, y)
        else:
            result = "Некорректная операция"

        self.view.output_result(result)


# Настройка логгера
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Запись лога в файл
file_handler = logging.FileHandler('calculator.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Вывод лога в консоль
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Запуск программы
if __name__ == "__main__":
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    controller.run()