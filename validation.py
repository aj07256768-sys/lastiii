def validate_task_name(task_name):
    return isinstance(task_name, str) and len(task_name.strip()) > 0


def validate_task_index(index, tasks):
    return isinstance(index, int) and 0 <= index < len(tasks)