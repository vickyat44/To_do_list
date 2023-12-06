import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("To-Do List App Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_completed(self):
        self.view_tasks()
        try:
            index = int(input("Enter the task number to mark as completed: ")) - 1
            self.tasks[index] = f"{self.tasks[index]} (Completed)"
            print("Task marked as completed.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

    def delete_task(self):
        self.view_tasks()
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            deleted_task = self.tasks.pop(index)
            print(f"Task '{deleted_task}' deleted.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid task number.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.mark_completed()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Exiting the To-Do List App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
