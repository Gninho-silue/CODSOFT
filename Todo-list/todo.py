# todo.py
from task import Task

def add_task(todo_list):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = Task(title, description)
    todo_list.append(task)
    print("Task added successfully.")

def view_tasks(todo_list):
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the to-do list.")

def complete_task(todo_list):
    view_tasks(todo_list)
    choice = int(input("Enter the task number to mark as completed: "))
    if 1 <= choice <= len(todo_list):
        todo_list[choice - 1].completed = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(todo_list):
    view_tasks(todo_list)
    choice = int(input("Enter the task number to delete: "))
    if 1 <= choice <= len(todo_list):
        del todo_list[choice - 1]
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")
