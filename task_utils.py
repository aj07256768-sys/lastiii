from validation import validate_task_name, validate_task_index

tasks = []

def add_task(task_name):
    if validate_task_name(task_name):
        tasks.append({"name": task_name, "completed": False})
        print("Task added successfully")
    else:
        print("Invalid task name")


def view_pending_tasks():
    found = False

    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i}. {task['name']}")
            found = True

    if not found:
        print("No pending tasks")


def mark_task_complete(index):
    if validate_task_index(index, tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete")
    else:
        print("Invalid task index")
