import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
days = ['monday', 'tuesday', 'wendesday', 'thursday', 'friday', 'saturday', 'sunday']


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
        city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month do you want to filter the data by? January, February, March, April, May, June, or all?').lower()
        if month in months or month == 'all':
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day do you want to filter the data by? Monday, Tuesday, Wendesday, Thursday, Friday, Saturday, Sunday or All?').lower()
        if day in days or day == 'all':
            break

    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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
    most_month = df['month'].value_counts().idxmax()
    print('The most common month: ', most_month)

    # TO DO: display the most common day of week
    most_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day: ', most_day)

    # TO DO: display the most common start hour
    most_hour = df['hour'].value_counts().idxmax()
    print('The most common hour: ', most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station: ', most_start)

    # TO DO: display most commonly used end station
    most_end = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station: ', most_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_start_end = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most frequent combination of start station and end station trip is: ', most_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_time = df['Trip Duration'].sum()
    print('Total travel time: ', tot_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_utype = df['User Type'].value_counts()
    print('Counts of user types: ', count_utype)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('Counts of user types: ', count_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        print('Earliest year of birth: ', earliest_birth)
        recent_birth = df['Birth Year'].max()
        print('Earliest year of birth: ', recent_birth)
        common_birth = df['Birth Year'].value_counts().idxmax()
        print('Earliest year of birth: ', common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
