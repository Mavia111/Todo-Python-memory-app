# Todo Console Application

A simple command-line todo application with in-memory storage, built with Python.

## Features

- **Add Todo**: Create new todo items with titles
- **View Todos**: Display all todos with their completion status
- **Update Todo**: Modify existing todo titles
- **Delete Todo**: Remove todos by ID
- **Mark Complete/Incomplete**: Track task completion status

## Requirements

- Python 3.12+ (Python 3.13+ recommended)

## How to Run

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application:

```bash
python src/todo_app/main.py
```

## Usage

The application provides a menu-driven interface:

```
========================================
TODO APPLICATION
========================================
1. Add Todo
2. View Todos
3. Update Todo
4. Delete Todo
5. Mark Todo as Complete
6. Mark Todo as Incomplete
7. Exit
========================================
```

- Follow the on-screen prompts to interact with the application
- All data is stored in memory only and will be lost when the application exits
- The application handles invalid input gracefully

## Architecture

The application follows a clean architecture with separation of concerns:

- **Models**: `src/todo_app/models/todo.py` - Defines the Todo entity
- **Services**: `src/todo_app/services/todo_store.py` - Business logic and data management
- **CLI Interface**: `src/todo_app/cli/interface.py` - User interaction handling
- **Controllers**: `src/todo_app/controllers/app_controller.py` - Application flow coordination
- **Main**: `src/todo_app/main.py` - Entry point

## Testing

To run the test suite:

```bash
python test_todo_app.py
```

To run the demo:

```bash
python demo_todo_app.py
```

## Project Structure

```
project/
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── todo.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── todo_store.py
│       ├── cli/
│       │   ├── __init__.py
│       │   └── interface.py
│       ├── controllers/
│       │   ├── __init__.py
│       │   └── app_controller.py
│       └── main.py
├── test_todo_app.py
├── demo_todo_app.py
└── README.md
```

## Design Principles

- **Clean Code**: Readable, modular, and well-named functions/classes
- **Separation of Concerns**: Clear boundaries between components
- **Error Handling**: Graceful handling of invalid user input
- **In-Memory Storage**: Todos persist only during runtime
- **User-Friendly**: Clear prompts and error messages"# Todo-Python-memory-app" 
