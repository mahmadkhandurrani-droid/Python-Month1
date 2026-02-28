
print("Hello, World!")
# main.py - Month 1 Hub

import json
import os

# Import your modules
from calculator import add, subtract, multiply, divide, power, square_root, percentage

from number_toolkit_utils import is_prime, factors, fibonacci
from string_analyzer_utils import count_vowels, reverse_sentence, is_palindrome

# ---------------- History for Calculator ----------------
HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Calculator history corrupted. Starting fresh.")
            return []
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def add_to_history(history, operation, result):
    record = f"{operation} = {result}"
    history.append(record)
    save_history(history)

def show_history(history):
    if not history:
        print("No history available.")
    else:
        print("\n--- Calculation History ---")
        for item in history:
            print(item)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a valid number.")

# ---------------- Month 1 Combined Menu ----------------
def main():
    calc_history = load_history()

    while True:
        print("\n=== Month 1 Python Hub ===")
        print("1. Smart Calculator")
        print("2. Number Toolkit")
        print("3. String Analyzer")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            run_calculator(calc_history)
        elif choice == "2":
            run_number_toolkit()
        elif choice == "3":
            run_string_analyzer()
        elif choice == "4":
            print("Goodbye! Keep learning Marie Curie style 🚀")
            break
        else:
            print("Invalid choice. Enter 1-4.")

# ---------------- Calculator ----------------
def run_calculator(history):
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
        "5": ("Power", power),
        "6": ("Square Root", square_root),
        "7": ("Percentage", percentage)
    }

    while True:
        print("\n--- Smart Calculator ---")
        print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Power 6.Square Root 7.Percentage")
        print("8.Show History 9.Back to Month 1 Hub")
        choice = input("Choose an option (1-9): ")

        if choice == "9":
            break
        elif choice == "8":
            show_history(history)
            continue
        elif choice not in operations:
            print("Invalid choice. Select 1-7, 8, or 9.")
            continue

        op_name, func = operations[choice]
        try:
            if choice == "6":  # Square Root
                num = get_number("Enter number: ")
                result = func(num)
                op_str = f"√{num}"
            elif choice == "7":  # Percentage
                num1 = get_number("Enter percentage: ")
                num2 = get_number("Enter number: ")
                result = func(num1, num2)
                op_str = f"{num1}% of {num2}"
            else:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                result = func(num1, num2)
                symbols = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "**"}
                op_str = f"{num1} {symbols[choice]} {num2}"

            print(f"Result: {result}")
            add_to_history(history, op_str, result)

        except (ZeroDivisionError, ValueError) as e:
            print(f"Error: {e}")

# ---------------- Number Toolkit ----------------
def run_number_toolkit():
    while True:
        print("\n--- Number Toolkit ---")
        print("1. Prime Checker 2. Factor Finder 3. Fibonacci Generator 4.Back to Month 1 Hub")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            num = int(input("Enter a number to check if it is prime: "))
            print(f"{num} is prime." if is_prime(num) else f"{num} is not prime.")
        elif choice == "2":
            num = int(input("Enter a number to find its factors: "))
            print(f"Factors of {num}: {factors(num)}")
        elif choice == "3":
            n = int(input("Enter how many Fibonacci numbers to generate: "))
            print(f"First {n} Fibonacci numbers: {fibonacci(n)}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Enter 1-4.")

# ---------------- String Analyzer ----------------
def run_string_analyzer():
    while True:
        print("\n--- String Analyzer ---")
        print("1. Count Vowels 2. Reverse Sentence 3. Palindrome Check 4.Back to Month 1 Hub")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            s = input("Enter a sentence: ")
            print(f"Number of vowels: {count_vowels(s)}")
        elif choice == "2":
            s = input("Enter a sentence: ")
            print(f"Reversed sentence: {reverse_sentence(s)}")
        elif choice == "3":
            s = input("Enter a sentence: ")
            print(f"'{s}' is a palindrome." if is_palindrome(s) else f"'{s}' is not a palindrome.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Enter 1-4.")

# ---------------- Run Hub ----------------
if __name__ == "__main__":
    main()
