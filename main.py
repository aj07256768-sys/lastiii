from task_utils import add_task, view_pending_tasks, mark_task_complete


def menu():
    print("\n=== TASK MANAGER ===")
    print("1. Add Task")
    print("2. View Pending Tasks")
    print("3. Mark Task Complete")
    print("4. Exit")


def main():
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            view_pending_tasks()

        elif choice == "3":
            try:
                index = int(input("Enter index: "))
                mark_task_complete(index)
            except ValueError:
                print("Invalid number")

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()