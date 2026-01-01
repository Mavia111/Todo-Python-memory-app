#!/usr/bin/env python3
"""
Script to run the main Todo Console Application
"""

import sys
import os

# Add the project root to the path so we can import modules
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Run the main application
if __name__ == "__main__":
    # Import and run main function from main.py
    import src.todo_app.main as main_module
    main_module.main()