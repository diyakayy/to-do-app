import functions
import FreeSimpleGUI as sg

#.Text and .Window etc are types
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout= [[label], [input_box, add_button]]) #label in one row and input and add is in separate row
window.read() #here it suspends execution and waits for user response
window.close()
