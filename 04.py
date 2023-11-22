import pandas as pd

reviews = pd.read_csv("archive/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

desc = reviews['description']

first_description = reviews['description'][0]


print("desc es :",type(desc),"\n")

print("Seleccionando el primer elemento de la columna description: \n",
        first_description,"\n")

print(desc)


