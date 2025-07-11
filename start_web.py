#!/usr/bin/env python3
"""
start_web.py
Easy startup script for the Smiley Calculator web application
"""

import webbrowser
import time
import threading
import os
from app import app


def open_browser():
    """Open the browser after a short delay."""
    time.sleep(1.5)
    webbrowser.open("http://127.0.0.1:5000")


def main():
    """Start the web application and open browser."""
    print("🚀 Starting Smiley Calculator Web App...")
    print("🌐 Opening browser automatically...")
    print("✨ Enjoy calculating with smilies!")
    print("🛑 Press Ctrl+C to stop the server")

    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()

    # Start Flask app
    try:
        app.run(debug=False, host="127.0.0.1", port=5000)
    except KeyboardInterrupt:
        print("\n👋 Goodbye! Thanks for using the Smiley Calculator!")


if __name__ == "__main__":
    main()
