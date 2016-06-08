import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import mpld3
from mpld3 import plugins, utils


class LinkedView(plugins.PluginBase):
    """A simple plugin showing how multiple axes can be linked"""

    JAVASCRIPT = """
    mpld3.register_plugin("linkedview", LinkedViewPlugin);
    LinkedViewPlugin.prototype = Object.create(mpld3.Plugin.prototype);
    LinkedViewPlugin.prototype.constructor = LinkedViewPlugin;
    LinkedViewPlugin.prototype.requiredProps = ["idpts", "idline", "data"];
    LinkedViewPlugin.prototype.defaultProps = {}
    function LinkedViewPlugin(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };

    LinkedViewPlugin.prototype.draw = function(){
      var pts = mpld3.get_element(this.props.idpts);
      var line = mpld3.get_element(this.props.idline);
      var data = this.props.data;

      function mouseover(d, i){
        line.data = data[i];
        line.elements().transition()
            .attr("d", line.datafunc(line.data))
            .style("stroke", this.style.fill);
      }
      pts.elements().on("mouseover", mouseover);
    };
    """

    def __init__(self, points, line, linedata):
        if isinstance(points, matplotlib.lines.Line2D):
            suffix = "pts"
        else:
            suffix = None

        self.dict_ = {"type": "linkedview",
                      "idpts": utils.get_id(points, suffix),
                      "idline": utils.get_id(line),
                      "data": linedata}

fig, ax = plt.subplots(2)

# scatter periods and amplitudes
np.random.seed(0)
P = np.random.random(size=10)
A = np.random.random(size=10)
x = np.linspace(0, 10, 100)
data = np.array([[x, (Ai+0.5*Ai * np.sin(x / Pi))]
                 for (Ai, Pi) in zip(A, P)])
points = ax[0].scatter(P, A, c=(P + A), s=200, alpha=0.5)

#ax[1].set_xlabel('Period')
#ax[1].set_ylabel('Amplitude')
#ax[0].set_xscale('log')
ax[0].invert_xaxis()
ax[0].set_xlabel('Temperature', size=15)
#ax[0].set_yscale('log')
ax[0].set_ylabel('Luminocity', size=15)
ax[0].set_title('', size=0)
#ax[1].text(9000, 0.01, 'Instability Strip', style='italic', bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
# create the line object
lines = ax[1].plot(x, 0 * x, '-w', lw=3, alpha=0.5)
ax[1].set_ylim(0, 2)

ax[0].set_title("HR Diagram - Instability Strip (Hover over points to see magnitude variation)")
ax[1].set_ylabel('Absolute Magnitude', size=15)
ax[1].set_xlabel('Time (days)', size=15)
ax[1].invert_yaxis()
# transpose line data and add plugin
linedata = data.transpose(0, 2, 1).tolist()
plugins.connect(fig, LinkedView(points, lines[0], linedata))

mpld3.show()