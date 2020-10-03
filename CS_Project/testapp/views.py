from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
# from django.http import HttpResponse

# Create your views here.

# def index(request):
#	return render(request, 'pages/base.html', {})
def index(request):
    
    x=[1,2,3,4,5]
    y=[6,7,8,9,10]

    plot = figure(title = "Line graph", x_axis_label='X-Axis', y_axis_label='Y-Axis', plot_width=400, plot_height=400)

    plot.line(x,y, line_width=2)
    script, div = components(plot)

    return render( request, 'pages/base.html', {'script' : script, 'div' : div} )
