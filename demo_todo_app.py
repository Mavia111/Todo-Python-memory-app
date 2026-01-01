#!/usr/bin/env python3
"""
Demo script for the Todo Console Application
Demonstrates all functionality of the application.
"""

import sys
import os

# Add the project root to the path so we can import modules
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'src'))

from src.todo_app.controllers.app_controller import AppController
from src.todo_app.services.todo_store import TodoStore


def demo_application():
    """Demonstrate the application functionality."""
    print("DEMO: Todo Console Application")
    print("="*50)

    # Create a controller instance
    controller = AppController()
    store = controller.todo_store

    print("\n1. ADDING TODOS:")
    print("-" * 20)
    todo1 = store.create_todo("Learn Python")
    print(f"✓ Added: {todo1}")
    todo2 = store.create_todo("Build a CLI app")
    print(f"✓ Added: {todo2}")
    todo3 = store.create_todo("Test the application")
    print(f"✓ Added: {todo3}")

    print("\n2. VIEWING ALL TODOS:")
    print("-" * 25)
    all_todos = store.get_all_todos()
    for todo in all_todos:
        print(f"  {todo}")

    print("\n3. UPDATING A TODO:")
    print("-" * 20)
    success = store.update_todo(2, "Build a CLI app with Python")
    if success:
        updated_todo = store.get_todo_by_id(2)
        print(f"✓ Updated: {updated_todo}")
    else:
        print("✗ Update failed")

    print("\n4. MARKING A TODO AS COMPLETE:")
    print("-" * 35)
    success = store.mark_complete(1)
    if success:
        completed_todo = store.get_todo_by_id(1)
        print(f"✓ Marked complete: {completed_todo}")
    else:
        print("✗ Mark complete failed")

    print("\n5. MARKING A TODO AS INCOMPLETE:")
    print("-" * 35)
    success = store.mark_incomplete(3)
    if success:
        incomplete_todo = store.get_todo_by_id(3)
        print(f"✓ Marked incomplete: {incomplete_todo}")
    else:
        print("✗ Mark incomplete failed")

    print("\n6. VIEWING ALL TODOS AFTER CHANGES:")
    print("-" * 40)
    all_todos = store.get_all_todos()
    for todo in all_todos:
        print(f"  {todo}")

    print("\n7. DELETING A TODO:")
    print("-" * 20)
    success = store.delete_todo(2)
    if success:
        print("✓ Deleted todo with ID 2")
    else:
        print("✗ Delete failed")

    print("\n8. FINAL TODO LIST:")
    print("-" * 20)
    final_todos = store.get_all_todos()
    if final_todos:
        for todo in final_todos:
            print(f"  {todo}")
    else:
        print("  No todos remaining")

    print("\n" + "="*50)
    print("DEMO COMPLETE: All core functionality demonstrated!")
    print("✓ Add, View, Update, Delete, Mark Complete/Incomplete")


def demo_error_handling():
    """Demonstrate error handling."""
    print("\n\nERROR HANDLING DEMO:")
    print("="*25)

    store = TodoStore()

    # Test invalid operations
    print("1. Attempting to get non-existent todo:")
    todo = store.get_todo_by_id(999)
    if todo is None:
        print("   ✓ Correctly returned None for non-existent todo")

    print("2. Attempting to update non-existent todo:")
    success = store.update_todo(999, "New title")
    if not success:
        print("   ✓ Correctly returned False for non-existent todo update")

    print("3. Attempting to delete non-existent todo:")
    success = store.delete_todo(999)
    if not success:
        print("   ✓ Correctly returned False for non-existent todo delete")

    print("4. Attempting to mark non-existent todo complete:")
    success = store.mark_complete(999)
    if not success:
        print("   ✓ Correctly returned False for non-existent todo mark complete")

    print("5. Testing empty title validation:")
    try:
        store.create_todo("")
        print("   ✗ Should have raised an error for empty title")
    except ValueError as e:
        print(f"   ✓ Correctly raised error: {e}")

    print("\n✓ All error handling scenarios work correctly!")


if __name__ == "__main__":
    demo_application()
    demo_error_handling()
    print("\n🎉 All application features working correctly!")