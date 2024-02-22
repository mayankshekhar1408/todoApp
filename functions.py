import os

FILEPATH="todos.txt"
def get_todos(filepath=FILEPATH):
    if not os.path.exists("todos.txt"):
        with open("todos.txt", "w") as file:
            pass
    with open(filepath,"r") as file_local:
        todos_local=file_local.readlines()      #gives List Object
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    if not os.path.exists("todos.txt"):
        with open("todos.txt", "w") as file:
            pass
    with open(filepath,'w') as file:
        file.writelines(todos_arg)


if __name__=="__main__":
    print("Hello")
