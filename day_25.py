import pandas
data = pandas.read_csv("weather_data.csv")

print(type(data["temp"]))
data_dict = data.to_dict()
print(data_dict)
print(data["temp"].sum()/len(data["temp"]))
print(data["temp"].max())
print(data[data.temp == data["temp"].max()])
monday = data[data.day == "Monday"]
monday_temp=monday.temp[0]
print(monday_temp)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240826.csv")
Grey = len(data[data["Primary Fur Color"] == "Gray"])
Red = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black = len(data[data["Primary Fur Color"] == "Black"])

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[Grey,Red,Black]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")