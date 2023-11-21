import pandas as pd

reviews = pd.read_csv("archive/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

desc = reviews['description']

print(desc)


