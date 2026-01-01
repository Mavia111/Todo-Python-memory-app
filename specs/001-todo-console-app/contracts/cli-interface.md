# CLI Interface Contract: Todo Console Application

## Command Interface

The application provides a menu-driven interface with the following commands:

### Add Todo
- **Command**: Option 1 from main menu
- **Input**: Todo title as string
- **Output**: Confirmation message with assigned ID
- **Error Cases**: Empty title returns error message

### View Todos
- **Command**: Option 2 from main menu
- **Input**: None
- **Output**: List of all todos with ID, title, and completion status
- **Error Cases**: None (empty list displays as "No todos found")

### Update Todo
- **Command**: Option 3 from main menu
- **Input**: Todo ID and new title
- **Output**: Confirmation of update
- **Error Cases**: Invalid ID returns error, empty title returns error

### Delete Todo
- **Command**: Option 4 from main menu
- **Input**: Todo ID
- **Output**: Confirmation of deletion
- **Error Cases**: Invalid ID returns error

### Mark Todo Complete
- **Command**: Option 5 from main menu
- **Input**: Todo ID
- **Output**: Confirmation of status change
- **Error Cases**: Invalid ID returns error

### Mark Todo Incomplete
- **Command**: Option 6 from main menu
- **Input**: Todo ID
- **Output**: Confirmation of status change
- **Error Cases**: Invalid ID returns error

### Exit
- **Command**: Option 7 from main menu
- **Input**: None
- **Output**: Application terminates