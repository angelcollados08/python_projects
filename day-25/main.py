import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#print(data["Primary Fur Color"])

red_list = data[data["Primary Fur Color"] == "Cinnamon"]
print(red_list["Hectare Squirrel Number"].sum())

grey_list = data[data["Primary Fur Color"] == "Gray"]
print(grey_list["Hectare Squirrel Number"].sum())

black_list = data[data["Primary Fur Color"] == "Black"]
print(black_list["Hectare Squirrel Number"].sum())

data_dict = {
    "colors" : ["red","grey","black"],
    "number" : [red_list["Hectare Squirrel Number"].sum(),grey_list["Hectare Squirrel Number"].sum(),black_list["Hectare Squirrel Number"].sum()]
}

data2 = pandas.DataFrame(data_dict)
data2.to_csv("new_Data_squirel.csv")