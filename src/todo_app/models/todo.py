"""
Todo Model
Represents a single todo item with id, title, and completion status.
"""

class Todo:
    """Represents a single todo item."""

    def __init__(self, todo_id: int, title: str, completed: bool = False):
        """
        Initialize a Todo object.

        Args:
            todo_id (int): Unique identifier for the todo item
            title (str): The task description/title
            completed (bool): Completion status, defaults to False
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            raise ValueError("ID must be a positive integer")

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")

        if not isinstance(completed, bool):
            raise ValueError("Completed must be a boolean value")

        self.id = todo_id
        self.title = title.strip()
        self.completed = completed

    def __str__(self):
        """String representation of the Todo."""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title}"

    def __repr__(self):
        """Developer-friendly representation of the Todo."""
        return f"Todo(id={self.id}, title='{self.title}', completed={self.completed})"

    def to_dict(self):
        """Convert Todo to dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }