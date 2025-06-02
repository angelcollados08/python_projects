# with open("weather_data.csv","r") as file:
#     data = file.readlines()

# print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# print (temperatures)

import pandas
import numpy as np

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()

monday = data[data.day == "Monday"]
print(monday.temp[0]*9/5 +32)

data_dict = {
    "students" : ["anme","dfd","fewf"],
    "scores" : [1,2,3]
}

data2 = pandas.DataFrame(data_dict)
data2.to_csv("new_Data.csv")