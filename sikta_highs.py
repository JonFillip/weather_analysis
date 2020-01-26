import csv

filename = "/Users/johnphillip/PycharmProjects/weather_analysis/weather_data" \
           "/sitka_weather_07-2018_simple.csv"
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    print(header_row)
