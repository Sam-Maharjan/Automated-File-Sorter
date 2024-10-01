import PySimpleGUI as sg
from organizer import organizer
layout = [  [sg.Text('Hi, thank you for using my file sorter!')],
            [sg.Text("Enter the directory of the files you want sorted (Start with /)"), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Done')] ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Done': # if user closes window or clicks cancel
        break
    temp=r"tmp"+values[0]
    temp=temp[3:]
    try:
        organizer(temp)
    except:
        sg.Popup('Error', f'An error occurred: Inexistant Directory') 


window.close()