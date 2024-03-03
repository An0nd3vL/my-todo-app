from modules.functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It's", now)


while True:
    user_action = input('Type add, show, edit, remove or exit: ')
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')
        
        write_todos(todos, 'todos.txt')

    elif user_action.startswith("show"):
        
        todos = get_todos()

        #new_todos =[item.strip('\n') for ite in todos]

        for index, item in enumerate(todos): 
            item = item.strip('\n')      #Removing spaces
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:

            number = int(user_action[5:])
            number = number - 1         #Making enumeration from 1

            todos = get_todos()

            new_todo = input('Enter new to do: ')
            todos[number] = new_todo + '\n'

            write_todos(todos, 'todos.txt')

        except ValueError:
            print("Invalid command!")
            continue
            
    elif user_action.startswith("remove"):
        try:
            number = int(user_action[7:])

            todos = get_todos()

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos, 'todos.txt')

            message = f'Todo {todo_to_remove} has been removed from the list'
            print(message)

        except IndexError:
            print("Invalid element number!")
            continue

    elif user_action.startswith("exit"):
        print('Bye bye!')
        break

    else:
        print('Unknown command')