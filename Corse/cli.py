import sys
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    command = input("Enter command (help to show any command exist in this program) ").lower().strip()

    if command.startswith('add'):
        todo = command[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif command.startswith('show'):

        todos = get_todos()

        for num, item in enumerate(todos):
            print('--'*(len(item)))
            print(f"{num+1}|{item.capitalize().rstrip()}")

    elif command.startswith('edit'):
        try:
            idx = int(command[5:])

            todos = get_todos()

            edited_todo = input("Введите новое дело: ")
            todos[idx-1] = edited_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Введите номер дела.')
            continue

    elif command.startswith('complete'):
        try:
            todos = get_todos('files/todos.txt')

            idx = int(command[9:]) - 1
            removed_todo = todos.pop(idx).rstrip()

            write_todos(todos)

            print(f"Дело {removed_todo.capitalize()} удалено")
        except IndexError:
            print("Дела с таким номером нет в списке.")
            continue

    elif command.startswith('help'):
        print("""
1) add - добавить дело в список дел
2) show - отображает список дел
3) edit - позволяет редактировать список дел
4) compete - позволяет удалить завершенное дело из списка
4) exit - выход из программы
""")

    elif command.startswith('exit'):
        print("Bye!")
        sys.exit()

    else:
        print("Команда не найдена (введите команду <help>)")