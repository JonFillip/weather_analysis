import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "/Users/johnphillip/PycharmProjects/weather_analysis/weather_data" \
           "/san_francisco_2018_full.csv"
with open(filename) as data_type:
    reader = csv.reader(data_type)
    header_row = next(reader)

    # Print header row and index
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # Automate the indexes for key data points.
    date_index = header_row.index('DATE')
    high_temp_index = header_row.index('TMAX')
    low_temp_index = header_row.index('TMIN')

    # Get the dates, highest and lowest temperatures of each day in San
    # Francisco.
    dates, high_temps, low_temps = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            highs = int(row[high_temp_index])
            lows = int(row[low_temp_index])
        except ValueError:
            print(f"Data not found for {current_date}")
        else:
            dates.append(current_date)
            high_temps.append(highs)
            low_temps.append(lows)

    # Style plot
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, high_temps, c='red', alpha=0.5)
    ax.plot(dates, low_temps, c='blue', alpha=0.5)
    # Fill in the gap range between the highest temperature and lowest
    # temperature plot line on the graph
    plt.fill_between(dates, high_temps, low_temps, facecolor='purple',
                     alpha=0.1)
    # Set the plot title and axes label.
    ax.set_title("Daily Weather Summary - 2018\nSan Francisco, CA", fontsize=20)
    ax.set_xlabel("", fontsize=15)
    ax.set_ylabel("Temperature (F)", fontsize=15)
    # Set the size of the label ticks
    ax.tick_params(axis='both', which='major', labelsize=15)
    plt.ylim(10, 150)

if __name__ == '__main__':
    plt.show()
