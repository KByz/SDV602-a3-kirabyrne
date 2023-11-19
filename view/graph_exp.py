"""
Display example graphs when opening the inital DES
ploulated with mock transport data. 
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.dont_write_bytecode = True


def bar_graph(**kwargs):
    """
    Plot an example bar graph in DES.

    """
    transport_modes = ['Car', 'Bike', 'Public Transport', 'Walk']
    y_pos = np.arange(len(transport_modes))

    plt.bar(y_pos, [10, 7, 5, 3], align='center', alpha=0.5)

    plt.xlabel("Transport Mode")
    plt.ylabel("Number of People")
    plt.title("Transport Mode Survey 2023")

    plt.plot()

    return plt.gcf()


def pie_graph(**kwargs):
    """
    Plot an eaxmple pie chart in initial DES
    poulated with transport data.
    """
    labels = ['Car', 'Bike', 'Public Transport', 'Walk']
    sizes = [10, 7, 5, 3]
    # sizes.append(100 - sum(sizes)) << ?? This makes sizes longer than the labels?
    explode = (0.1, 0, 0, 0)

    graph1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=0)
    # Levels the aspect ratio of the pie chart to make it a perfect circle.
    ax1.axis('equal')

    plt.title('Transport Pie Chart 2023')

    return plt.gcf()


def trend_chart(**kwargs):
    Bus = {
        "Bus_Passangers": [43191, 41042, 15293, 19183, 35193, 56180, 68113],
        "Year": [2018, 2019, 2020, 2021, 2022, 2023, 2024]
    }
    graph, ax = plt.subplots()
    ax.plot(Bus["Year"], Bus["Bus_Passangers"])
    ax.set_xlabel("Year")
    ax.set_ylabel("Bus Passangers")
    ax.set_title("Bus Passangers Per Year")
    return plt.gcf()


def show_plot(pFigureFunction, **kwargs):
    """
    Display chosen graph in canvas pane.

    args
        pFigureFunction (returns a MatPlotLib figure)\n
        **kwargs must match kwargs of the function
    """
    current_graph = graph_w_kwargs(pFigureFunction, **kwargs)
    plt.figure(current_graph.number)
    plt.show()


def graph_w_kwargs(pFigureFunction, **kwargs):
    """
    Plot with keyword arguments.
    """
    kwarg_fig = None
    if kwargs:
        kwarg_fig = pFigureFunction(**kwargs)
    else:
        kwarg_fig = pFigureFunction()
    return kwarg_fig


if __name__ == "__main__":
    show_plot(trend_chart)
    show_plot(bar_graph)
    show_plot(pie_graph)
    pass
