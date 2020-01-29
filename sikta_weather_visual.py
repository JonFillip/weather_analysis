import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "/Users/johnphillip/PycharmProjects/weather_analysis/weather_data" \
           "/sitka_weather_2018_simple.csv"
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    # To print the header row in the file.
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates and highest temperatures from the weather record file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high_temp = int(row[5])
            low_temp = int(row[6])
        except ValueError:
            print(f"Data not found for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high_temp)
            lows.append(low_temp)

    # style plot
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    # Fill in the gap range between the high and low temperature on the graph.
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Set the chart title and label axes
    ax.set_title("Daily High & Low Temperatures - 2018\nSitka, AK",
                 fontsize=24)
    ax.set_xlabel("", fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=14)
    # Set the size of the tick labels.
    ax.tick_params(axis='both', which='major', labelsize=14)


if __name__ == "__main__":
    plt.show()
