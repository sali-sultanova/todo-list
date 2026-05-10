tasks = []


def add_task():
    task = input("Введите задачу: ")
    tasks.append(task)
    print("Задача добавлена!")


while True:
    choice = int(input("1- Добавить, 2-Просмотреть, 3-Удалить, 4-Изменить"))
    if choice == 1:
        add_task()
    elif choice == 2:
        print(tasks)
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        print("error")