import csv

def recuperation (filepatch):
    with open (filepatch,'rt')as csvfile:
        instalReader = cvs.reader(cvsfile,delimiter=',',quotechar='"')
        for row in instalReader:
            return (row[1])    