"""
Application Controller
Connects CLI interface with the todo store and controls program flow.
"""

import sys
import os

# Add the project root to the path to import modules
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(os.path.dirname(current_dir))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from src.todo_app.services.todo_store import TodoStore
from src.todo_app.cli.interface import CLIInterface


class AppController:
    """Connects CLI interface with the todo store and controls program flow."""

    def __init__(self):
        """Initialize the controller with a todo store and CLI interface."""
        self.todo_store = TodoStore()
        self.cli = CLIInterface()

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo Console Application!")
        print("This application stores todos in memory only.")

        while True:
            self.cli.display_menu()
            choice = self.cli.get_user_choice()

            if choice == 1:
                self._handle_add_todo()
            elif choice == 2:
                self._handle_view_todos()
            elif choice == 3:
                self._handle_update_todo()
            elif choice == 4:
                self._handle_delete_todo()
            elif choice == 5:
                self._handle_mark_complete()
            elif choice == 6:
                self._handle_mark_incomplete()
            elif choice == 7:
                self._handle_exit()
                break

    def _handle_add_todo(self):
        """Handle adding a new todo."""
        try:
            title = self.cli.get_todo_title()
            new_todo = self.todo_store.create_todo(title)
            self.cli.display_message(f"Todo '{new_todo.title}' added successfully with ID {new_todo.id}!")
        except ValueError as e:
            self.cli.display_error(str(e))

    def _handle_view_todos(self):
        """Handle viewing all todos."""
        todos = self.todo_store.get_all_todos()
        self.cli.display_todos(todos)

    def _handle_update_todo(self):
        """Handle updating a todo's title."""
        todos = self.todo_store.get_all_todos()
        if not todos:
            self.cli.display_message("No todos to update.")
            return

        self.cli.display_todos(todos)

        try:
            todo_id = self.cli.get_todo_id("Enter the ID of the todo to update: ")
            todo = self.todo_store.get_todo_by_id(todo_id)
            if todo:
                new_title = self.cli.get_todo_title()
                if self.todo_store.update_todo(todo_id, new_title):
                    self.cli.display_message(f"Todo ID {todo_id} updated successfully!")
                else:
                    self.cli.display_error("Failed to update todo.")
            else:
                self.cli.display_error(f"No todo found with ID {todo_id}.")
        except ValueError as e:
            self.cli.display_error(str(e))

    def _handle_delete_todo(self):
        """Handle deleting a todo."""
        todos = self.todo_store.get_all_todos()
        if not todos:
            self.cli.display_message("No todos to delete.")
            return

        self.cli.display_todos(todos)

        try:
            todo_id = self.cli.get_todo_id("Enter the ID of the todo to delete: ")
            todo = self.todo_store.get_todo_by_id(todo_id)
            if todo:
                if self.cli.confirm_action(f"Are you sure you want to delete todo '{todo.title}'?"):
                    if self.todo_store.delete_todo(todo_id):
                        self.cli.display_message(f"Todo ID {todo_id} deleted successfully!")
                    else:
                        self.cli.display_error("Failed to delete todo.")
                else:
                    self.cli.display_message("Delete operation cancelled.")
            else:
                self.cli.display_error(f"No todo found with ID {todo_id}.")
        except ValueError as e:
            self.cli.display_error(str(e))

    def _handle_mark_complete(self):
        """Handle marking a todo as complete."""
        todos = self.todo_store.get_all_todos()
        if not todos:
            self.cli.display_message("No todos to mark complete.")
            return

        self.cli.display_todos(todos)

        try:
            todo_id = self.cli.get_todo_id("Enter the ID of the todo to mark complete: ")
            todo = self.todo_store.get_todo_by_id(todo_id)
            if todo:
                if self.todo_store.mark_complete(todo_id):
                    self.cli.display_message(f"Todo ID {todo_id} marked as complete!")
                else:
                    self.cli.display_error("Failed to mark todo as complete.")
            else:
                self.cli.display_error(f"No todo found with ID {todo_id}.")
        except ValueError as e:
            self.cli.display_error(str(e))

    def _handle_mark_incomplete(self):
        """Handle marking a todo as incomplete."""
        todos = self.todo_store.get_all_todos()
        if not todos:
            self.cli.display_message("No todos to mark incomplete.")
            return

        self.cli.display_todos(todos)

        try:
            todo_id = self.cli.get_todo_id("Enter the ID of the todo to mark incomplete: ")
            todo = self.todo_store.get_todo_by_id(todo_id)
            if todo:
                if self.todo_store.mark_incomplete(todo_id):
                    self.cli.display_message(f"Todo ID {todo_id} marked as incomplete!")
                else:
                    self.cli.display_error("Failed to mark todo as incomplete.")
            else:
                self.cli.display_error(f"No todo found with ID {todo_id}.")
        except ValueError as e:
            self.cli.display_error(str(e))

    def _handle_exit(self):
        """Handle exiting the application."""
        self.cli.display_message("Thank you for using the Todo Console Application. Goodbye!")