import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("To-Do Web App")
st.subheader("Thsis is my to-do web app")
st.write("This is an app to increase my productivity")


for index,todo in enumerate(todos):
    if todo != "\n":
        checkbox=st.checkbox(todo,key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.experimental_rerun()
        

st.text_input(label="",placeholder="Add new todo...", on_change=add_todo, key='new_todo')

st.session_state