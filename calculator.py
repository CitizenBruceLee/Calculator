"""
calculator.py
🧮 A state-of-the-art calculator that uses smilies instead of numbers and operations!
This calculator provides a fun, user-friendly CLI interface with visual feedback.
"""

import sys
import random
from typing import Dict, List, Tuple, Union


class SmileyCalculator:
    """A revolutionary calculator that uses smilies instead of numbers and operations."""
    
    def __init__(self):
        """Initialize the calculator with smiley mappings."""
        # Number mappings: Each smiley represents a number 0-9
        self.numbers = {
            '😀': 0,  # Grinning face
            '😊': 1,  # Smiling face with smiling eyes
            '😁': 2,  # Beaming face with smiling eyes
            '😂': 3,  # Face with tears of joy
            '😃': 4,  # Grinning face with big eyes
            '😄': 5,  # Grinning face with smiling eyes
            '😆': 6,  # Grinning squinting face
            '😇': 7,  # Smiling face with halo
            '😈': 8,  # Smiling face with horns
            '😉': 9,  # Winking face
        }
        
        # Operation mappings: Each smiley represents an operation
        self.operations = {
            '➕': 'add',        # Plus sign
            '➖': 'subtract',   # Minus sign
            '✖️': 'multiply',   # Heavy multiplication x
            '➗': 'divide',     # Heavy division sign
        }
        
        # Reverse mappings for display
        self.reverse_numbers = {v: k for k, v in self.numbers.items()}
        self.reverse_operations = {v: k for k, v in self.operations.items()}
        
        # Success/failure expressions
        self.success_expressions = ['🎉', '✨', '🌟', '💫', '🎊', '🔥', '👏', '🎈']
        self.thinking_expressions = ['🤔', '💭', '🧠', '⚡', '🔮']
        
    def add(self, a: float, b: float) -> float:
        """Add two numbers together."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero! 🚫")
        return a / b
    
    def smiley_to_number(self, smiley_string: str) -> float:
        """Convert a string of smiley digits to a number."""
        if not smiley_string:
            return 0
        
        # Handle decimal point
        if '.' in smiley_string:
            integer_part, decimal_part = smiley_string.split('.')
            integer_value = self._convert_smiley_digits(integer_part)
            decimal_value = self._convert_smiley_digits(decimal_part)
            return integer_value + decimal_value / (10 ** len(decimal_part))
        else:
            return self._convert_smiley_digits(smiley_string)
    
    def _convert_smiley_digits(self, smiley_string: str) -> float:
        """Convert smiley digits to numeric value."""
        result = 0
        for smiley in smiley_string:
            if smiley in self.numbers:
                result = result * 10 + self.numbers[smiley]
            elif smiley != '.':  # Ignore decimal point
                raise ValueError(f"Unknown smiley digit: {smiley}")
        return result
    
    def number_to_smiley(self, number: float) -> str:
        """Convert a number to smiley representation."""
        if number == int(number):
            number = int(number)
        
        number_str = str(number)
        smiley_result = ""
        
        for char in number_str:
            if char.isdigit():
                smiley_result += self.reverse_numbers[int(char)]
            elif char == '.':
                smiley_result += '.'
            elif char == '-':
                smiley_result += '➖'
        
        return smiley_result
    
    def get_operation_function(self, operation_smiley: str):
        """Get the operation function for a given smiley."""
        if operation_smiley not in self.operations:
            raise ValueError(f"Unknown operation: {operation_smiley}")
        
        operation_name = self.operations[operation_smiley]
        return getattr(self, operation_name)
    
    def calculate(self, num1_smiley: str, operation_smiley: str, num2_smiley: str) -> str:
        """Perform calculation with smiley inputs and return smiley result."""
        try:
            # Convert smiley inputs to numbers
            num1 = self.smiley_to_number(num1_smiley)
            num2 = self.smiley_to_number(num2_smiley)
            
            # Get operation function
            operation_func = self.get_operation_function(operation_smiley)
            
            # Perform calculation
            result = operation_func(num1, num2)
            
            # Convert result back to smiley
            return self.number_to_smiley(result)
        
        except Exception as e:
            raise ValueError(f"Calculation error: {e}")
    
    def get_help_text(self) -> str:
        """Return help text explaining the smiley system."""
        help_text = "\n🌟 Welcome to the Smiley Calculator! 🌟\n\n"
        help_text += "📚 SMILEY NUMBER SYSTEM:\n"
        for smiley, number in self.numbers.items():
            help_text += f"  {smiley} = {number}\n"
        
        help_text += "\n🔧 OPERATION SMILIES:\n"
        for smiley, operation in self.operations.items():
            help_text += f"  {smiley} = {operation}\n"
        
        help_text += "\n💡 EXAMPLES:\n"
        help_text += f"  {self.reverse_numbers[2]} ➕ {self.reverse_numbers[3]} = {self.reverse_numbers[5]} (2 + 3 = 5)\n"
        help_text += f"  {self.reverse_numbers[1]}{self.reverse_numbers[0]} ➖ {self.reverse_numbers[5]} = {self.reverse_numbers[5]} (10 - 5 = 5)\n"
        
        return help_text



def print_banner():
    """Print a beautiful banner for the calculator."""
    print("\n" + "="*50)
    print("🧮✨ SMILEY CALCULATOR ✨🧮")
    print("The world's first emoji-based calculator!")
    print("="*50)


def print_thinking_animation():
    """Show a thinking animation."""
    thinking = ['🤔', '💭', '🧠', '⚡']
    print("Calculating... ", end="")
    for emoji in thinking:
        print(emoji, end=" ")
        sys.stdout.flush()
    print()


def print_success_message():
    """Print a random success message."""
    success_emojis = ['🎉', '✨', '🌟', '💫', '🎊', '🔥', '👏', '🎈']
    print(f"\n{random.choice(success_emojis)} Result calculated successfully! {random.choice(success_emojis)}")


def validate_smiley_input(input_str: str, calc: SmileyCalculator, input_type: str) -> bool:
    """Validate user input for smiley numbers or operations."""
    try:
        if input_type == "number":
            # Check if all characters are valid number smilies or decimal point
            for char in input_str:
                if char not in calc.numbers and char != '.':
                    return False
            # Try to convert to ensure it's valid
            calc.smiley_to_number(input_str)
            return True
        elif input_type == "operation":
            return input_str in calc.operations
        return False
    except:
        return False


def get_user_input(prompt: str, calc: SmileyCalculator, input_type: str) -> str:
    """Get and validate user input with helpful error messages."""
    while True:
        user_input = input(prompt).strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            return 'quit'
        
        if user_input.lower() in ['help', 'h']:
            print(calc.get_help_text())
            continue
        
        if validate_smiley_input(user_input, calc, input_type):
            return user_input
        else:
            if input_type == "number":
                print("❌ Invalid number! Please use smiley digits only.")
                print("💡 Type 'help' to see the smiley number system.")
            elif input_type == "operation":
                print("❌ Invalid operation! Please use: ➕ ➖ ✖️ ➗")
                print("💡 Type 'help' to see available operations.")


def format_calculation_display(num1: str, op: str, num2: str, result: str, calc: SmileyCalculator) -> str:
    """Format the calculation in a beautiful display."""
    # Convert to regular numbers for reference
    num1_regular = calc.smiley_to_number(num1)
    num2_regular = calc.smiley_to_number(num2)
    result_regular = calc.smiley_to_number(result)
    op_name = calc.operations[op]
    
    display = f"""
┌─ 🧮 CALCULATION RESULT 🧮 ─┐
│                              │
│  {num1} {op} {num2} = {result}
│                              │
│  ({num1_regular} {op_name} {num2_regular} = {result_regular})
│                              │
└──────────────────────────────┘
"""
    return display


def interactive_mode(calc: SmileyCalculator):
    """Run the calculator in interactive mode."""
    print("\n🎮 Welcome to Interactive Mode!")
    print("✨ Enter 'help' anytime to see the smiley guide")
    print("✨ Enter 'quit' to exit")
    print("✨ Let's calculate with smilies! 🎉\n")
    
    while True:
        try:
            print("─" * 40)
            
            # Get first number
            num1 = get_user_input("Enter first number (smilies): ", calc, "number")
            if num1 == 'quit':
                break
            
            # Get operation
            operation = get_user_input("Enter operation (➕ ➖ ✖️ ➗): ", calc, "operation")
            if operation == 'quit':
                break
            
            # Get second number
            num2 = get_user_input("Enter second number (smilies): ", calc, "number")
            if num2 == 'quit':
                break
            
            # Show thinking animation
            print_thinking_animation()
            
            # Calculate result
            result = calc.calculate(num1, operation, num2)
            
            # Display result beautifully
            print_success_message()
            print(format_calculation_display(num1, operation, num2, result, calc))
            
            # Ask if user wants to continue
            print("\n🔄 Ready for another calculation!")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("💡 Type 'help' for guidance or 'quit' to exit.\n")


def demo_mode(calc: SmileyCalculator):
    """Run a demonstration of the calculator."""
    print("\n🎭 DEMO MODE - Watch the magic happen! 🎭\n")
    
    # Demo calculations
    demos = [
        ("", "➕", "😃", "2 + 4 = 6"),
        ("😈", "➖", "😃", "8 - 4 = 4"),
        ("😁", "✖️", "😄", "2 × 5 = 10"),
        ("😉", "➗", "�", "9 ÷ 3 = 3"),
        ("😊😀", "➕", "😄", "10 + 5 = 15"),
    ]
    
    for i, (num1, op, num2, description) in enumerate(demos, 1):
        print(f"Demo {i}: {description}")
        print(f"Smiley: {num1} {op} {num2}")
        
        try:
            result = calc.calculate(num1, op, num2)
            print(f"Result: {result}")
            print(format_calculation_display(num1, op, num2, result, calc))
        except Exception as e:
            print(f"Error in demo: {e}")
        
        if i < len(demos):
            try:
                input("Press Enter for next demo...")
            except EOFError:
                break
        
        print("\n" + "─" * 50 + "\n")


def main():
    """Main function to run the smiley calculator."""
    calc = SmileyCalculator()
    
    print_banner()
    print(calc.get_help_text())
    
    while True:
        print("\n🎯 Choose your adventure:")
        print("1. 🎮 Interactive Mode - Calculate with smilies!")
        print("2. 🎭 Demo Mode - Watch examples")
        print("3. 📚 Show Help - Learn the smiley system")
        print("4. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            interactive_mode(calc)
        elif choice == '2':
            demo_mode(calc)
        elif choice == '3':
            print(calc.get_help_text())
        elif choice == '4':
            print("\n🎉 Thanks for using the Smiley Calculator!")
            print("😊 Have a great day! 😊")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
