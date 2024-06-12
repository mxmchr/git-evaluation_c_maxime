import sys
import re

def read_input():
    if sys.stdin.isatty():
        user_input = input("Enter expressions (press Enter twice to finish):\n")
        if user_input.strip() == "":
            return []
        return [user_input]
    else:
        return sys.stdin.readlines()

def calculate(expression):
    results = []
    pattern = re.compile(r"(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)")

    for exp in expression:
        match = pattern.fullmatch(exp.strip())
        if not match:
            results.append("Error: Invalid expression")
            continue

        num1, operator, num2 = match.groups()
        num1 = float(num1)
        num2 = float(num2)

        if operator == "+":
            results.append(num1 + num2)
        elif operator == "-":
            results.append(num1 - num2)
        elif operator == "*":
            results.append(num1 * num2)
        elif operator == "/":
            if num2 == 0:
                results.append("Error: Division by zero")
            else:
                results.append(num1 / num2)

    return results

if __name__ == "__main__":
    user_input = read_input()
    results = calculate(user_input)
    print("Results:", results)
