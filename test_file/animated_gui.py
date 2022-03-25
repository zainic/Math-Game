import PySimpleGUI as sg
import os.path
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import matplotlib.pyplot as plt
from zmath import *

matplotlib.use("TkAgg")

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def delete_fig_agg(fig_agg):
    fig_agg.get_tk_widget().forget()
    plt.close('all')
    
create_formula = [
    [
        sg.Text("Write Your Equation Down [ex: 2*x + sin(x)]"),
    ],
    [
        sg.Text("Function : "),
        sg.InputText(size=(40, 1), enable_events=True, key="-FUNCTION-"),
    ],
    [
        sg.Text("Lower Bound : "),
        sg.InputText(size=(10, 1), enable_events=True, key="-LOWER-"),
    ],
    [
        sg.Text("Upper Bound : "),
        sg.InputText(size=(10, 1), enable_events=True, key="-UPPER-"),
    ],
    [
        sg.Button("Run/Create Graph", key="-RUN-")
    ]
]

graph_viewer = [
    [sg.Text("This is your graph")],
    [sg.Canvas(key="-GRAPH-")],
    [sg.Text(size=(40, 1), key="-ERROR-")],
    [sg.Button('Exit', size=(10, 1), pad=((280, 0), 3), font='Helvetica 14')]
]

# ----- Full layout -----
layout = [
    [
        sg.Column(create_formula),
        sg.VSeperator(),
        sg.Column(graph_viewer),
    ]
]

window = sg.Window("Math Game", layout)
event, values = window.read(timeout=0)
canvas_elem = window['-GRAPH-']
canvas = canvas_elem.TKCanvas

fig = matplotlib.figure.Figure()
ax = fig.add_subplot(111)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)
ax.grid()
fig_agg = draw_figure(canvas, fig)

while True:
    event, values = window.read()
    if event == "-RUN-":
        function = values["-FUNCTION-"]
        lower = values["-LOWER-"]
        upper = values["-UPPER-"]
        """Check Emptyness"""
        if function == "":
            window["-ERROR-"].update("No function inserted")
            continue
        if lower == "":
            window["-ERROR-"].update("No lower bound inserted")
            continue
        if upper == "":
            window["-ERROR-"].update("No upper bound inserted")
            continue
        break

"""Run the Event Loop"""
lower = float(eval(lower))
upper = float(eval(upper))
x_list = np.arange(lower, upper, (upper-lower)/100)
fun_list = [eval(function) for x in x_list]
for i in range(len(fun_list) + 1):
    event, values = window.read(timeout=0)
    if event in ('Exit', None):
        exit(69)
    ax.cla()
    ax.set_xlim(lower, upper)
    ax.set_ylim(-10, 20)
    ax.grid()
    ax.plot(x_list[:i], fun_list[:i],  color='red')
    fig_agg.draw()

while True:
    event, values = window.read()
    if event in ('Exit', None, sg.WIN_CLOSED):
        exit(69)

window.close()