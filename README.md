# Task Manager Application
## A simple command-line task manager written in Python. This app allows users to add, mark as complete, undo, delete, clear the terminal of clutter, and exit the program. Tasks are stored in a JSON file (data.json), which is automatically updated with each action.

## Features
Add tasks to the list
Mark tasks as completed or mark tasks as incomplete
Delete tasks from the list
Clear the console screen
Exit the application
The tasks are saved in a JSON file (data.json), and the application loads and saves the tasks on each action.

## Requirements
Python 3.x
No external libraries are required for this application.

## Installation
Clone this repository to your local machine:

bash
Copy
git clone https://github.com/yourusername/task-manager.git
cd task-manager
Ensure that Python 3.x is installed on your machine. You can check this by running:

bash
Copy
python3 --version
Run the script:

bash
Copy
python3 task_manager.py
Usage
Once the script is running, you'll interact with the application via the terminal. It will display a list of tasks and prompt you for input. Here are the commands you can use:

## Commands
add <task_name>: Adds a task to the list.

Example: add Task 1
done <task_name>: Marks the specified task as completed.

Example: done Task 1
undo <task_name>: Marks the specified task as incomplete.

Example: undo Task 1
delete <task_name>: Deletes the specified task from the list.

Example: delete Task 1
clear: Clears the terminal screen (works only in supported terminals).

exit: Exits the application.

### Example Interaction
bash
Copy
--List of Tasks--
1. Task 1
2. Task 2

Commands: add <task>, done <task>, undo <task>, delete <task>, clear, exit
add Task 3

Task Task 3 added to list!

--List of Tasks--
1. Task 1
2. Task 2
3. Task 3

Commands: add <task>, done <task>, undo <task>, delete <task>, clear, exit
done Task 3

Task Task 3 is complete.
Task List Display
The task list is displayed with the task name and whether it is marked as completed. Completed tasks are shown with the suffix - completed.

bash
Copy
1. Task 1
2. Task 2 - completed
Data Storage
Tasks are stored in a JSON file named data.json. Each task is represented by a dictionary key (task name) with its corresponding completion status (True for completed, False for incomplete).

Example data.json:

json
Copy
{
    "Task 1": false,
    "Task 2": true
}
When a task is added, completed, or deleted, the JSON file is updated accordingly.

## Error Handling
If the data.json file is not found or is empty, the application will create and start with an empty task list.
Invalid or unrecognized commands will prompt the user to revise their input.

# License
This project is licensed under the MIT License.
