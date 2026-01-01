# Data Model: Todo In-Memory Python Console Application

## Todo Entity

**Attributes:**
- `id`: Integer - Unique identifier for the todo item (auto-incremented)
- `title`: String - The task description/title (required, non-empty)
- `completed`: Boolean - Completion status (default: False)

**Validation Rules:**
- `id` must be a positive integer
- `title` must be a non-empty string (1-255 characters)
- `completed` must be a boolean value

**State Transitions:**
- `incomplete` → `completed` (when marked as complete)
- `completed` → `incomplete` (when marked as incomplete)

## Todo Collection

**Structure:**
- In-memory list of Todo objects
- Maintains order of creation (FIFO)

**Operations:**
- Create: Add new Todo to collection
- Read: Retrieve Todo by ID or all Todos
- Update: Modify existing Todo properties
- Delete: Remove Todo by ID

**Constraints:**
- All IDs must be unique within the collection
- Collection size limited by available memory (practical limit: 1000 items)