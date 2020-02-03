import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "weather_data/sitka_weather_2018_full.csv"
with open(filename) as weather_record:
    reader = csv.reader(weather_record)
    header_row = next(reader)

    # Print the header row of the file to check the index of the data types
    # in the file.
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates and rainfall (PRCP) parameter from the weather record.
    dates, prcp = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rainfall = float(row[5])
        except ValueError:
            print(f"Data not found for {current_date}.")
        else:
            dates.append(current_date)
            prcp.append(rainfall)

    # Style the plot
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots()
    ax.plot(dates, prcp, c='blue')

    # Set the chart title and label axes
    ax.set_title("Sitka, Alaska Rainfall 2018", fontsize=24)
    ax.set_xlabel('', fontsize=10)
    fig.autofmt_xdate()
    ax.set_ylabel("Precipitation (inches)", fontsize=15)

    # Set the size of the tick labels.
    ax.tick_params(axis='both', which='major', labelsize=14)


if __name__ == "__main__":
    plt.show()
