def task():
    tasks = []
    print("Welcome to the To-Do App!")

    total_task = int(input("Enter the total number of tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)


    print(f"Tasks added successfully! You have added {total_task} tasks.")
    print(f"Today's tasks are:\n{tasks}")

    while 
