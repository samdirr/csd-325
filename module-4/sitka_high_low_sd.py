"""
Sam Dirr
Module 4 Assignment - High/Low Temperatures

This program reads weather data from sitka_weather_2018_simple.csv and lets the
user choose whether to view a graph of daily high temperatures, daily low
temperatures, or exit the program. The menu continues to loop until the user
chooses to exit.
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


FILENAME = 'sitka_weather_2018_simple.csv'


def load_weather_data(filename):
    """Read the CSV file and return dates, highs, and lows."""
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows



def plot_temperatures(dates, temperatures, title_text, line_color):
    """Plot the selected temperatures."""
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=line_color)

    plt.title(title_text, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()



def display_menu():
    """Display the menu instructions."""
    print('\nSitka Weather Menu')
    print('Enter H to view daily high temperatures.')
    print('Enter L to view daily low temperatures.')
    print('Enter E to exit the program.')



def main():
    """Run the main menu loop for the program."""
    dates, highs, lows = load_weather_data(FILENAME)

    while True:
        display_menu()
        choice = input('Your choice: ').strip().lower()

        if choice == 'h':
            plot_temperatures(dates, highs, 'Daily High Temperatures - 2018', 'red')
        elif choice == 'l':
            plot_temperatures(dates, lows, 'Daily Low Temperatures - 2018', 'blue')
        elif choice == 'e':
            print('Exiting program. Thank you for using the Sitka Weather viewer.')
            sys.exit()
        else:
            print('Invalid selection. Please enter H, L, or E.')


if __name__ == '__main__':
    main()
