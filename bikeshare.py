import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']
months=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December','All']
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']

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
        city=str(input('Which city do you want to view: \n')).lower()
        if city not in cities:
            print("Kindly choose between chicago, new york city and washington")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=str(input('Enter the month you wish to get more insights of, If all type all  \n')).title()
        if month not in months:
            print('Kindly share a valid month')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=str(input('Which day do you want to filter with?, If all type all ')).title()
        if day not in days:
            print('Please enter a valid day')
        else:
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day

    if month != 'all':
        month = months.index(month)+1
        df = df[df['month'] == month]

#     if day != 'all':
#         df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month 
    print("The most common month is: ", df['month'].value_counts().idxmax())
    # TO DO: display the most common day of week
    print('The most common day of the week is {}' .format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    print('The most common start hour is {}' .format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is {}' .format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end statation is {}' .format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df['Start Station'].map(str) + 'to' + ['End Station']
    print('Most common start and end station are {}' .format(common_start_end_station.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_m, total_s = divmod(df['Trip Duration'].sum(), 60)
    total_h, total_m = divmod(total_m, 60)
    print ('The total travel time is: ',total_h,' hours, ', total_m,' minutes, and ', total_s,' seconds.')


    # TO DO: display mean travel time
    mean_m, mean_s = divmod(df['Trip Duration'].mean(), 60)
    mean_h, mean_m = divmod(mean_m, 60)
    print ('The mean travel time is: ',mean_h,' hours, ', mean_m,' minutes, and ', mean_s,' seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The user counts is {}' .format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if('Gender' not in df):
          print('Not Applicable')
    else:
          print('The genders are {}' .format(df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Year of birth' not in df):
        print('Year of birth Not avalilable')
    else:
        print('The Earliest Year of birth is {}'.format(df['Year of birth'].min()))
        print('The most recent Year of birth is {}'.format(df['Year of birth'].max()))              
        print('The most common Year of birth is {}'.format(df['Year of birth'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_data(df):
    input('Do you want to view individual raw data?, Yes or No \n' , ).lower()
    start_loc = 0
    while(input()!='no'):
        start_loc += 5
        print(df.head(start_loc))
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
