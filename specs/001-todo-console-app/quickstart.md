# Quickstart Guide: Todo In-Memory Python Console Application

## Prerequisites

- Python 3.13+ installed
- UV package manager (for dependency management, though no external dependencies required)

## Setup

1. Clone or navigate to the project directory
2. Ensure Python 3.13+ is available in your environment
3. No additional setup required - the application uses only Python standard library

## Running the Application

```bash
cd src
python todo_app/main.py
```

## Basic Usage

1. The application will display a menu with the following options:
   - 1. Add Todo
   - 2. View Todos
   - 3. Update Todo
   - 4. Delete Todo
   - 5. Mark Todo as Complete
   - 6. Mark Todo as Incomplete
   - 7. Exit

2. Follow the on-screen prompts to interact with the application

## Example Workflow

1. Select "1. Add Todo" and enter a task title
2. Select "2. View Todos" to see your tasks
3. Select "5. Mark Todo as Complete" and enter the todo ID to mark it complete
4. Select "7. Exit" to quit the application

## Development

The application is organized into four main components:
- Models: Todo data structure
- Services: In-memory storage and CRUD operations
- CLI: User interface and input handling
- Controllers: Application logic coordination

To modify functionality, edit the appropriate module in the `src/todo_app/` directory.