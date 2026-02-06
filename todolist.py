import time
import os
def main_menu():
    intro="""Welcome to to do list manangement
    1 - Add a task
    2 - Delete a task
    3 - Update a task
    4 - View all tasks
    5 - Exit
    """
    print(intro)

def task():
    task=[]
    print("Welcome to to do list manangement")
    tasks_num=int(input("Enter the number of tasks : "))
    time.sleep(2)
    os.system("cls")
    for i in range(1,tasks_num+1):
        task_name=input(f"Enter the task {i} : ")
        task.append(task_name)
    time.sleep(2)
    os.system("cls")
    print("Your all tasks are added")
    time.sleep(2)
    os.system("cls")
    while True:
        # os.system("cls")
        main_menu()
        choice =int(input("Enter the choice : "))
        time.sleep(2)
        os.system("cls")
        if choice == 1:
            new_task_user=input("Enter the task you want to add : ")
            if new_task_user not in task:
                task.append(new_task_user)
                print("Task added successfully")
                time.sleep(2)
                os.system("cls")
            else:
                print("This task is already exit")
                time.sleep(2)
                os.system("cls")
        elif choice==2:
            del_task=input("Enter the name of task : ")
            if del_task in task:
                ind=task.index(del_task)
                del task[ind]
                print("Task delete sucessfully")
                time.sleep(2)
                os.system("cls")
            else:
                print("Task unavalaible")
                print("Try Again")
                time.sleep(2)
                os.system("cls")
        elif choice==3:
            up_task=input("Enter the name of task : ")
            if up_task in task:
                new_task=input("Enter the new task name : ")
                ind=task.index(up_task)
                task[ind]=new_task
                print("Task update successfully")
                time.sleep(2)
                os.system("cls")
            else:
                print("Task unavalaible")
                print("Try Again")
                time.sleep(2)
                os.system("cls")
        elif choice==4:
            os.system("cls")
            print("Your all tasks are given :")
            for index,i in enumerate(task,start=1):
                print(index," - " , i)
            print("\n")
            key=input("Press a key to back : ")
            if key.lower()=="a":
                os.system("cls")
                exit
        elif choice==5:
            print("Closing the system ")
            time.sleep(2)
            os.system("cls")
            break
task()

