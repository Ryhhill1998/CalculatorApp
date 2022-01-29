from calculator_functions import add, subtract, multiply, divide


class CalculatorBrain:

    def __init__(self):

        self.answer = 0
        self.num1 = 1
        self.num2 = 1
        self.operation = ""
        self.operation_dict = {
            "+": add,
            "-": subtract,
            "/": divide,
            "*": multiply
        }

    def perform_calculation(self):
        print(self.num1, self.operation, self.num2)
        calculate = self.operation_dict[self.operation]
        self.answer = calculate(self.num1, self.num2)
        self.num1 = self.answer
        self.num2 = 1
        self.operation = "*"
