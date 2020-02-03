import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "weather_data/austin_weather_2010_2020.csv"
with open(filename) as weather_file:
    reader = csv.reader(weather_file)
    # Print out first row to check the indexes of the keys for the data types
    # in the file
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #   print(index, column_header)

    # Get the dates, highest and lowest temps of the each day from the records.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high_temp = int(row[6])
            low_temp = int(row[7])

        except ValueError:
            print(f"Data not found for {current_date}")

        else:
            dates.append(current_date)
            highs.append(high_temp)
            lows.append(low_temp)

    # Style plot
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    # Fill in the gap range between the highest and lowest temperature in the
    # graph
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Set the chart title and labels
    ax.set_title("Daily High and Low temperature 2010 - 2020\nAustin Texas",
                 fontsize=25)
    ax.set_xlabel('', fontsize=10)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=10)

    # Set the size of the tick labels
    ax.tick_params(axis='both', which='major', labelsize=14)

if __name__ == '__main__':
    plt.show()
