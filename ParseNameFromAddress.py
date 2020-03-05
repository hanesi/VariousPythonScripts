# Sometimes address data can have the addressee's name in the same field as the address
# This script uses Regex to remove the addressee's name from the address string

import pandas as pd
import re

key = "some file key.csv"
fp = f"/Users/ianhanes/downloads/files-14/{key}"
df = pd.read_csv(fp)


def findAddress(address):
    regex_obj = re.search(r"\d|P.O. BOX|PO BOX", address)
    index = regex_obj.start()
    return address[index:]
    #To return the full name, just return address[:index] as well
    
df["street"] = df["Customer Full Address"].apply(findAddress)
