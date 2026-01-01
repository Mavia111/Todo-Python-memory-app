"""
Todo Store Service
Manages in-memory collection of Todo objects with CRUD operations.
"""

from typing import List, Optional

# Import the Todo model
import sys
import os

# Add the project root to the path to import modules
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(os.path.dirname(current_dir))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from src.todo_app.models.todo import Todo


class TodoStore:
    """Manages in-memory collection of Todo objects with CRUD operations."""

    def __init__(self):
        """Initialize the TodoStore with an empty list and ID counter."""
        self.todos: List[Todo] = []
        self._next_id = 1

    def create_todo(self, title: str) -> Todo:
        """
        Create a new todo with the given title.

        Args:
            title (str): The title for the new todo

        Returns:
            Todo: The created Todo object
        """
        if not title or not title.strip():
            raise ValueError("Todo title cannot be empty")

        # Create the new todo with the next available ID
        new_todo = Todo(todo_id=self._next_id, title=title.strip())
        self.todos.append(new_todo)

        # Increment the ID counter for the next todo
        self._next_id += 1

        return new_todo

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in the store.

        Returns:
            List[Todo]: List of all Todo objects
        """
        return self.todos.copy()

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a todo by its ID.

        Args:
            todo_id (int): The ID of the todo to retrieve

        Returns:
            Optional[Todo]: The Todo object if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, new_title: str) -> bool:
        """
        Update the title of an existing todo.

        Args:
            todo_id (int): The ID of the todo to update
            new_title (str): The new title for the todo

        Returns:
            bool: True if the todo was updated, False if not found
        """
        if not new_title or not new_title.strip():
            raise ValueError("Todo title cannot be empty")

        for todo in self.todos:
            if todo.id == todo_id:
                todo.title = new_title.strip()
                return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id (int): The ID of the todo to delete

        Returns:
            bool: True if the todo was deleted, False if not found
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo as complete.

        Args:
            todo_id (int): The ID of the todo to mark complete

        Returns:
            bool: True if the todo was marked complete, False if not found
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = True
                return True
        return False

    def mark_incomplete(self, todo_id: int) -> bool:
        """
        Mark a todo as incomplete.

        Args:
            todo_id (int): The ID of the todo to mark incomplete

        Returns:
            bool: True if the todo was marked incomplete, False if not found
        """
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = False
                return True
        return False