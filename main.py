todos=[]
while True:
    user_action=input("Type show, add, edit, complete or exit: ")
    user_action=user_action.strip()

    match user_action:
        case "show":
            print("List of todos are:")
            for index,item in enumerate(todos):
                print(f"{index}-{item}")
        case "add":
            todo=input("Enter a todo item: ")
            todos.append(todo)
        case "edit":
            for index,item in enumerate(todos):
                print(f"{index}-{item}")
            number=int(input("Number of the todo to edit: "))
            new_todo=input("Enter new todo item: ")
            todos[number]=new_todo
        case "complete":
            for index,item in enumerate(todos):
                print(f"{index}-{item}")
            number=int(input("Number of the todo to complete: "))
            todos.pop(number)
        case "exit":
            print("Bye!!")
            break
        case _:
            print("looks like you entered not from the given options.")
            continue

