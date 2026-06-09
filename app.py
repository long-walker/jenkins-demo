def add_numbers(a, b):
    return a - b  # ❌ Bug introduced: subtracting instead of adding!

if __name__ == "__main__":
    print(f"Result of 5 + 10 is: {add_numbers(5, 10)}")
