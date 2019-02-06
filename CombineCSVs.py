"""
This script efficiently combines csv's into one file
"""
import shutil
import glob

#import csv files from folder
path = r'PATH TO FILES'
allFiles = glob.glob(path + "/*.csv")
with open(path + r'\06_Output.csv', 'wb') as outfile:
    for i, fname in enumerate(allFiles):
        with open(fname, 'rb') as infile:
            #Only take the header from the first file
            if i != 0:
                infile.readline()
            # Use shutil to block copy the contents of the file to the output
            shutil.copyfileobj(infile, outfile)
            print(fname + " has been imported.")
