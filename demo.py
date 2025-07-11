#!/usr/bin/env python3
"""
Quick demonstration of the Smiley Calculator
Shows how to use the calculator programmatically for integration into other projects.
"""

from calculator import SmileyCalculator


def main():
    """Demonstrate the Smiley Calculator functionality."""
    print("🎯 Smiley Calculator - Quick Demo\n")

    # Create calculator instance
    calc = SmileyCalculator()

    # Show the mapping
    print("🔢 Number Mapping:")
    for smiley, number in calc.numbers.items():
        print(f"  {smiley} = {number}")

    print("\n🔧 Operation Mapping:")
    for smiley, operation in calc.operations.items():
        print(f"  {smiley} = {operation}")

    print("\n📊 Sample Calculations:")

    # Example calculations
    examples = [
        ("😁", "➕", "😃", "2 + 4"),
        ("😈", "➖", "😃", "8 - 4"),
        ("😁", "✖️", "😄", "2 × 5"),
        ("😉", "➗", "😂", "9 ÷ 3"),
        ("😊😀", "➕", "😄", "10 + 5"),
        ("😂.😄", "✖️", "😁", "3.5 × 2"),
    ]

    for num1, op, num2, description in examples:
        try:
            result = calc.calculate(num1, op, num2)

            # Convert to regular numbers for verification
            n1 = calc.smiley_to_number(num1)
            n2 = calc.smiley_to_number(num2)
            res = calc.smiley_to_number(result)

            print(f"  {num1} {op} {num2} = {result}")
            print(f"    ({n1} {calc.operations[op]} {n2} = {res}) - {description}")
            print()
        except Exception as e:
            print(f"  Error: {e}")

    print("🎉 Demo completed! The Smiley Calculator is ready for use!")
    print("🚀 Run 'python calculator.py' to start the interactive calculator!")


if __name__ == "__main__":
    main()
