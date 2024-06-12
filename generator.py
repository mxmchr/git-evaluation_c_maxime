import random

def generate_expression():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    operator = random.choice(['+', '-', '*', '/'])
    expression = f"{num1}{operator}{num2}"
    return expression

expression = generate_expression()

print(expression)
