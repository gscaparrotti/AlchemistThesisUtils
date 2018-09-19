import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', action="append", dest="fileName", help="The CSV file containing the data you want to plot", required=True)
parser.add_argument('-l', '--legend', action="append", dest="legend", help="A legend for the corresponding CSV file", required=False, default=[])
parser.add_argument('-a', '--amount', action="store", dest="amount", help="The amount of measurements for each iteration", type=int, required=True)
parser.add_argument('--fields', action="store", dest="fields", help="defines the amount and the names of the columns. Must be the same size of the columns number (eg. 'x,y,z,t')", default="x,y,z,t")
parser.add_argument('--ycolumn', action="store", dest="y", help="The CSV file's column whose content you want to plot (must be a field you specified with the --field option)", default="x")
parser.add_argument('--xcolumn', action="store", dest="x", help="The CSV file's column which distinguishes the different rows of data in each file(must be a field you specified with the --field option)", default="y")
parser.add_argument('--xlabel', action="store", dest="xlabel", help="The label for the X axis", default='')
parser.add_argument('--ylabel', action="store", dest="ylabel", help="The label for the Y axis", default='')
parser.add_argument('-s', '--save', action='store_true', help='Specifies if the produced plot should be saved to file')
args = parser.parse_args()
font = {'weight' : 'normal',
        'size'   : 22}
matplotlib.rc('font', **font)
y = args.y
x = args.x
amount = args.amount
file_n = len(args.fileName)
ys = []
ys_devs = []
tags = []
for tag in args.legend:
    tags.append(str(tag))
if (tags == []):
    for i in range(0, file_n):
        pieces = str(args.fileName[i]).split('/')
        tags.append(pieces[len(pieces) - 1])
for f in range(0, file_n):
    rawData = np.genfromtxt(args.fileName[f], delimiter=' ', names=args.fields)
    rawData.sort(order=x)
    iterations = int(len(rawData) / amount)
    fields_amount = len(rawData[0])
    rawData = np.split(rawData, iterations)[amount - 1]   
    sum = 0.0
    ys_devs.append(np.std(rawData[:amount][y]))
    for e in range(0, amount):
        sum += rawData[e][y]
    yindex = rawData[0].dtype.names.index(y)
    for q in range(0, fields_amount):
        if q == yindex:
            ys.append(sum / amount)
plt.bar(range(0, len(ys)), ys, yerr = ys_devs, tick_label = tags, color = '#cccccc', edgecolor = 'black')
plt.xlabel(args.xlabel)
plt.ylabel(args.ylabel)
plt.show()