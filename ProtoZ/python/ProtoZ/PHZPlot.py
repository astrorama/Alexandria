import ProtoZ.ChDataModel as chdm

def plot_2d_table(axes, name, table):
    x = table[table.keys()[0]].data
    y = table[table.keys()[1]].data
    axes.plot(x, y, label=name)

def plot_all_filters(axes, path):
    filters = chdm.get_filters(path)
    for name, data in filters.items():
        plot_2d_table(axes, name, data)