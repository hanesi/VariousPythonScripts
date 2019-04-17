import pandas as pd
from io import StringIO
import unidecode

#Initialize Variables
LOGINS_DATA = """DATA IN FORMAT:
DATA\tDATA\tDATA\tDATA\n
DATA\tDATA\tDATA\tDATA\n
DATA\tDATA\tDATA\tDATA\n
DATA\tDATA\tDATA\tDATA\n
"""
COUNTRIES = {1: 'USA', 2: 'Canada', 3: 'Mexico'}

#Define aggregation function
def Aggregator(logins,countries):
    #Use the unidecode library to replace accented characters
    logins_dec = unidecode.unidecode(logins)
    #Use StringIO method to write the LOGINS_DATA as a file
    data = StringIO(logins_dec)
    #Reads the data into a dataframe, delimiter chosen to strip whitespace
    dfLogins = pd.read_csv(data,delimiter = ' *\t *', names = ['timestamp','app_name','number_of_logins','country_id'], engine ='python')
    #Read country data into a dataframe
    dfCountries = pd.DataFrame(list(countries.items()), columns = ['country_id','country'])
    #Join dataframes
    dfCombined = dfLogins.merge(dfCountries, how = 'inner', left_on = 'country_id',right_on = 'country_id')
    #Drop columns not required for aggregation and create aggregate df
    dfToAgg = dfCombined.drop(columns = ['timestamp','country_id'])
    dfAgg = dfToAgg.groupby(['app_name','country']).mean()
    return dfAgg

try:
    print(Aggregator(LOGINS_DATA,COUNTRIES))
except:
    print(traceback.format_exc())








