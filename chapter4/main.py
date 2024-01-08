class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self

    def subtract(self, num):
        self.result -= num
        return self

    def multiply(self, num):
        self.result *= num
        return self

    def divide(self, num):
        self.result /= num
        return self

    def end(self):
        return self.result


calculator = Calculator()

print(calculator.result)
while True:
    choice = input(": ")
    if choice == "+":
        calculator.add(int(input(": ")))
    elif choice == "-":
        calculator.subtract(int(input(": ")))
    elif choice == "*":
        calculator.multiply(int(input(": ")))
    elif choice == "/":
        try:
            calculator.divide(int(input()))
        except ZeroDivisionError:
            print("Invalid 0")
    elif choice == "=":
        print(calculator.end())
        break
    else:
        break
