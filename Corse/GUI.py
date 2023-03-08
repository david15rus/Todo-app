import sys

import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
exit_button = sg.Button('Exit')


window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [exit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()
    print(event, values, sep='\n')
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Show':
            pass

        case 'Edit':
            edited_todo = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            idx_of_edit = todos.index(edited_todo)
            todos[idx_of_edit] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            pass

        case sg.WINDOW_CLOSED:
            break

        case 'Exit':
            break

window.close()

