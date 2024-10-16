tasks = []  

while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Task")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter Task: ")
        tasks.append(task)  
    elif choice == 2:
        task = input("Enter task to remove: ")
        if task in tasks:  
            tasks.remove(task)  
        else:
            print("Task not found")
    elif choice == 3:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")  
    elif choice == 4:
        break  
    else:
        print("Invalid choice. Try again.")
