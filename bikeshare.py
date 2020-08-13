import time
import pandas as pd
import numpy as np

#this project takes in 3 cities and reveals travel information about them.

#creating data strucutures to store relevant information
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_to_num_dict = {'january': 1, 'febuary': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
num_to_month_dict = {1 : 'january', 2: 'febuary', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}
months = ('january', 'febuary', 'march', 'april', 'may', 'june', 'all')
days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', "all")

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
    cities = ("chicago", "new york city", "washington")
    while True:
        city = input("Where would you like to explore: Chicago, New York City, or Washington? \n>").lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("please input month here \n> {} \n>".format(months))
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please input day here \n> {} \n> '.format(days))
        if day in days:
            break


    return city, month, day
    print('-'*40)
    



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
    
    #reading csv into dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #formatting and creating new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['Station Combo']=(df['Start Station'] + " , " +  df['End Station'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    #filter data frame based on month and day if necessary
    if month != 'all':
        df = df[df['month'] == month_to_num_dict[month]]
    if day != 'all':
        df = df[df['day'] == day.capitalize()]

    return df


def highest_count_col_val(df, col_name):
    '''sorts value counts for column in descending order and returns value with highest count'''
    return df[col_name].value_counts().sort_values(ascending = False).index.tolist()[0]

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('most common month is: ')
    print(num_to_month_dict[highest_count_col_val(df, 'month')])

    # TO DO: display the most common day of week
    print('most common day is: ')
    print(highest_count_col_val(df, 'day'))

    # TO DO: display the most common start hour
    print('most common start hour is: ')
    print(highest_count_col_val(df, 'hour'))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('most common start station is: ')
    print(highest_count_col_val(df, 'Start Station'))

    # display most commonly used end station
    print('most common end station is: ')
    print(highest_count_col_val(df, 'End Station'))

    # display most frequent combination of start station and end station trip
    print('most common station combination is: ')
    print(highest_count_col_val(df, 'Station Combo'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration ...\n")
    start_time = time.time()

    # display total travel time
    print("the total travel time is: ")
    print(str(df["Trip Duration"].sum()) + "min")

    # display mean travel time
    print("the mean travel time is: ")
    print(str(df["Trip Duration"].mean()) + "min")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats ...\n')
    start_time = time.time()

    # Display counts of user types
    print("user type counts are: ")
    print(df["User Type"].value_counts())
    
    #displays gender and birth year statistics if applicable 
    if 'Gender' in df.columns:
        # Display counts of gender
        print("gender count is: ")
        print(df["Gender"].value_counts())
    else:
        print('no gender data available')
        
       
    if 'Birth Year'in df.columns:
        # Display earliest, most recent, and most common year of birth
        print( 'The earliest year is: ')
        print(int(df['Birth Year'].min()))
        print( 'The latest year is: ')
        print(int(df['Birth Year'].max()))
        #DISPLAY MOST FREQUENT YEAR
        print('Most common birth year is: ')
        print(int(highest_count_col_val(df, 'Birth Year')))
    else:
        print('no birth year data available')
    
    

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
        
        #displays 5 rows of data if requested
        start_row = 0
        end_row = start_row + 5        
        while True:
            response = input('would you like to see an extra 5 rows of data, yes or no?').lower()
            if response == 'yes':
                print(df[start_row : end_row])
                start_row += 5
                end_row += 5
            elif response == 'no':
                break
                
                     
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    

if __name__ == "__main__":
	main()
