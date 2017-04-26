import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--index', action="store", dest="index", help="The index of the parameter you want to write to the CSV file (besides the variables)", type=int, default=-1)
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
            variableList = lines[file_len(s) - 4].split()
            if (i == -1):
                variable = variableList[variableList.length - 1]
            else:
                variable = variableList[i]
            result = open("results.csv", "a")
            result.write(variable)
            for td in timeDistributions:
                result.write(" ")
                result.write(td)
            result.close()