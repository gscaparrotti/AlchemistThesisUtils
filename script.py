import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--index', action="store", dest="index", help="The index of the parameter you want to write to the CSV file (besides the variables, defaults to the last one)", type=int, default=-1)
parser.add_argument('-a', '--average', action="store_true", dest="avg", help="Evaluates the average value between all the lines in the file instead of picking just the last value")
args = parser.parse_args()

i = int(args.index)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

for s in os.listdir():
    if "export" in s:
        with open(s, "r") as file:
            lines = file.readlines()
            timeDistributions = []
            for l in lines[3].split(','):
                timeDistributions.append(l.split(" = ")[1])
            endLine = file_len(s) - 4
            variableList = lines[endLine].split()
            if (i == -1):
                firstRun = False
                i = len(variableList) - 1
            elif (i < 0 or i > len(variableList)):
                sys.exit("The index must be a value between 0 and " + str(len(variableList) - 1) + " (it was " + str(i) + ")");
            if (args.avg):
                average = 0
                tot = 0
                for l in range(7, endLine + 1, 1):
                    average += float(lines[l].split()[i])
                    tot += 1
                variableList[i] = average / tot
            variable = variableList[i]
            result = open("results.csv", "a")
            result.write(str(variable))
            for td in timeDistributions:
                result.write(" ")
                result.write(td)
            result.close()