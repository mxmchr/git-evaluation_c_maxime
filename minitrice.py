import sys
import re

def read_input():
    user_input = sys.stdin.readline().rstrip("\n")
    print("Input received:", user_input)
    return user_input

def calculate(expression):
    pattern = re.compile(r"(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)")
    match = pattern.fullmatch(expression.strip())
    if not match:
        return "Error: Invalid expression"

    num1, operator, num2 = match.groups()
    num1 = float(num1)
    num2 = float(num2)

    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2

if __name__ == "__main__":
    user_input = read_input()
    result = calculate(user_input)
    print("Result:", result)
