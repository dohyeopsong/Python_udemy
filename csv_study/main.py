import pandas

data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].to_list()

# # print(data.temp.mean())
# # print(data["temp"].max())

# # print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday = monday.to_dict()
# monday_temp_F = monday_temp * 9/5 + 32

print(monday)

#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 21, 55]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# print(data)

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# # print(gray_squirrels_count)
# # print(red_squirrels_count)
# # print(black_squirrels_count)

# data_dict = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrels_count.csv")

# data = pandas.read_csv("squirrels_count.csv")
# print(data)