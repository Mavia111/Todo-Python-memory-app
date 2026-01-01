#!/usr/bin/env python3
"""
Test script for the Todo Console Application
"""

import sys
import os

# Add the project root to the path so we can import modules
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Import modules using direct file paths to avoid package issues
sys.path.insert(0, os.path.join(project_root, 'src'))

from src.todo_app.models.todo import Todo
from src.todo_app.services.todo_store import TodoStore
from src.todo_app.cli.interface import CLIInterface
from src.todo_app.controllers.app_controller import AppController


def test_todo_model():
    """Test the Todo model functionality."""
    print("Testing Todo model...")

    # Test creating a todo
    todo = Todo(1, "Test todo", False)
    assert todo.id == 1
    assert todo.title == "Test todo"
    assert todo.completed == False

    # Test string representation
    assert str(todo) == "[○] 1. Test todo"

    # Test marking as complete
    todo.completed = True
    assert str(todo) == "[✓] 1. Test todo"

    # Test dictionary conversion
    todo_dict = todo.to_dict()
    assert todo_dict["id"] == 1
    assert todo_dict["title"] == "Test todo"
    assert todo_dict["completed"] == True

    # Test validation
    try:
        Todo(0, "Invalid ID")
        assert False, "Should have raised ValueError for invalid ID"
    except ValueError:
        pass

    try:
        Todo(1, "")
        assert False, "Should have raised ValueError for empty title"
    except ValueError:
        pass

    print("✓ Todo model tests passed")


def test_todo_store():
    """Test the TodoStore functionality."""
    print("Testing TodoStore...")

    store = TodoStore()

    # Test creating todos
    todo1 = store.create_todo("First todo")
    assert todo1.id == 1
    assert todo1.title == "First todo"
    assert todo1.completed == False

    todo2 = store.create_todo("Second todo")
    assert todo2.id == 2
    assert todo2.title == "Second todo"

    # Test getting all todos
    all_todos = store.get_all_todos()
    assert len(all_todos) == 2
    assert all_todos[0].id == 1
    assert all_todos[1].id == 2

    # Test getting todo by ID
    found_todo = store.get_todo_by_id(1)
    assert found_todo is not None
    assert found_todo.title == "First todo"

    # Test updating todo
    result = store.update_todo(1, "Updated todo")
    assert result == True
    updated_todo = store.get_todo_by_id(1)
    assert updated_todo.title == "Updated todo"

    # Test marking as complete/incomplete
    result = store.mark_complete(1)
    assert result == True
    completed_todo = store.get_todo_by_id(1)
    assert completed_todo.completed == True

    result = store.mark_incomplete(1)
    assert result == True
    incomplete_todo = store.get_todo_by_id(1)
    assert incomplete_todo.completed == False

    # Test deleting todo
    result = store.delete_todo(1)
    assert result == True
    deleted_todo = store.get_todo_by_id(1)
    assert deleted_todo is None

    remaining_todos = store.get_all_todos()
    assert len(remaining_todos) == 1

    print("✓ TodoStore tests passed")


def test_cli_interface():
    """Test the CLI interface functionality."""
    print("Testing CLI interface...")

    cli = CLIInterface()

    # Just testing that methods exist and can be called without errors
    # (actual input/output would require mocking)
    assert hasattr(cli, 'display_menu')
    assert hasattr(cli, 'get_user_choice')
    assert hasattr(cli, 'get_todo_title')
    assert hasattr(cli, 'get_todo_id')
    assert hasattr(cli, 'display_todos')
    assert hasattr(cli, 'display_message')
    assert hasattr(cli, 'display_error')
    assert hasattr(cli, 'confirm_action')

    print("✓ CLI interface tests passed")


def test_app_controller():
    """Test the AppController functionality."""
    print("Testing AppController...")

    controller = AppController()

    # Test that controller has required attributes
    assert hasattr(controller, 'todo_store')
    assert hasattr(controller, 'cli')
    assert hasattr(controller, 'run')

    # Test basic functionality
    initial_count = len(controller.todo_store.get_all_todos())

    # Add a todo
    new_todo = controller.todo_store.create_todo("Test todo for controller")
    assert len(controller.todo_store.get_all_todos()) == initial_count + 1

    print("✓ AppController tests passed")


def main():
    """Run all tests."""
    print("Running tests for Todo Console Application...\n")

    test_todo_model()
    test_todo_store()
    test_cli_interface()
    test_app_controller()

    print("\n✓ All tests passed! The application is working correctly.")


if __name__ == "__main__":
    main()