import numbers
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import random

def findMax(table, column) :
    """Returns the row of the given table where the given column has the
       maximum value. If there are multiple rows with this value the
       first one is returned."""

    maxIndex = -1
    maxValue = float('-inf')
    for row in table:
        if row[column] > maxValue:
            maxIndex = row.index
            maxValue = row[column]
    return table[maxIndex]


def getDistinctValues(table, column) :
    """Returns a set containing the different values of the tables column
       (without repetition)."""

    options = sorted(set([row[column] for row in table]))
    return options


def subTable(table, fixedColumns) :
    """Returns the rows of the table which have the fixed values for the
       columns given in the fixedColumns dictionary."""

    newIndices = [row.index for row in table if 
        all(row[column] == value for column,value in fixedColumns.items())]
    newColumns = list(set(table.colnames) - set(fixedColumns.keys()))
    return table[newIndices][newColumns]

def plot2D(table, xColumn, yColumn, plotType='bars') :
    """Creates a bar plot of the given columns of the table."""
    
    if len(table.colnames) != 2:
        print "Only tables with two columns can be plotted with plot2D"
        return
    fig, axes = plt.subplots()
    axes.set_xlabel(xColumn)
    axes.set_ylabel(yColumn)
    if plotType == 'bars':
        axes.bar(range(len(table[xColumn])), table[yColumn].data, align='center', width=1)
    else:
        axes.plot(range(len(table[xColumn])), table[yColumn].data)
    axes.set_xticks(range(len(table[xColumn])))
    axes.set_xticklabels(table[xColumn].data, size='small', rotation='vertical')
    fig.show()
    

def colorMap(table, xColumn, yColumn, colorColumn) :
    """Creates a color plot of the values in the colorColumn, treating
       it as a 2D array with axes the xColumn and yColumn."""

    if len(table.colnames) != 3:
        print "Only tables with three columns can be plotted with colorMap"
        return
    xOptions = getDistinctValues(table, xColumn)
    yOptions = getDistinctValues(table, yColumn)
    values = np.array([[subTable(table, {xColumn:xValue,yColumn:yValue})[colorColumn][0] for xValue in xOptions] for yValue in yOptions])
    fig, axes = plt.subplots()
    axes.set_xlabel(xColumn)
    axes.set_ylabel(yColumn)
    axes.set_xlim(0, len(xOptions))
    axes.set_ylim(0,len(yOptions))
    axes.set_xticks(np.array(range(len(xOptions)))+0.5)
    axes.set_yticks(np.array(range(len(yOptions)))+0.5)
    axes.set_xticklabels(xOptions, size='small', rotation='vertical')
    axes.set_yticklabels(yOptions, size='small')
    p = axes.pcolor(values)
    fig.colorbar(p)
    fig.show()


def plot3D(table, xColumn, yColumn, zColumn) :
    """Creates a 3D plot of the values in the zColumn, treating it as
       a 2D array with axes the xColumn and yColumn."""

    if len(table.colnames) != 3:
        print "Only tables with three columns can be plotted with plot3D"
        return
    xOptions = getDistinctValues(table, xColumn)
    yOptions = getDistinctValues(table, yColumn)
    zValues = np.array([[subTable(table, {xColumn:xValue,yColumn:yValue})[zColumn][0] for xValue in xOptions] for yValue in yOptions])
    fig = plt.figure()
    axes = fig.add_subplot(111, projection='3d')
    axes.set_xlabel(xColumn)
    axes.set_ylabel(yColumn)
    axes.set_xlim(0, len(xOptions))
    axes.set_ylim(0,len(yOptions))
    axes.set_xticks(np.array(range(len(xOptions))))
    axes.set_yticks(np.array(range(len(yOptions))))
    axes.set_xticklabels(xOptions, size='small', rotation='vertical')
    axes.set_yticklabels(yOptions, size='small', rotation='vertical')
    xValues = [range(len(xOptions)) for i in yOptions]
    yValues = [len(xOptions)*[i] for i in range(len(yOptions))]
    axes.plot_wireframe(xValues, yValues, zValues)
    fig.show()


