#this is the frontend which is the codebase that constructs the user interface

import functions
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:S")
print("It is", now)
while True:
    user_action = input("Type add, edit, complete, show or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] +"\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()
            print("existing todos:", todos)

            new_todo = input("Enter new todo:")
            todos[number] = new_todo + "\n"
            print("the new list", todos)

            functions.write_todos(todos)

        except ValueError:
            print("invalid input")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("no item with that number")
            continue

    elif "exit" in user_action:
        break
    else:
        print("your answer doesnt make sense")

print("Bye!")

# "_" means anything else
# doc strings - uses triple quotes to describe the function for other ppl


