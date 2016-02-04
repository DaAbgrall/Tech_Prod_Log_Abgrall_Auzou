import csv

def recuperation (filepatch):
    with open (filepatch,'rt')as csvfile:
        instalReader = csv.reader(csvfile,delimiter=',',quotechar='"')
        for row in instalReader:
            return (row[1])    