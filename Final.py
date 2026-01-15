# Michael Mcadams
# Period 6
# Section 1: Data Storage Setup
# A list of dictionaries to store tasks.
# Data Storage Requirement met: Using a List to store collection of items
#Starts a list to store tasks
todo_list = []


#Adds a new task entry to the todo list
def add_task(task_name):
    """Adds a new task dictionary to the global todo_list."""
    new_task = {'name': task_name, 'status': 'Pending'}
    todo_list.append(new_task)
    print(f"\n✅ Added task: '{task_name}'\n")

#Handles logic for dispalying all current tasks 
def view_tasks_range():
    print("\n--- Your To-Do List  ---")
    if not todo_list:
        print("Your list is currently empty.")
    else:
        for index in range(len(todo_list)):
            # Access the task using the index
            task = todo_list[index] 
            status_display = "[X]" if task['status'] == 'Complete' else "[ ]"
            print(f"{index + 1}. {status_display} {task['name']}")
    print("-----------------------\n")

#Primary control center that manages user experience 
def main():
    """The main application loop handling user interaction."""
    # makes sure the program runs until the player types 3
    while True:
        print("Menu: 1. Add Task | 2. View Tasks | 3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            task_name = input("Enter the new task name: ").strip()
            if task_name:
                add_task(task_name)
            else:
                print("Task name cannot be empty.")
        elif choice == '2':
            view_tasks_range() 
        elif choice == '3':
            print("Goodbye!")
            break
        else:
        
            print("\nInvalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    # This starts the application when the script is run
    main()
