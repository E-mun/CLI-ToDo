import json
from os import system
# Note: The current Task implementation handles the ID of the task *implicitly* in the ordering of the tasks list
class Task():
    '''
    This is the primary class that tracks the In-App functionality of the tasks on the list. 
    Note that all commands issued to the app will also have a component that updates the 'data' dictionary
    '''
    # Instantiates the Task with the given Task name and sets the complete flag to "False"
    def __init__(self, name, complete=False):
        self.name = name
        self.complete = complete

    def __repr__(self):
        if not self.complete:
            return f"{self.name}"
        else:
            return f"{self.name} - completed"
    
    def mark_complete(self):
        self.complete = True
        
    def mark_incomplete(self):
        self.complete = False

# Opening the data json file and writing the contents as a dict 'data'
'''
Note that the 'data' dictionary will be written to and will overwrite the 'data.json' file with each command input (except the clear and exit commands)
'''
try:
    with open('data.json', 'r') as f:
        # Try to load JSON data
        data = json.load(f)
except json.JSONDecodeError:  # Catch JSON decoding errors (e.g., empty file)
    data = {}  # Set data to an empty dict if the file is empty or contains invalid JSON
except FileNotFoundError:  # Handle case where file doesn't exist
    data = {}  # Set data to an empty dict if file is not found

# Uploads the tasks from data as a list of Task objects with keys as the task name and values as the completion status
tasks = []
for k,v in data.items():
    tasks.append(Task(k, v))

# Main Use Loop
app_running = True
while app_running:

    # Display Step
    print("--List of Tasks--")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}") # should print 1. Task Alpha
                                  #              2. Task Beta ...
    print("")

    # Command Step
    print("Commands: add <task>, done <task>, undo <task>, delete <task>, clear, exit")
    action = input()
    print("")

    # ADD command
    if action[:4].lower() == "add ":
        # Slices the name of the task from end of input
        task_name = action[4:]

        # Appends the task to the tasks list and updates the data file
        if task_name not in tasks:

            tasks.append(Task(task_name))
            data[task_name] = False
            with open('data.json', 'w') as f:
                json.dump(data, f)
            
            print(f"Task {task_name} added to list!")

        else:
            print("Task already in task list. Use undo command to reset the existing task.")
    
    # DONE command
    elif action[:5].lower() == "done ":
        # Slices the name of the task to mark as done
        task_raw = action[5:]
        task = action[5:].lower()

        # Check if task exists
        lowercase_tasks_list = []

        for existing_task in tasks:

            # Handle stripping the existing task "completed" string from the end if complete is True
            if not existing_task.complete:
                lowercase_tasks_list.append(str(existing_task).lower())
            else:
                lowercase_tasks_list.append(str(existing_task).lower()[:-12])

        if task in lowercase_tasks_list:
            
            # Update the task within the tasks list
            ind = lowercase_tasks_list.index(task)
            tasks[ind].complete = True

            # Update data file
            data[task_raw] = True
            with open('data.json', 'w') as f:
                json.dump(data, f)

            # Print to terminal
            print(f"Task {task_raw} is complete.")
        
        else:
            print("Task not recognized in task list. Check your task naming and try again.")
    
    # UNDO command
    elif action[:5].lower() == "undo ":

        # Slices the name of the task to undo complete flag
        task_raw = action[5:]
        task = action[5:].lower()

        # Check if task exists
        lowercase_tasks_list = []

        for existing_task in tasks:
            if not existing_task.complete:
                lowercase_tasks_list.append(str(existing_task).lower())
            else:
                lowercase_tasks_list.append(str(existing_task).lower()[:-12])

        if task in lowercase_tasks_list:
            
            # Update the task within the tasks list
            ind = lowercase_tasks_list.index(task)
            tasks[ind].complete = False

            # Update data file
            data[task_raw] = False
            with open('data.json', 'w') as f:
                json.dump(data, f)

            # Print to terminal
            print(f"Task {task_raw} is marked as incomplete.")
        
        else:
            print("Task not recognized in task list. Check your task naming and try again.")
    
    # DELETE command
    elif action[:7].lower() == "delete ":

        # Slices input for task name
        task_raw = action[7:]
        task = action[7:].lower()

        # Check if task exists
        lowercase_tasks_list = []

        for existing_task in tasks:
            if not existing_task.complete:
                lowercase_tasks_list.append(str(existing_task).lower())
            else:
                lowercase_tasks_list.append(str(existing_task).lower()[:-12])

        if task in lowercase_tasks_list:

            # Delete task from task list
            ind = lowercase_tasks_list.index(task)
            tasks.pop(ind)

            # Delete task from data file
            data.pop(task_raw)
            with open('data.json', 'w') as f:
                json.dump(data, f)
            
            # Update data file
            print(f"Task {task_raw} has been deleted.")

        else:
            print("Task not recognized in task list. Check your task naming and try again")
    
    # CLEAR command
    elif action[:5].lower() == "clear":
        system('clear')

    # EXIT command
    elif action[:4].lower() == "exit":
        app_running = False

    # Catch unrecognized input
    else:
        print("Command not recognized. Please try revising your input.")
    print("")
