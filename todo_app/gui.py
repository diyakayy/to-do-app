import functions
import FreeSimpleGUI as sg

#.Text and .Window etc are types
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout= [[label], [input_box, add_button]]) #label in one row and input and add is in separate row
#each row in the GUI has to be a list; if theres inly an outer bracket then theyll all be in one row and they all have to be a specific widget type , they cant be str or int etd

window.read() #here it suspends execution and waits for user response
window.close()
