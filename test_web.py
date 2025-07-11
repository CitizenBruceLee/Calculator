#!/usr/bin/env python3
"""
test_web.py
Test script for the web version of the Smiley Calculator
"""

import requests
import json
import sys


def test_web_calculator():
    """Test the web calculator API endpoints."""
    base_url = "http://127.0.0.1:5000"

    print("🧪 Testing Smiley Calculator Web API...\n")

    # Test if server is running
    try:
        response = requests.get(base_url, timeout=2)
        if response.status_code == 200:
            print("✅ Server is running successfully!")
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("❌ Server is not running. Please start it with: python app.py")
        return False

    # Test calculation endpoint
    print("\n🔢 Testing calculation endpoint:")

    test_cases = [
        {"data": {"num1": "😁", "operation": "➕", "num2": "😃"}, "expected": "😆", "description": "2 + 4 = 6"},
        {"data": {"num1": "😈", "operation": "➖", "num2": "😃"}, "expected": "😃", "description": "8 - 4 = 4"},
        {"data": {"num1": "😁", "operation": "✖️", "num2": "😄"}, "expected": "😊😀", "description": "2 × 5 = 10"},
        {"data": {"num1": "😉", "operation": "➗", "num2": "😂"}, "expected": "😂", "description": "9 ÷ 3 = 3"},
    ]

    for test in test_cases:
        try:
            response = requests.post(f"{base_url}/calculate", json=test["data"], headers={"Content-Type": "application/json"}, timeout=5)

            if response.status_code == 200:
                result = response.json()
                if result["success"] and result["result"] == test["expected"]:
                    print(
                        f"  ✅ {test['description']}: {test['data']['num1']} {test['data']['operation']} {test['data']['num2']} = {result['result']}"
                    )
                else:
                    print(f"  ❌ {test['description']}: Expected {test['expected']}, got {result.get('result', 'error')}")
            else:
                print(f"  ❌ {test['description']}: HTTP {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"  ❌ {test['description']}: Request failed - {e}")

    # Test error handling
    print("\n🚫 Testing error handling:")
    error_test = {"data": {"num1": "😊", "operation": "➗", "num2": "😀"}, "description": "Division by zero"}

    try:
        response = requests.post(f"{base_url}/calculate", json=error_test["data"], headers={"Content-Type": "application/json"}, timeout=5)

        if response.status_code == 200:
            result = response.json()
            if not result["success"] and "error" in result:
                print(f"  ✅ {error_test['description']}: Error correctly handled - {result['error']}")
            else:
                print(f"  ❌ {error_test['description']}: Should have returned an error")
        else:
            print(f"  ❌ {error_test['description']}: HTTP {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"  ❌ {error_test['description']}: Request failed - {e}")

    print("\n🎉 Web API testing completed!")
    return True


if __name__ == "__main__":
    # Check if requests is available
    try:
        import requests
    except ImportError:
        print("❌ 'requests' library not found. Install with: pip install requests")
        sys.exit(1)

    test_web_calculator()
