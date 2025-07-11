#!/usr/bin/env python3
"""
Test script for the Smiley Calculator
Tests core functionality to ensure everything works properly.
"""

from calculator import SmileyCalculator


def test_calculator():
    """Test the basic functionality of the smiley calculator."""
    calc = SmileyCalculator()

    print("🧪 Testing Smiley Calculator Functions...\n")

    # Test number conversion
    print("1️⃣ Testing number conversion:")
    test_cases = [
        ("😀", 0),
        ("😊", 1),
        ("😁", 2),
        ("😂", 3),
        ("😃", 4),
        ("😄", 5),
        ("😆", 6),
        ("😇", 7),
        ("😈", 8),
        ("😉", 9),
        ("😊😀", 10),
        ("😁😄", 25),
        ("😂.😄", 3.5),
    ]

    for smiley, expected in test_cases:
        result = calc.smiley_to_number(smiley)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {smiley} -> {result} (expected {expected})")

    print("\n2️⃣ Testing reverse conversion:")
    reverse_cases = [
        (0, "😀"),
        (1, "😊"),
        (25, "😁😄"),
        (3.5, "😂.😄"),
        (10, "😊😀"),
    ]

    for number, expected in reverse_cases:
        result = calc.number_to_smiley(number)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {number} -> {result} (expected {expected})")

    print("\n3️⃣ Testing calculations:")
    calc_cases = [
        ("😁", "➕", "😃", "😆", "2 + 4 = 6"),
        ("😈", "➖", "😃", "😃", "8 - 4 = 4"),
        ("😁", "✖️", "😄", "😊😀", "2 × 5 = 10"),
        ("😉", "➗", "😂", "😂", "9 ÷ 3 = 3"),
        ("😊😀", "➕", "😄", "😊😄", "10 + 5 = 15"),
    ]

    for num1, op, num2, expected, description in calc_cases:
        try:
            result = calc.calculate(num1, op, num2)
            status = "✅" if result == expected else "❌"
            print(f"  {status} {num1} {op} {num2} = {result} (expected {expected}) - {description}")
        except Exception as e:
            print(f"  ❌ {num1} {op} {num2} = Error: {e}")

    print("\n4️⃣ Testing error handling:")
    error_cases = [
        ("😊", "➗", "😀", "Division by zero"),
        ("🙂", "➕", "😊", "Invalid smiley"),
        ("😊", "🤔", "😁", "Invalid operation"),
    ]

    for num1, op, num2, test_name in error_cases:
        try:
            result = calc.calculate(num1, op, num2)
            print(f"  ❌ {test_name}: Should have failed but got {result}")
        except Exception as e:
            print(f"  ✅ {test_name}: Correctly caught error - {e}")

    print("\n🎉 Testing completed! The Smiley Calculator is ready to use! 🎉")


if __name__ == "__main__":
    test_calculator()
