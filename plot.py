import argparse
import numpy as np
import matplotlib.pyplot as plt
#==============================================================================
# import matplotlib.ticker as ticker
# import matplotlib.cm as cmx
# import matplotlib.lines as mlines
# from scipy import interpolate
#==============================================================================
from matplotlib.ticker import FormatStrFormatter

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', action="store", dest="fileName", help="The CSV file containing the data you want to plot", required=True)
parser.add_argument('-a', '--amount', action="store", dest="amount", help="The amount of measurements for each iteration", type=int, required=True)
parser.add_argument('--fields', action="store", dest="fields", help="defines the names of the columns. Must be the same size of the columns number", default="x,y,z,t")
parser.add_argument('--ycolumn', action="store", dest="y", help="The CSV file column you want to plot on the Y axis", default="x")
parser.add_argument('--xcolumn', action="store", dest="x", help="The CSV file column you want to plot on the X axis", default="y")
parser.add_argument('--xlabel', action="store", dest="xlabel", help="The label for the X axis", default='')
parser.add_argument('--ylabel', action="store", dest="ylabel", help="The label for the Y axis", default='')
parser.add_argument('--log', action='store_true', help='Specifies if the axises should use a logarithmic scale')
parser.add_argument('-s', '--save', action='store_true', help='Specifies if the produced plot should be saved to file')
args = parser.parse_args()
x = args.x
y = args.y
amount = args.amount
rawData = np.genfromtxt(args.fileName, delimiter=' ', names=args.fields)
rawData.sort(order=x)
iterations = int(len(rawData) / amount)
data = np.zeros_like(rawData[:iterations])
for r in range(0, len(rawData), amount):
    sum = 0.0
    for e in range(r, r+amount, 1):
        sum += rawData[e][0]
    data[int(r / amount)] = (sum / amount, rawData[r][1], rawData[r][2], rawData[r][3])
data.sort(order=x)
fig, ax1 = plt.subplots()
plt.xlabel(args.xlabel)
plt.ylabel(args.ylabel)
#new_x = interpolate.interp1d(data[x], range(iterations))(data[x])
if (args.log):
    ax1.set_yscale('log')
    ax1.set_xscale('log')
plt.yticks(data[y])
plt.xticks(data[x], rotation=45)
ax1.grid(which = 'both')
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.3f'))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax1.plot(data[x], data[y], 'o-', label='the data')
plt.show()
if (args.save):
    fig.savefig(args.fileName + '-plot.pdf')