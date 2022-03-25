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
    
# First the window layout in 2 columns

create_formula = [
    [
        sg.Text("Write Your Formula Down"),
    ],
    [
        sg.InputText(
            size=(40, 20), enable_events=True, key="-FUNCTION-"
        )
    ],
    [
        sg.Button("Run/Create Graph", key="-RUN-")
    ]
]

# For now will only show the name of the file that was chosen
graph_viewer = [
    [sg.Text("This is your graph")],
    [sg.Canvas(key="-GRAPH-")],
    [sg.Text(size=(40, 1), key="-ERROR-")],
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

fig_agg = None
# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    """Create function graph after click run button"""
    if event == "-RUN-":
        function = values["-FUNCTION-"]
        if fig_agg is not None:
            delete_fig_agg(fig_agg)
        try:
            fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
            t = np.arange(0, 3, .01)
            fig.add_subplot(111).plot(t, eval(function))
            fig_agg = draw_figure(window["-GRAPH-"].TKCanvas, fig)
            window["-ERROR-"].update(" ")
        except:
            window["-ERROR-"].update("Error input function")

window.close()