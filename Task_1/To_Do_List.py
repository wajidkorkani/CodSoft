class Task:
    def __init__(self, name, due_date=None):
        self.name = name
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Pending"
            due_date = f"Due on {task.due_date}" if task.due_date else "No due date"
            print(f"{index}. {task.name} - {status} - {due_date}")

    def mark_task_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print(f"Task '{self.tasks[task_index - 1].name}' marked as done.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task.name}' removed.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (optional, press Enter to skip): ")
            new_task = Task(task_name, due_date if due_date else None)
            todo_list.add_task(new_task)
            print(f"Task '{task_name}' added to the to-do list.")
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as done: "))
            todo_list.mark_task_done(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "5":
            print("Quitting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
