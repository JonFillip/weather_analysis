import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "weather_data/death_valley_2018_full.csv"
with open(filename) as file_object:
    read_file = csv.reader(file_object)
    header_row = next(read_file)

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates and highest temperatures for Death valley.
    dates, highs, lows = [], [], []
    for row in read_file:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high_temp = int(row[6])
            low_temp = int(row[7])
        except ValueError:
            print(f"Missing data for {current_date}")
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
    ax.set_title("Daily High & Low Temperatures - 2018\nDeath Valley, CA",
                 fontsize=24)
    ax.set_xlabel("", fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=14)
    # Set the size of the tick labels.
    ax.tick_params(axis='both', which='major', labelsize=14)
    # Set a limit for the y-axis
    plt.ylim(10, 150)

if __name__ == "__main__":
    plt.show()
