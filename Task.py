def remove_task(tasks, task_name):
    if task_name in tasks:
        tasks.remove(task_name)
    return tasks

# Example usage:
tasks = ["Task 1", "Task 2", "Task 3"]
task_to_remove = "Task 2"
tasks = remove_task(tasks, task_to_remove)
print("Tasks after removal:", tasks)
