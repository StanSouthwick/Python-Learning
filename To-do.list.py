tasks = []


# Load tasks from a file
def load_tasks():
    global tasks
    try:
        with open ("task.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = [] # Error redundancy if file is not found


# Save tasks to a file
def save_tasks():
    with open("task.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n") # Write task with a new line in file task.txt

           
# Displays tasks in the list
def show_task():
    print("\nTo do to list:")
    if not tasks:
        print("You're all up to date!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"\n{i}. {task}")

# Adds a task to the list
def add_task():
    task = input("\nAdd a task to your list: ")
    tasks.append(task)
    save_tasks()
    print("Your to-do list has been updated.")

# Removes a task from the list
def remove_task():
    show_task()
    task = int(input("Please select which task you would like to remove:"))
    removed = tasks.pop(task - 1)
    save_tasks()
    print(f"{removed} has been removed from your list.")

    # Main menu
def menu():
    while True:
        print("\nSelect one of the following options to manage your to-do list:")
        print("\n1. Show your to-do list")
        print("\n2. Add a task to your list")
        print("\n3. Remove a task from your list")
        print("\n4. Exit")
        load_tasks()

        choice = input("\nEnter your choice:")

        if choice == "1":
            show_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("\nThank you! Have a great day!\n")
            break
        else:
            print("Invalid choice. Please try again.")

menu()

