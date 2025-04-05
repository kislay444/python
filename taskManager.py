import os

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")
    print("User registered successfully!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open("users.txt", "r") as file:
        users = file.readlines()
    for user in users:
        stored_username, stored_password = user.strip().split(",")
        if username == stored_username and password == stored_password:
            print("Login successful!")
            return username
    print("Invalid username or password.")
    return None

def get_task_file(username):
    return f"{username}_tasks.txt"

def add_task(username):
    task = input("Enter task: ")
    with open(get_task_file(username), "a") as file:
        file.write(task + ",not done\n")
    print("Task added.")

def view_tasks(username):
    print("=== Your Tasks ===")
    try:
        with open(get_task_file(username), "r") as file:
            tasks = file.readlines()
        for i, task in enumerate(tasks):
            task_text, status = task.strip().split(",")
            print(f"{i+1}. {task_text} - {status}")
    except FileNotFoundError:
        print("No tasks found.")

def complete_task(username):
    view_tasks(username)
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        with open(get_task_file(username), "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            task_text, _ = tasks[task_num - 1].strip().split(",")
            tasks[task_num - 1] = task_text + ",done\n"
            with open(get_task_file(username), "w") as file:
                file.writelines(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except:
        print("Something went wrong.")

def delete_task(username):
    view_tasks(username)
    try:
        task_num = int(input("Enter task number to delete: "))
        with open(get_task_file(username), "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            with open(get_task_file(username), "w") as file:
                file.writelines(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Something went wrong.")

def task_menu(username):
    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            complete_task(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            print("Logged out.")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        print("\n=== Welcome to Task Manager ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                task_menu(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
