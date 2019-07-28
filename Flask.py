
from flask import Flask, request,  render_template,send_from_directory
import pandas as pd
import numpy as np
import datetime
import AirlineDictonary as ad
from datetime import date
from sklearn.externals import joblib
import os


path = '/home/sunbeam/Dbda Project/AirlineDelayPrediction/Airline-Model.sav'
model=joblib.load(path)

class InvalidUserInputError(Exception):
   """Raised when the input value is invalid"""
   pass

class InvalidDateInputError(Exception):
   """Raised when the input date is invalid invalid"""
   pass

# PEOPLE_FOLDER = os.path.join('static', 'figure')



app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER



@app.route('/')
@app.route('/home')
def home():
    # leng = len(Carrier_code)
    return render_template('form.html',carrier_code=ad.carrier_code,origin_code=ad.origin_code,destination_code=ad.destination_code,
                           Ahour=ad.hour_list,Aminute=ad.minute_list,Dhour=ad.hour_list,Dminute=ad.minute_list)

@app.route('/', methods=['POST'])
def getUserInput():
    str_date = request.form['journeydate']
    str_ORG_AIRPORT = request.form['origin']
    str_DEST_AIRPORT = request.form['destination']
    str_CARRIER = request.form['airlineCode']
    str_Ahour = request.form['Ahour']
    str_Aminute = request.form['Aminute']
    str_Dhour = request.form['Dhour']
    str_Dminute = request.form['Dminute']

    today = str(datetime.date.today())
    print("today ", today)
    warning = "ERROR!!! "
    if str_ORG_AIRPORT == str_DEST_AIRPORT:
        warning += "Origine Airport and Destination Airport CAN NOT be same."
    if str_date <= today:
        warning += "Invalid Date!! Date should be greater than today's date"
    else:
        warning ="ERROR!!! Please fill all the fields with valid details. All fields are Mendatory!!"
    try:
        if str_ORG_AIRPORT is "Select-Option" or str_DEST_AIRPORT is "Select-Option"  or str_CARRIER is "Select-Option"  or str_Ahour is "Select-Option"  or str_Aminute is "Select-Option"  or str_Dhour is "Select-Option"  or str_Dminute is "Select-Option" :
            raise InvalidUserInputError
        else:
            # today = str(datetime.date().today())
            # print("today " ,today)
            if str_date <= today :
            #     result =" Invalid Date!! Date should be greater than today's date"
                raise InvalidDateInputError
            else:
                # date
                print("date", str_date)
                date = str_date.split("-")
                YEAR = int(date[0])
                MONTH = int(date[1])
                DAY_OF_MONTH = int(date[2])
                DAY_OF_WEEK = (datetime.date(YEAR, MONTH, DAY_OF_MONTH).weekday() + 1)

                ORIGIN = int(ad.origin_dict.get(str_ORG_AIRPORT,0))
                DESTINATION = int(ad.destination_dict.get(str_DEST_AIRPORT,0))
                CARRIER = int(ad.carrier_dict.get(str_CARRIER,0))
                ARV_TIME = int(str_Ahour + str_Aminute)
                DPT_TIME = int(str_Dhour + str_Dminute)

                print("month " ,MONTH)
                print("Day of month ",DAY_OF_MONTH)
                print("Weekday ", DAY_OF_WEEK)
                print("origin " ,ORIGIN )
                print("destination" , DESTINATION)
                print("carrier ", CARRIER)
                print("arrival ",ARV_TIME)
                print("departure ",DPT_TIME)
                # result = str_date + " " + str_ORG_AIRPORT + " " + str_DEST_AIRPORT + " " + str_CARRIER + " " + str_Ahour + " " + str_Aminute + " " + str_Dhour + " " + str_Dminute
                DataList = [(DAY_OF_MONTH, DAY_OF_WEEK, MONTH, ARV_TIME, DPT_TIME, CARRIER, ORIGIN,
                             DESTINATION)]

                flight_data = pd.DataFrame(DataList, columns=['MONTH','DAY_OF_MONTH', 'DAY_OF_WEEK', 'DPT_TIME',  'ARV_TIME',
                                                       'CARRIER', 'ORIGIN','DESTINATION'])
                print(flight_data.info())

                prediction_result = model.predict(flight_data)
                print(" The prediction of {} is {} ".format(flight_data,prediction_result))
                print(type(prediction_result))

                # generate response
                if prediction_result[0] == 0.0:
                    prediction = 'It might get delay by 15 min, which is usually considered as On-Time'
                else:
                    prediction = 'It might get delayed by more than 15 min, which is considered as Delayed'

                # # send response
                return render_template('predict.html', CARRIER=CARRIER, ORIGIN=ORIGIN,MONTH=MONTH,
                                       DAY_OF_MONTH=DAY_OF_MONTH,DAY_OF_WEEK=DAY_OF_WEEK,
                                       DESTINATION=DESTINATION,ARV_TIME=ARV_TIME,DPT_TIME=DPT_TIME,
                                        RESULT=prediction)

    except:
        return render_template('form.html', carrier_code=ad.carrier_code, origin_code=ad.origin_code,
                               destination_code=ad.destination_code,
                               Ahour=ad.hour_list, Aminute=ad.minute_list, Dhour=ad.hour_list, Dminute=ad.minute_list,
                               result=warning)


@app.route('/analysis', methods=['POST'])
def showAnalysis():
    return render_template('analysis.html')





if __name__ == '__main__':
   app.run(debug = True)
