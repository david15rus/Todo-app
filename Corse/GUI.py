import functions
import PySimpleGUI as sg
import time

sg.theme("Topanga")

clock = sg.Text('', key='time')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')


window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=200)
    window['time'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
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
            try:
                edited_todo = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                idx_of_edit = todos.index(edited_todo)
                todos[idx_of_edit] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 14))

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case 'Complete':
            try:
                completed_todo = values['todos'][0]

                todos = functions.get_todos()
                todos.remove(completed_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 14))
        case sg.WINDOW_CLOSED:
            break

        case 'Exit':
            break

window.close()

