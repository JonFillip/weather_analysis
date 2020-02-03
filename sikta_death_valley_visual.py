import csv
import matplotlib.pyplot as plt
from datetime import datetime


def get_weather_visual(filename, dates, highs, lows, date_index, highs_index,
                       lows_index):
    """Retrieve key data points from the weather records for sitka city,
    AK and Death Valley, CA."""
    with open(filename) as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)

        # Get the dates, highest and lowest temperatures of each day.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high_temps = int(row[highs_index])
                low_temps = int(row[lows_index])
            except ValueError:
                print(f"Data not found for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high_temps)
                lows.append(low_temps)


# Get weather key data points for Sikta.
record_name = "weather_data/sitka_weather_2018_full.csv"
specific_date, high_temp, low_temp = [], [], []
get_weather_visual(record_name, specific_date, high_temp, low_temp,
                   date_index=2, highs_index=8, lows_index=9)
# Set plot style for Sitka.
plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.plot(specific_date, high_temp, c='red', alpha=0.5)
ax.plot(specific_date, low_temp, c='blue', alpha=0.5)
# Fill in the gap between the highest and lowest temperature range on the graph
plt.fill_between(specific_date, high_temp, low_temp, facecolor='gray',
                 alpha=0.1)

# Get the dates, highest and lowest daily temperatures for Death Valley.
record_name = "weather_data/death_valley_2018_full.csv"
dates, highs, lows = [], [], []
get_weather_visual(record_name, dates, highs, lows, date_index=2, highs_index=6,
                   lows_index=7)
# Set plot style for Death Valley
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
# Fill in the gap between the highest and lowest temperature range on the graph
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Set plot title and axes labels
ax.set_title("Daily weather summary 2018,\nSITKA AIRPORT, AK & DEATH VALLEY, "
             "CA USA", fontsize=25)
ax.set_xlabel("", fontsize=15)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=15)
# Set the size of the tick labels
ax.tick_params(axis='both', which='major', labelsize=10)
plt.ylim(10, 150)

if __name__ == "__main__":
    plt.show()
