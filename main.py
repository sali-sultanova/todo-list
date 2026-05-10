tasks = []

def delete_task(tasks):
    print(tasks)
    tasks.pop(int(input("Номер задачи: ")) - 1)   

while True:
    choice = int(input("1- Добавить, 2-Просмотреть, 3-Удалить, 4-Изменить"))
    if choice == 1:
        pass
    elif choice == 2:
        print(tasks)
    elif choice == 3:
        delete_task(tasks)
    elif choice == 4:
        pass
    else:
        print("error")



