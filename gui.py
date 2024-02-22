import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple4")

clock=sg.Text('',key='clock')
label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo",key="todo_add")
add_button=sg.Button("Add")

list_box=sg.Listbox(values=functions.get_todos(), key='todos_edit',enable_events=True, size=[45,10])
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")

exit_button=sg.Button("Exit")

window=sg.Window("My To-Do App", layout=[[clock],[label],[input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],font=("Helvetica",20))

while True:
    event,values=window.read(timeout=1000)  #windows.read() gives tuple object with 2 values.
    window["clock"].update(value=time.strftime("%d-%b-%Y %H:%M:%S"))
    #print(event)       #On selecting the items from the "to do list", the 1. event=todos_edit, 2. Add(On clicking Add), 3. event=Edit(On clicking Edit)                
    #print(values)      #Values is a dict type whcih has keys as todo_add and todos_edit and values as the selection and add box data.
    match event:
        case "Add":
            todos=functions.get_todos()
            #print(todos)
            todos.append(values['todo_add'] +'\n')
            functions.write_todos(todos)
            window['todos_edit'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit=values['todos_edit'][0]
                new_to_do=values['todo_add'] +'\n'
                todos=functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_to_do
                #print(todos)
                functions.write_todos(todos)
                window['todos_edit'].update(values=todos)
            except IndexError:
                #print("Please select an item first")
                sg.popup("Please select an item first",font=("Helvetica",20))
        case 'todos_edit':
            window['todo_add'].update(value=values['todos_edit'][0])
        case "Complete":
            try:
                todo_to_remove=values['todos_edit'][0]
                todos=functions.get_todos()
                index=todos.index(todo_to_remove)
                todos.pop(index)
                print(todos)
                functions.write_todos(todos)
                window['todos_edit'].update(values=todos)
                window['todo_add'].update(value='')
            except IndexError:
                sg.popup("Please select an item first",font=("Helvetica",20))
        case 'Exit':
            #print("Bye!!")
            break
        case sg.WIN_CLOSED:
            #print("closing window")
            break  # exit() ==> the exit() will terminate the program at this place.
window.close()



