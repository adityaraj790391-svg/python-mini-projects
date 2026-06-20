def task():
    tasks = []
    print("Welcome to the To-Do App!")

    total_task = int(input("Enter the total number of tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)


    print(f"Tasks added successfully! You have added {total_task} tasks.")
    print(f"Today's tasks are:\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add \n2-Update \n3-Delete \n4-View \n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been added successfully!")

        elif operation == 2:
            updated_val = input("Enter the task you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{updated_val}' has been updated to '{up}' successfully!")

        elif operation == 3:
            deleted_val = input("Enter the task you want to delete: ")
            if deleted_val in tasks:
                ind = tasks.index(deleted_val)
                del tasks[ind]
                print(f"Task '{deleted_val}' has been deleted successfully!")

        elif operation == 4:
            print(f"Today's tasks are: {tasks}")

        elif operation == 5:
            print("Exiting the To-Do App. Have a great day!")
            break

        else:
            print("Invalid Input")

task()

