tasks = []


def show_progress():
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])

    if total == 0:
        percentage = 0
    else:
        percentage = int((completed / total) * 100)

    bar_length = 20
    filled = int(bar_length * percentage / 100)
    bar = "#" * filled + "-" * (bar_length - filled)

    print(f"\nProgress: [{bar}] {percentage}%")
    print(f"Completed: {completed}/{total} tasks")


def add_task():
    name = input("Enter a new task: ").strip()

    if name:
        tasks.append({"name": name, "completed": False})
        print("Task added successfully!")
    else:
        print("Task name cannot be empty.")


def view_tasks():
    if not tasks:
        print("\nYour task list is empty.")
        show_progress()
        return

    print("\n--- Your To-Do List ---")

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['name']} - {status}")

    show_progress()


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter the task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
            show_progress()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def remove_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter the task number to remove: "))

        if 1 <= number <= len(tasks):
            if tasks[number - 1]["completed"]:
                removed = tasks.pop(number - 1)
                print(f"Removed completed task: {removed['name']}")
                show_progress()
            else:
                print("Complete the task before removing it.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add a task")
    print("2. View tasks and progress")
    print("3. Mark a task as completed")
    print("4. Remove a completed task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Thank you for using the To-Do List Application!")
        break
    else:
        print("Invalid option. Please choose 1, 2, 3, 4, or 5.")