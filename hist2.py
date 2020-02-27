import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', action="store", dest="fileName", help="The CSV file containing the data you want to plot", required=True)
parser.add_argument('--fields', action="store", dest="fields", help="defines the amount and the names of the columns. Must be the same size of the columns number (eg. 'x,y')", default="x,y")
parser.add_argument('--ycolumn', action="store", dest="y", help="The CSV file's column whose content you want to plot (must be a field you specified with the --field option)", default="y")
parser.add_argument('--xcolumn', action="store", dest="x", help="The CSV file's column which distinguishes the different rows of data in each file(must be a field you specified with the --field option)", default="x")
parser.add_argument('--xlabel', action="store", dest="xlabel", help="The label for the X axis", default='')
parser.add_argument('--ylabel', action="store", dest="ylabel", help="The label for the Y axis", default='')
parser.add_argument('-s', '--save', action='store_true', help='Specifies if the produced plot should be saved to file')
args = parser.parse_args()
font = {'weight' : 'normal',
        'size'   : 18}
matplotlib.rc('font', **font)
y = args.y
x = args.x
ys = []
tags = []
rawData = np.genfromtxt(args.fileName, delimiter='|', names=args.fields, dtype=[('f0', '<U20'), ('f1', '<f8')])
rawData.sort(order=y)
for k in range (0, len(rawData)):
    ys.append(rawData[k][y])
    tags.append(rawData[k][x])
plt.bar(range(0, len(ys)), ys, tick_label = tags, color = '#cccccc', edgecolor = 'black')
plt.xlabel(args.xlabel)
plt.ylabel(args.ylabel)
if (args.save):
    plt.savefig(args.fileName[0:args.fileName.rfind(".")] + '-plot.pdf')
plt.show()
