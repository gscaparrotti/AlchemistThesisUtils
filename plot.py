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
parser.add_argument('-f', '--file', action="append", dest="fileName", help="The CSV file containing the data you want to plot", required=True)
parser.add_argument('-l', '--legend', action="append", dest="legend", help="A legend for the corresponding CSV file", required=False)
parser.add_argument('-a', '--amount', action="store", dest="amount", help="The amount of measurements for each iteration", type=int, required=True)
parser.add_argument('--fields', action="store", dest="fields", help="defines the amount and the names of the columns. Must be the same size of the columns number (eg. 'x,y,z,t')", default="x,y,z,t")
parser.add_argument('--ycolumn', action="store", dest="y", help="The CSV file column you want to plot on the Y axis (must be a field you specified with the --field option)", default="x")
parser.add_argument('--xcolumn', action="store", dest="x", help="The CSV file column you want to plot on the X axis (must be a field you specified with the --field option)", default="y")
parser.add_argument('--xlabel', action="store", dest="xlabel", help="The label for the X axis", default='')
parser.add_argument('--ylabel', action="store", dest="ylabel", help="The label for the Y axis", default='')
parser.add_argument('--log', action='store_true', help='Specifies if the axises should use a logarithmic scale')
parser.add_argument('-s', '--save', action='store_true', help='Specifies if the produced plot should be saved to file')
args = parser.parse_args()
x = args.x
y = args.y
amount = args.amount
fig, ax1 = plt.subplots()
plt.xlabel(args.xlabel)
plt.ylabel(args.ylabel)
#new_x = interpolate.interp1d(data[x], range(iterations))(data[x])
if (args.log):
    ax1.set_yscale('log')
    ax1.set_xscale('log')
yt = np.empty(0)
xt = np.empty(0)
ax1.grid(which = 'both')
ax1.xaxis.set_major_formatter(FormatStrFormatter('%.3f'))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
for f in range(0, len(args.fileName)):
    rawData = np.genfromtxt(args.fileName[f], delimiter=' ', names=args.fields)
    rawData.sort(order=x)
    iterations = int(len(rawData) / amount)
    fields_amount = len(rawData[0])
    data = np.zeros_like(rawData[:iterations])
    ystddev = np.zeros(iterations)
    for r in range(0, len(rawData), amount):
        sum = 0.0
        ystddev[int(r / amount)] = np.std(rawData[r:r + amount][y])
        for e in range(r, r+amount, 1):
            sum += rawData[e][y]
        temp = np.zeros(fields_amount)
        yindex = rawData[0].dtype.names.index(y)
        for q in range(0, fields_amount, 1):
            if q == yindex:
                temp[q] = sum / amount
            else:
                temp[q] = rawData[r][q]
        data[int(r / amount)] = temp
    data.sort(order=x)
    yt = np.append(yt, data[y])
    xt = np.append(xt, data[x])
    ax1.errorbar(data[x], data[y], yerr=ystddev, fmt='o-', capsize=2, label = args.legend[f] if (args.legend != None and len(args.legend) >= f) else "Plot n. " + str(f + 1))
    ax1.legend(loc='lower right')
plt.yticks(np.unique(yt))
plt.xticks(np.unique(xt), rotation=45)
plt.show()
if (args.save):
    fig.savefig(args.fileName + '-plot.pdf')