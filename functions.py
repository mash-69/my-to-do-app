FILEPATH = "todos.txt"


def get_todos(filename=FILEPATH):
    with open(filename, 'r') as file:
        todos_local = file.readlines()
        return todos_local
    """ read a text file and return the list
    of todo item.
    """


def write_todos(todos_arg, filename="todos.txt"):
    with open(filename, 'w') as file:
        file.writelines(todos_arg)
        """ write the todo items in the file"""
