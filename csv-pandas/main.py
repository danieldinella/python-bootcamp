import pandas

data = pandas.read_csv("centralPark.csv")
print(data["Primary Fur Color"].value_counts())