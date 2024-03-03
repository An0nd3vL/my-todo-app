import modules.functions
#import os
#os.environ['PySimpleGUI_license'] = 'eDyXJsM8aTWxNglYbunYNgl0V9HclEwCZQSpIo6sI6kARalpdrmiV5sIbD3zBJlXcniKI5s9IakoxlpBYh2PVUuIcP2QVYJsR4CyIS6LMzTEceweOdDyUL0BMsTLcq3AMHigwHiOTdGrljj1ZjWx5xzfZdU6RJlCcZGfxhvfehWP17lqbQnoRZWDZJXNJPzuanWX9tunI3jdocxyLlCHJqOZYgWu1BlKR6m8lSysc632QHiIOOiHJaLjZiXAZSp0bciMIZsIIekr5uhfbSWBV4M9YeXTNV0rI8jfoZiMUG2i1upOdOGhgsiTLMCxJLDgbZ2m18w1YIW45f5HIljCoeitIxiDwcidQc3sV7zQdoG89otqZMXgJBJSRICxIf6uIrj5Mf52MCTpkKiPLdCAJrEbYXXvRclWS7XGNTzpdOWuVPknIHjhoKiqM0DsIFvfMGjdENvFM5jiAJyjNGCYIksOIak9RHhLd5G8V1F2ehHqBkpncPm4VOzzIRjtolitM9D6IvvpMUjXE8vjMEjYA7yUNYSLIjscIdkIVGt1YyWTl3sLQSWmRfkbckmqVJzZckyeIS6qItmJxPp5evGMFr3MbV3dgg4KNPD1VFAGcum7lYjpbV3tJopGdBCv5ejEbu2a0jiNLLC4J2J7UWEQF3kiZEHVJglocy39M5iKO6i7IS0XN0iM48yTMZTqYXuJNzjsAXuONgjpgtiZfSQy=a=q2f142170079278da6bf365c4862484b3064d37844c982c2d2a31c5b5e8956b4012213425cd0e23298deadbff5b786ad61fbd056a1cbf963bc38f58723f6f5998be7772e90a4450542a451c6ab0dd35ba690dbb07d437e57b1c47c8d6c15efee507d499b0d9db2ae7097e19e52ac8eeb2241888d52e7dcbf8e3797e1684da9a8da8d85bd3959e38c80a5d362a31073c0c65e70f5bbe19c0793304ea233579c3f710aac33cc0a37e09ffc888d5ab694a931aa41128f1c24570b59f4255f4812bc0c59eccf7855506118b6a82b319e2ffc31ff1f32214c10ba4a29ce9dc73135f769d06527cd11bb7fd8a35f0064f4605f4f13ae1f631d915ce2c0dfc8e24445dd41f06e439248053e57bea21c467567f8f969c8fc82e7f51524df83dd38589bbbcb69bb59a9f7cb4653b67efcc2075db0621495dc9bf2b7a2033e358ec1712b6d9784fd386cac508f2eaf59222248a3c7dc117d7122347f583254dc3c439821098c2f31139240368bc4d55a5484d2a3b0c4a15ca6ce4396aa137185cc9b48f218b08a0824883601806a406ba80310d6fd7f5d924826c7802ffe0a55fe88aec67edc30bbc5bf3edc924dd18ba7bd4e935c843f81de9a633fef8917df2398d8b708c026e4d9e52beb6059e49b78ee03bd5c9890623a6fa59593de1bf41c28dbdb610ef89809528f8daaea23945f18fb2dc91519e6735d33eda253d2769809f54b873'
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open("todos.txt", 'w') as file:
        pass           

sg.theme('LightGreen6')

clock = sg.Text('', key='clock')
label = sg.Text('Type in a todo')
input_box = sg.InputText(key="todo")
add_button = sg.Button('Add', mouseover_colors='LightYellow', key='Add')
list_box = sg.Listbox(values=modules.functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
remove_button = sg.Button('Remove', mouseover_colors='LightYellow', key="Remove")
exit_button = sg.Button('Exit')

window = sg.Window('Todo assistant', 
                   layout =[[clock],
                            [label], 
                            [input_box, add_button], 
                            [list_box, edit_button, remove_button],
                            [exit_button]],font=('Helvetica', 15),
                            finalize=True)


while True:
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    event, values = window.read(timeout=500)
    print(1, event)
    print(2, values)
    print(3, ['todos'])
    match event:
        case 'Add':
            todos = modules.functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            modules.functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = modules.functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                modules.functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please, select an item first.', font=('Helvetica', 15))

        case 'Remove': 
            try:   
                todo_to_remove = values['todos'][0]
                todos = modules.functions.get_todos()
                todos.remove(todo_to_remove)
                modules.functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please, select an item first.', font=('Helvetica', 15))

        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=['todos'][0])
        case sg.WIN_CLOSED:
            break

    
window.close()

