"""
utilizamos bokeh para hacer gráficos

"""
from bokeh.plotting import figure, output_file, show

if __name__=="__main__":
    output_file('graficado_simple.html')
    fig = figure()
    print(type(fig))
    total_vals = int(input('cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor Y para {x}: '))
        y_vals.append(val)

fig.line(x_vals, y_vals,line_width = 2)
show(fig)