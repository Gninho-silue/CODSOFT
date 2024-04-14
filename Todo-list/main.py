# main.py
from todo import add_task, view_tasks, complete_task, delete_task

def main():
    todo_list = []
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            complete_task(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
