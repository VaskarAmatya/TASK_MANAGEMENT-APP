import json

FILE_NAME = "tasks.json"


# Load tasks from JSON file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add a new task
def add_task(tasks):
    task = input("Enter task: ")

    tasks.append({
        "task": task,
        "done": False
    })

    save_tasks(tasks)
    print("Task added successfully!")


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{number}. [{status}] {task['task']}")


# Complete a task
def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    number = int(input("Enter task number to complete: "))

    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Task completed!")
    else:
        print("Invalid task number.")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    number = int(input("Enter task number to delete: "))

    if 1 <= number <= len(tasks):
        deleted_task = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted: {deleted_task['task']}")
    else:
        print("Invalid task number.")


# Main program
tasks = load_tasks()

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        complete_task(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
