import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import resample
from sklearn.preprocessing import LabelEncoder

def up_sampling(flight,max_count):
    """
    checking the praportion of 0(On time) and 1(delayed) for the dependent column ARRIVAL_DELAY15

    doing up sampling
    """
    # Separate majority and minority classes
    delay_rows = flight[flight['ARRIVAL_DELAY15'] == 1]   #minority class
    ontime_rows = flight[flight['ARRIVAL_DELAY15'] == 0]   #majority class

    # Upsample majority class
    delay_rows_upsampled = resample(delay_rows,
                                       replace=True,  # sample without replacement
                                       n_samples=max_count,  # to match minority class
                                       random_state=123 )  # reproducible results

    # Combine majority class with upsampled minority class
    sampledflight = pd.concat([delay_rows_upsampled, ontime_rows])

    return sampledflight

def label_encoder(flight):
    labelEncoder = LabelEncoder()
    flight['CARRIER'] = labelEncoder.fit_transform(flight['CARRIER_CODE'])
    carrier_dict = dict(zip(labelEncoder.classes_, labelEncoder.transform(labelEncoder.classes_)))
    print(carrier_dict)

    flight['ORG_AIRPORT'] = labelEncoder.fit_transform(flight['ORIGIN_AIRPORT'])
    origin_dict = dict(zip(labelEncoder.classes_, labelEncoder.transform(labelEncoder.classes_)))
    print(origin_dict)

    flight['DEST_AIRPORT'] =labelEncoder.fit_transform(flight['DESTINATION_AIRPORT'])
    destination_dict = dict(zip(labelEncoder.classes_, labelEncoder.transform(labelEncoder.classes_)))
    print(destination_dict)


if __name__=='__main__':
    pd.set_option('display.max_columns', 50)
    missingValue = ['n/a', 'Na', '--',' ','']
    flight = pd.read_csv("/home/sunbeam/Dbda Project/flights_Top10.csv",na_values=missingValue,low_memory=False)

    print(flight.columns)

    flight.rename(columns ={'OP_CARRIER' : 'CARRIER_CODE','OP_CARRIER_FL_NUM' : 'FLIGHT_NUMBER','ORIGIN' : 'ORIGIN_AIRPORT',
                           'DEST' : 'DESTINATION_AIRPORT' ,'CRS_DEP_TIME' : 'SCHEDULED_DEPARTURE',
                           'DEP_TIME' : 'ACTUAL_DEPARTURE','DEP_DELAY_NEW' : 'DEPARTURE_DELAY',
                           'DEP_DEL15' :'DEPARTURE_DELAY15','CRS_ARR_TIME' : 'SCHEDULED_ARRIVAL' ,
                           'ARR_TIME'  : 'ACTUAL_ARRIVAL' ,'ARR_DELAY_NEW' : 'ARRIVAL_DELAY' ,
                           'ARR_DEL15' : 'ARRIVAL_DELAY15'}, inplace=True)


    flight.info()

    #column wise datatype , null values and null value percentage
    flight_info = pd.DataFrame(flight.dtypes).T.rename(index={0: 'column type'})
    flight_info = flight_info.append(pd.DataFrame(flight.isnull().sum()).T.rename(index={0: 'null values (nb)'}))
    flight_info = flight_info.append(pd.DataFrame(flight.isnull().sum() / flight.shape[0] * 100)
                               .T.rename(index={0: 'null values (%)'}))

    print(flight_info)

    #dropping the columns which has high null values and which are target leaker
    flight.drop(columns=['Unnamed: 0.1','Unnamed: 0','ACTUAL_ARRIVAL','ACTUAL_DEPARTURE','ARRIVAL_DELAY','CANCELLATION_CODE',
                         'DEPARTURE_DELAY','FLIGHT_NUMBER','DEPARTURE_DELAY15','Unnamed: 0',
                         'CANCELLED'],inplace=True)

    #droping rows with NA from target variable
    flight.dropna(subset=['ARRIVAL_DELAY15'], inplace=True)  #deleting rows for which ARRIVAL_DELAY15 is null

    print("null values - {}".format(flight.isnull().sum()))

    print(flight.info())

    print("Month Range " + str(sorted(flight['MONTH'].unique())))
    print("DAY_OF_MONTH " + str(sorted(flight['DAY_OF_MONTH'].unique())))
    print("DAY_OF_WEEK " + str(sorted(flight['DAY_OF_WEEK'].unique())))
    print("ARRIVAL_DELAY15 " + str(sorted(flight['ARRIVAL_DELAY15'].unique())))

    # showing propartion of delayed and on time flights
    valueCounts = flight['ARRIVAL_DELAY15'].value_counts()
    print("value ditribution for the dependent variable :")
    print(valueCounts)
    max_count = valueCounts.max()

    # resampling the file
    flight =up_sampling(flight,max_count=max_count)

    # label_encoder(cleaned_flight)
    label_encoder(flight)

    fl_corr=flight.drop(columns=['CARRIER_CODE','ORIGIN_AIRPORT','DESTINATION_AIRPORT'])
    flight_corr=fl_corr.corr()
    print("The correlation of target variable with the features :")
    print(flight_corr['ARRIVAL_DELAY15'])

    # cleaned_flight.info()
    flight.info()

    print(flight.columns)

    # flight.to_csv("/home/sunbeam/Dbda Project/flights_Top10_cleaned.csv")
    # flight.to_csv("/home/sunbeam/Dbda Project/flights_Top10_cleaned.csv")


