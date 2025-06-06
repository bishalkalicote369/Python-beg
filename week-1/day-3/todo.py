# todo_app.py

todo_list = []


def show_menu():
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(todo_list, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['title']}")


def add_task():
    title = input("Enter task title: ")
    todo_list.append({"title": title, "done": False})
    print("Task added!")


def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            deleted = todo_list.pop(task_num - 1)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
