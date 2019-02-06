import shutil
import glob

#import csv files from folder
path = r'C:\Users\hanesi\Desktop\Projects\Python\06\csv'
allFiles = glob.glob(path + "/*.csv")
with open(path + r'\06_Output.csv', 'wb') as outfile:
    for i, fname in enumerate(allFiles):
        with open(fname, 'rb') as infile:
            if i != 0:
                infile.readline()  # Throw away header on all but first file
            # Block copy rest of file from input to output without parsing
            shutil.copyfileobj(infile, outfile)
            print(fname + " has been imported.")
