from app import add_numbers


def test_addition():
    # This checks if our function works correctly
    assert add_numbers(2, 3) == 5
    print("✅ Unit test passed successfully!")


if __name__ == "__main__":
    test_addition()
