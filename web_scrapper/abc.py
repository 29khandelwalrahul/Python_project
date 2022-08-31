import csv
import imp
import pandas as pd
filename = 'web_scrapper\data.csv'

r = pd.read_csv(filename,nrows=-3)
print(r)