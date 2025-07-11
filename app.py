#!/usr/bin/env python3
"""
app.py
Flask web application for the Smiley Calculator
Provides a beautiful web interface with clickable smiley buttons
"""

from flask import Flask, render_template, request, jsonify
import json
from calculator import SmileyCalculator

app = Flask(__name__)
calc = SmileyCalculator()


@app.route("/")
def index():
    """Main page with the calculator interface."""
    return render_template(
        "index.html",
        numbers=calc.numbers,
        operations=calc.operations,
        reverse_numbers=calc.reverse_numbers,
        reverse_operations=calc.reverse_operations,
    )


@app.route("/calculate", methods=["POST"])
def calculate():
    """Handle calculation requests."""
    try:
        data = request.json
        num1 = data.get("num1", "")
        operation = data.get("operation", "")
        num2 = data.get("num2", "")

        if not num1 or not operation or not num2:
            return jsonify({"success": False, "error": "Please enter both numbers and select an operation"})

        # Perform calculation
        result = calc.calculate(num1, operation, num2)

        # Convert to regular numbers for display
        num1_regular = calc.smiley_to_number(num1)
        num2_regular = calc.smiley_to_number(num2)
        result_regular = calc.smiley_to_number(result)
        op_name = calc.operations[operation]

        return jsonify(
            {
                "success": True,
                "result": result,
                "calculation": {
                    "num1": num1,
                    "operation": operation,
                    "num2": num2,
                    "result": result,
                    "num1_regular": num1_regular,
                    "num2_regular": num2_regular,
                    "result_regular": result_regular,
                    "operation_name": op_name,
                },
            }
        )

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/help")
def help_page():
    """Help page with smiley guide."""
    return render_template("help.html", numbers=calc.numbers, operations=calc.operations)


@app.route("/api/convert", methods=["POST"])
def convert_number():
    """Convert between smiley and regular numbers."""
    try:
        data = request.json
        if "smiley" in data:
            # Convert smiley to number
            number = calc.smiley_to_number(data["smiley"])
            return jsonify({"success": True, "number": number})
        elif "number" in data:
            # Convert number to smiley
            smiley = calc.number_to_smiley(data["number"])
            return jsonify({"success": True, "smiley": smiley})
        else:
            return jsonify({"success": False, "error": "Invalid input"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    print("🚀 Starting Smiley Calculator Web App...")
    print("🌐 Open your browser and go to: http://127.0.0.1:5000")
    print("✨ Enjoy calculating with smilies!")
    app.run(debug=False, host="127.0.0.1", port=5000)
