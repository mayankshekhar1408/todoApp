import time
import functions

print(time.strftime("%d-%b-%Y %H:%M:%S"))
while True:
    user_action=input("Type show, add, edit, complete or exit: ")
    user_action=user_action.strip()

    if user_action.startswith("show"):
        todos=functions.get_todos()
        for index,item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("add"):
        if user_action.strip()=="add":
            todo=input("Enter the todo item for add: ")
        else:
            todo=user_action[4:]
        todos=functions.get_todos()
        todos.append(todo +'\n')
        functions.write_todos(todos)


    elif user_action.startswith("edit"):
        todos=functions.get_todos()
        for index,item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)
        user_input=int(input("Select the todo item number for editing: "))
        user_item=input("Please write the new todo item in the place: ")
        todos[user_input-1]=user_item
        functions.write_todos(todos)
        
    elif user_action.startswith("complete"):
        todos=functions.get_todos()
        for index,item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)
        user_input=int(input("Select the todo item number for completing: "))
        todos.pop(user_input-1)
        functions.write_todos(todos)

    elif user_action.startswith("exit"):
        print("Bye!!")
        break

    else:
        print("Looks like you have not given correct input.")
