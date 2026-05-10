def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def edit_task(tasks):
    print(f"Ваши задачи: ")
    show_tasks(tasks)
    num = int(input("Введите номер задачи для изменения: "))
    if 1 <= num <= len(tasks):
        new_task = input("Введите измененный текст задачи: ")
        tasks[num-1] = new_task
        print("Задача обновлена")
    else:
        print("Неправильный номер задачи")


tasks = []
while True:
    choice = int(input("1- Добавить, 2-Просмотреть, 3-Удалить, 4-Изменить"))
    if choice == 1:
        pass
    elif choice == 2:
        show_tasks(tasks)
    elif choice == 3:
        pass
    elif choice == 4:
        edit_task(tasks)
    else:
        print("error")