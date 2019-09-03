"""
This program is used to analyze bike sharing data in Chicago, New York City and Washington
"""


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:   
        city = input('Which city do you want to explore? Chicago, New York City, or Washington?')
        if city.lower() not in ['chicago', 'new york city', 'washington']:
            print('Invalid response. Please select Chicago, New York City or Washington')
        else:
            break
        # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('What month do you want to explore? January, February, March, April, May, June or all?')
        if month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print('Invalid response. Please select  January, February, March, April, May, June or all.')
        else:
            break

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('What day do you want to explore? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?')
        if day.lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print('Invalid response. Please select  Monday, Tuesday, Wednesday, Thursday, Friday, Satuday, Sunday or all.')
        else:
            break
              
    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0] 
    print ('\nThe most popular month is\n', popular_month)
        # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0] 
    print ('\nThe most popular day is\n', popular_day)

        # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0] 
    print ('\nThe most popular starting hour is\n', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print ('\nThe most popular starting station is\n', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print ('\nThe most popular end station is\n', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print ('\nThe most popular combination of start and end station is\n', popular_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('\The total travel time was\n', total_travel_time, 'minutes')
                           
    # TO DO: display mean travel time
  
    avg_travel_time = df['Trip Duration'].mean()
    print ('\The average travel time was\n', avg_travel_time, 'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe user types are {}:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('\nThe counts of gender type are:\n', gender_types)
    else:
        print('\nSorry, gender data does not exist for Washington.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        oldest_yob = df['Birth Year'].min()
        print('\nThe oldest person was born in:\n', int(round(oldest_yob)))
        youngest_yob = df['Birth Year'].max()
        print('\nThe oldest person was born in:\n', int(round(youngest_yob)))
        common_yob = df['Birth Year'].mode()[0]
        print('\nThe most common birth year is:\n', int(round(common_yob)))
    else:
        print('\nSorry, birth year does not exist for Washington.\n')
    x=0
    y=5
    while True:
        raw = input('\nWould you like to see indiviudal lines of data? Yes or no.\n')
        if raw.lower() in ['yes']:
                print(df.iloc[x:y])
                x += 5
                y += 5
        elif raw.lower() in ['no']:
            break
        else:
            print('\nSorry, please choose yes or no.\n')
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
