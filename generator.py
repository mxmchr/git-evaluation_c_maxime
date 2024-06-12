import random
import sys

def generate_expression():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    operator = random.choice(['+', '-', '*', '/'])
    expression = f"{num1} {operator} {num2}"
    return expression

if len(sys.argv) != 2:
    print("Usage: python3 generator.py <nombre d'expressions voulu>")
    sys.exit(1)

try:
    num_expressions = int(sys.argv[1])
except ValueError:
    print("Le nombre d'expressions doit être un entier.")
    sys.exit(1)

for _ in range(num_expressions):
    expression = generate_expression()
    print(expression)
