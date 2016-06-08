#from django.shortcuts import render

# Create your views here.
import django
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins, utils
# import Figure and FigureCanvas, we will use API
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# used to generate the graph
import numpy as np
import matplotlib.pyplot as plt, mpld3
	
def hr(request):

	import matplotlib.pyplot as plt, mpld3

	fig = plt.figure(figsize=(8,6))
	plt.plot([1,2,3,4])
	g = mpld3.fig_to_html(fig)
	return django.http.HttpResponse(g)
	
