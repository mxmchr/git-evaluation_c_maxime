import sys

def read_input():
    user_input = sys.stdin.readline().rstrip("\n")
    print("Input received:", user_input)
    return user_input

if __name__ == "__main__":
    read_input()
