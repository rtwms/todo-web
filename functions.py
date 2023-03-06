import os
todo_file = 'todo.txt'


def read_todos():
    if os.path.isfile(todo_file):
        with open(todo_file, 'r') as ftd:
            items = ftd.readlines()
        todos = []
        todos = [item.strip('\n') for item in items]
        for td in todos:
            if len(td) < 2:
                todos.remove(td)
    else:
        todos = []
    return todos


def save_todos(todos):
    with open(todo_file, 'w') as ftd:
        for x in todos:
            ftd.writelines(f'{x}\n')


