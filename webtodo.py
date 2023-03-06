import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo)
    st.session_state['new_todo'] = ''
    functions.save_todos(todos)


def complete_todo():
    for xx in st.session_state:
        if xx.startswith('complete-'):
            idx = int(xx[9:])
            print(f'{xx}: {st.session_state[xx]}  {idx}  {todos[idx]}')
            if bool(st.session_state[xx]):
                print(f'removing {todos[idx]}')
                todos.remove(todos[idx])
                break
    functions.save_todos(todos)


# st.experimental_rerun()

todos = functions.read_todos()

st.title('RTW Todo app')
st.subheader('Ardit\'s Python megacourse')

for kk, xx in enumerate(todos):
    st.checkbox(f'{kk}.{xx}', on_change=complete_todo, key=f'complete-{kk}')

st.text_input(label='todo', placeholder='add new todo',
              on_change=add_todo, key='new_todo')

# st.session_state
