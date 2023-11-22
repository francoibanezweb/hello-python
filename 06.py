import pandas as pd
pd.set_option("display.max_rows", 15)
reviews = pd.read_csv("archive/winemag-data-130k-v2.csv", index_col=0)

median_points = reviews.points.median()

countries = reviews.country.unique()

reviews_per_country = reviews.country.value_counts()

review_points_mean = reviews.price.mean()
centered_price = reviews.price.map(lambda p: p - review_points_mean)


# Calculo el cociente entre puntos y precio de cada vino.
bargain_idx = (reviews.points / reviews.price).idxmax()

# Encuentro el vino con la mejor relación puntos - precio.
bargain_wine = reviews.loc[bargain_idx, ['title','points','price']]

# ===============
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity],
                              index=['tropical', 'fruity'])

# ===============

def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')

print(star_ratings)

# print(descriptor_counts)

# print(bargain_wine)

# print(centered_price)

# print(reviews_per_country)

# print(median_points)

