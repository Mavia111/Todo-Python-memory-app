# Tasks: Todo In-Memory Python Console Application

## Phase 1: Setup
Initialize project structure and foundational components per implementation plan.

### Tasks
- [ ] T001 Create project directory structure in src/todo_app/
- [ ] T002 Create package __init__.py files in models, services, cli, controllers directories
- [ ] T003 Create main.py entry point file in src/todo_app/
- [ ] T004 [P] Create todo.py model file in src/todo_app/models/
- [ ] T005 [P] Create todo_store.py service file in src/todo_app/services/
- [ ] T006 [P] Create interface.py CLI file in src/todo_app/cli/
- [ ] T007 [P] Create app_controller.py controller file in src/todo_app/controllers/

## Phase 2: Foundational Components
Build core components that all user stories depend on.

### Tasks
- [ ] T008 Implement Todo class with id, title, completed attributes in src/todo_app/models/todo.py
- [ ] T009 Add validation for Todo attributes (non-empty title, positive ID, boolean completed)
- [ ] T010 Implement TodoStore class with in-memory list in src/todo_app/services/todo_store.py
- [ ] T011 Add create method to TodoStore to add new todos with auto-incrementing IDs
- [ ] T012 Add read methods to TodoStore to get all todos and get todo by ID
- [ ] T013 Add update method to TodoStore to modify todo title
- [ ] T014 Add delete method to TodoStore to remove todo by ID
- [ ] T015 Add mark complete/incomplete methods to TodoStore
- [ ] T016 Create basic menu display functionality in src/todo_app/cli/interface.py
- [ ] T017 Create input handling functions in src/todo_app/cli/interface.py
- [ ] T018 Create Application Controller class in src/todo_app/controllers/app_controller.py
- [ ] T019 Connect controller to service layer in Application Controller
- [ ] T020 Set up basic application loop in main.py

## Phase 3: User Story 1 - Add and View Todos (Priority: P1)
As a user, I want to add new tasks to my todo list and view all my tasks with their completion status so that I can keep track of what I need to do.

### Goal
Implement the foundational functionality to add and view todos. This delivers the core value of a todo application.

### Independent Test Criteria
Can be fully tested by adding multiple tasks and viewing the complete list. Delivers the core value of a todo application.

### Tasks
- [ ] T021 [US1] Implement add todo functionality in TodoStore service
- [ ] T022 [US1] Create add todo CLI interface functions in src/todo_app/cli/interface.py
- [ ] T023 [US1] Connect add todo functionality in Application Controller
- [ ] T024 [US1] Implement view all todos functionality in TodoStore service
- [ ] T025 [US1] Create view todos CLI interface functions in src/todo_app/cli/interface.py
- [ ] T026 [US1] Connect view todos functionality in Application Controller
- [ ] T027 [US1] Integrate add and view functionality into main application loop
- [ ] T028 [US1] Test add and view functionality together
- [ ] T029 [US1] Add input validation for todo titles (non-empty)
- [ ] T030 [US1] Add error handling for empty titles in add functionality

## Phase 4: User Story 2 - Update and Delete Todos (Priority: P2)
As a user, I want to update the title of existing tasks and remove tasks I no longer need so that I can maintain an accurate todo list.

### Goal
Implement update and delete functionality to allow users to maintain their todo lists effectively after initial creation.

### Independent Test Criteria
Can be fully tested by updating an existing task's title and deleting tasks. Delivers value by allowing users to maintain their lists.

### Tasks
- [ ] T031 [US2] Implement update todo functionality in TodoStore service
- [ ] T032 [US2] Create update todo CLI interface functions in src/todo_app/cli/interface.py
- [ ] T033 [US2] Connect update todo functionality in Application Controller
- [ ] T034 [US2] Implement delete todo functionality in TodoStore service
- [ ] T035 [US2] Create delete todo CLI interface functions in src/todo_app/cli/interface.py
- [ ] T036 [US2] Connect delete todo functionality in Application Controller
- [ ] T037 [US2] Integrate update and delete functionality into main application loop
- [ ] T038 [US2] Test update and delete functionality together
- [ ] T039 [US2] Add error handling for non-existent todo IDs in update/delete
- [ ] T040 [US2] Add input validation for updated todo titles (non-empty)

## Phase 5: User Story 3 - Mark Todos as Complete (Priority: P3)
As a user, I want to mark tasks as complete so that I can track my progress and identify completed work.

### Goal
Implement functionality for tracking task completion status, which is essential for productivity.

### Independent Test Criteria
Can be fully tested by marking tasks as complete and viewing the updated status. Delivers value by allowing users to track progress.

### Tasks
- [ ] T041 [US3] Implement mark complete/incomplete functionality in TodoStore service
- [ ] T042 [US3] Create mark complete CLI interface functions in src/todo_app/cli/interface.py
- [ ] T043 [US3] Create mark incomplete CLI interface functions in src/todo_app/cli/interface.py
- [ ] T044 [US3] Connect mark complete/incomplete functionality in Application Controller
- [ ] T045 [US3] Integrate mark complete/incomplete functionality into main application loop
- [ ] T046 [US3] Test mark complete/incomplete functionality together
- [ ] T047 [US3] Add error handling for non-existent todo IDs in mark operations

## Phase 6: Error Handling and Edge Cases
Implement comprehensive error handling and address edge cases from specification.

### Tasks
- [ ] T048 Handle case when user tries to update or delete a non-existent task ID
- [ ] T049 Handle case when user enters empty or invalid input for task titles
- [ ] T050 Handle case when the todo list is empty and user tries to view tasks
- [ ] T051 Handle case when user enters invalid commands or options
- [ ] T052 Add graceful error handling to prevent application crashes
- [ ] T053 Ensure all user-facing messages are clear and helpful
- [ ] T054 Add input sanitization where needed
- [ ] T055 Test all error handling scenarios

## Phase 7: Polish & Cross-Cutting Concerns
Final touches, documentation, and quality improvements.

### Tasks
- [ ] T056 Create comprehensive menu system with all available options
- [ ] T057 Improve user prompts and messages for better UX
- [ ] T058 Add application exit functionality
- [ ] T059 Test complete application flow from start to finish
- [ ] T060 Verify all 5 required features work correctly (Add, View, Update, Delete, Mark Complete)
- [ ] T061 Ensure application runs fully in terminal without crashes
- [ ] T062 Verify todos persist during runtime (in-memory only)
- [ ] T063 Confirm code follows clean code principles (readable, modular, well-named)
- [ ] T064 Document any remaining functionality in comments
- [ ] T065 Run final integration test of all features together

## Dependencies

User stories can be implemented in priority order:
1. User Story 1 (P1) - Add and View Todos (foundational)
2. User Story 2 (P2) - Update and Delete Todos (depends on US1)
3. User Story 3 (P3) - Mark Todos as Complete (depends on US1)

## Parallel Execution Examples

Phase 2 (Foundational Components) tasks can be parallelized:
- T008-T009 (Todo model) can run in parallel with T010-T015 (TodoStore service)
- T016-T017 (CLI interface) can run in parallel with T018-T019 (Application Controller)

Phase 3+ (User Stories) tasks can be parallelized within each story:
- Add functionality [US1] can run in parallel with View functionality [US1]
- Update functionality [US2] can run in parallel with Delete functionality [US2]

## Implementation Strategy

MVP Scope: Complete Phase 1, Phase 2, and Phase 3 to deliver core add/view functionality that provides value as a basic todo application.

Incremental Delivery:
1. MVP: Add and view todos (US1)
2. Enhanced: Add update and delete (US2)
3. Complete: Add mark complete/incomplete (US3)
4. Polished: Error handling and polish (Phases 6-7)