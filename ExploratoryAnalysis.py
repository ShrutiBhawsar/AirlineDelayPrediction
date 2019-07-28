import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def flight_correlation(flight):
    flight_corr = flight.drop(columns=['CARRIER_CODE', 'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT'])
    fCorr=flight_corr.corr()
    sns.heatmap(fCorr, vmax=1.0, center=0, fmt='.2f',
                square=True, linewidths=.5, annot=True, cbar_kws={"shrink": .50})
    plt.show();


def flight_exploratoryAnalysis(flight):
    flight['delayed'] = flight['ARRIVAL_DELAY15'].apply(lambda x: x == 1)
    flight['on_time'] = flight['ARRIVAL_DELAY15'].apply(lambda x: x == 0)

    delayed_flight = flight['delayed'].value_counts()[1]  # True = 1
    onTime_flight_ = flight['on_time'].value_counts()[1]  # False = 0


    #1. Percentage of Delayed-flights Vs On-Time-flights in the year 2018
    plt.figure(1)
    plt.pie([delayed_flight, onTime_flight_], labels=['delayed', 'On_time'], colors=['yellowgreen', 'lightcoral'], autopct='%1.1f%%',shadow=True)
    plt.legend(labels=['delayed', 'On_time'])
    plt.title('Percentage of Delayed-flights Vs On-Time-flights in the year 2018')


    # Month wise number of flight delay chart

    month_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep','Oct','Nov','Dec']
    monthwise_flightdelay =[]

    #counting monthwise delayed flights
    for i in range(1,13):
        monthwise_flightdelay.append(flight[flight['MONTH'] == i]['delayed'].sum())

    index=np.arange(len(month_label))
    plt.figure(2)
    plt.bar(index, monthwise_flightdelay,align='center', alpha=1)
    plt.xlabel('Months', fontsize=15)
    plt.ylabel('No of delayed flights', fontsize=15)
    plt.xticks(index, month_label, fontsize=10, rotation=30)
    plt.title('Month wise number of delayed flights')
    # plt.show()

    # Week wise number of flight delay chart

    weekday_label = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekWise_flightdelay = []

    # counting weekwise delayed flights
    for i in range(1, 8):
        weekWise_flightdelay.append(flight[flight['DAY_OF_WEEK'] == i]['delayed'].sum())

    index = np.arange(len(weekday_label))

    plt.figure(3)
    plt.bar(index, weekWise_flightdelay, align='center', alpha=1,color='lightgreen')
    plt.xlabel('WeekDay', fontsize=10)
    plt.ylabel('No of delayed flights', fontsize=10)
    plt.xticks(index, weekday_label, fontsize=8, rotation=30)
    plt.title('Week wise number of delayed flights')
    # plt.show()

    plt.figure(4)
    group = flight.groupby(['DAY_OF_MONTH'], as_index=False).aggregate(np.mean)[['DAY_OF_MONTH', 'ARRIVAL_DELAY15']]
    group.sort_values(by='DAY_OF_MONTH', inplace=True)
    group.plot.bar(x='DAY_OF_MONTH', y='ARRIVAL_DELAY15')
    plt.ylabel('Percent of Flights that Arrive Late')
    plt.title('DAY_OF_MONTH wise flight delay')

    series_labels = ['Delayed', 'On-Time']

    plt.figure(5, figsize=(15, 5))
    group = flight.groupby(['CARRIER_CODE'],as_index=False).aggregate(np.mean)[['CARRIER_CODE', 'ARRIVAL_DELAY15']]
    group.sort_values(by='CARRIER_CODE', inplace=True)
    group.plot.bar(x='CARRIER_CODE', y='ARRIVAL_DELAY15',color='lightgreen')
    plt.ylabel('Percent of Flights that Arrive Late')
    plt.title('CARRIER_CODE wise flight delay')
    plt.show()







if __name__=='__main__':
    # pd.set_option('display.max_columns', 50)
    flight=pd.read_csv("/home/sunbeam/Dbda Project/flights_Top10_cleaned.csv")
    print(flight.columns)


    flight.drop(columns=['Unnamed: 0'],inplace=True)
    # data_preparation(flight)
    flight_exploratoryAnalysis(flight)
    flight_correlation(flight)