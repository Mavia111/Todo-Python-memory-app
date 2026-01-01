"""
CLI Interface
Handles user input and output for the todo application.
"""

from typing import Optional
# Note: Todo import is not directly used in this file, so we don't need to import it


class CLIInterface:
    """Handles user input and output for the todo application."""

    def display_menu(self):
        """Display the main menu options to the user."""
        print("\n" + "="*40)
        print("TODO APPLICATION")
        print("="*40)
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Mark Todo as Complete")
        print("6. Mark Todo as Incomplete")
        print("7. Exit")
        print("="*40)

    def get_user_choice(self) -> int:
        """
        Get the user's menu choice.

        Returns:
            int: The user's menu choice (1-7)
        """
        while True:
            try:
                choice = int(input("Enter your choice (1-7): "))
                if 1 <= choice <= 7:
                    return choice
                else:
                    print("Please enter a number between 1 and 7.")
            except ValueError:
                print("Please enter a valid number.")

    def get_todo_title(self) -> str:
        """
        Get a todo title from the user.

        Returns:
            str: The todo title entered by the user
        """
        while True:
            title = input("Enter todo title: ").strip()
            if title:
                return title
            else:
                print("Title cannot be empty. Please enter a valid title.")

    def get_todo_id(self, prompt: str = "Enter todo ID: ") -> int:
        """
        Get a todo ID from the user.

        Args:
            prompt (str): The prompt to display to the user

        Returns:
            int: The todo ID entered by the user
        """
        while True:
            try:
                todo_id = int(input(prompt))
                if todo_id > 0:
                    return todo_id
                else:
                    print("Please enter a positive number for the ID.")
            except ValueError:
                print("Please enter a valid number for the ID.")

    def display_todos(self, todos: list):
        """
        Display all todos to the user.

        Args:
            todos (list): List of Todo objects to display
        """
        if not todos:
            print("\nNo todos found.")
            return

        print("\nYour Todos:")
        for todo in todos:
            print(f"  {todo}")

    def display_message(self, message: str):
        """
        Display a message to the user.

        Args:
            message (str): The message to display
        """
        print(f"\n{message}")

    def display_error(self, error: str):
        """
        Display an error message to the user.

        Args:
            error (str): The error message to display
        """
        print(f"\nError: {error}")

    def confirm_action(self, action: str) -> bool:
        """
        Ask the user to confirm an action.

        Args:
            action (str): The action to confirm

        Returns:
            bool: True if the user confirms, False otherwise
        """
        while True:
            response = input(f"\n{action} (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")