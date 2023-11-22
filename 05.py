import pandas as pd

reviews = pd.read_csv("archive/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

sample_reviews = reviews.iloc[[1,2,3,5,8]]


cols = ['country','province','region_1','region_2']

df = reviews.loc[[0,1,10,100], cols]


# print(sample_reviews)

print(df)

