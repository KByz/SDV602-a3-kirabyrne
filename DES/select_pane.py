"""
DES selection pane on homescreen and new windows.
"""
import sys
sys.dont_write_bytecode = True

import matplotlib.pyplot as plt
import numpy as np

def trend_plot():
    """
    Plot trend line graph in DES.
    """

def bar_plot():
    """
    Plot bar graph in DES.
    """

def pie_plot():
    """
    Plot pie chart in DES.
    """

def show_plot(pFigureFunction, **kwargs):
    """
    Show selected DES plot in layout.
    """
    current_plot = plot_with_kwargs(pFigureFunction, **kwargs)
    plt.figure(current_plot.number)
    plt.show()

def plot_with_kwargs(pFigureFunction, **kwargs):
    """
    Plot with keyword arguments.
    """
    kwarg_fig = None
    if kwargs :
        kwarg_fig = pFigureFunction(**kwargs)
    else:
        kwarg_fig = pFigureFunction()
    return kwarg_fig

if __name__=="__main__":

    show_plot(trend_plot)
    show_plot(bar_plot)
    show_plot(pie_plot)
    pass