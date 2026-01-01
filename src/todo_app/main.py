#!/usr/bin/env python3
"""
Todo Console Application
A simple command-line todo application with in-memory storage.
"""

import sys
import os

# Add the project root to the path so we can import modules
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(os.path.dirname(current_dir))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

# Import the modules
from src.todo_app.controllers.app_controller import AppController


def main():
    """Main entry point for the application."""
    print("Welcome to the Todo Console Application!")
    print("This application stores todos in memory only.")

    controller = AppController()
    controller.run()


if __name__ == "__main__":
    main()