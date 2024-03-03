import streamlit as st
import modules.functions
import os

if not os.path.exists('todos.txt'):
    with open("todos.txt", 'w') as file:
        pass 

todos = modules.functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    modules.functions.write_todos(todos)

st.title('My Todo App')
st.write('This is the app to create your to-do list.')


st.checkbox('Buy grocery')
st.checkbox('Buy the gel')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        modules.functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder='Enter a new todo...',
              on_change=add_todo, key="new_todo")

st.session_state
