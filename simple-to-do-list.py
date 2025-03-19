def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()

def todo_list():
    tasks = []

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added successfully!\n")
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            task_no = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_no < len(tasks):
                removed_task = tasks.pop(task_no)
                print(f"Removed task: {removed_task}\n")
            else:
                print("Invalid task number!\n")
        elif choice == "4":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 4.\n")

todo_list()
