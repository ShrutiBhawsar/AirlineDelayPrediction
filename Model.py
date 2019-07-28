import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib


def printAccuracy(model,cm):
    total = sum(sum(cm))
    accurate = sum(np.diagonal(cm))
    accuracy = (accurate / total) * 100
    print('{} accuracy: {}%'.format(model,accuracy))

def LogisticClasifier(x_train, x_test, y_train, y_test):
    classifier = LogisticRegression()
    classifier = classifier.fit(x_train, y_train)
    predictions = classifier.predict(x_test)
    cm = confusion_matrix(y_test, predictions)
    printAccuracy('Logistic Classifier',cm)


def featureSelection(flight_labels,x_train, x_test, y_train, y_test):
    classifier = RandomForestClassifier(n_estimators=50, n_jobs=-1, criterion='gini',
                                        max_features='auto', class_weight='balanced', random_state=0)
    original = classifier.fit(x_train, y_train)

    print("*****************original prediction**********************")

    predictions = original.predict(x_test)
    probabilities = original.predict_proba(x_test)
    roc_auc = roc_auc_score(y_test, probabilities[:, 1])
    print("Accuracy score is {}".format(accuracy_score(y_test, predictions)))
    print("roc auc score is : {}".format(roc_auc))

    print("*****************important features prediction**********************")

    for feature in zip(flight_labels, original.feature_importances_):
        print(feature)
    sfm = SelectFromModel(original, threshold=0.08)
    sfm.fit(x_train, y_train)
    X_important_train = sfm.transform(x_train)
    X_important_test = sfm.transform(x_test)

    clf_important =classifier.fit(X_important_train, y_train)

    y_important_pred = clf_important.predict(X_important_test)
    clf_probabilities = clf_important.predict_proba(X_important_test)
    roc_auc = roc_auc_score(y_test, clf_probabilities[:, 1])
    print("Accuracy score is {}".format(accuracy_score(y_test, y_important_pred)))
    print("roc auc score is : {}".format(roc_auc))


def randomForest(flight_labels,x_train, x_test, y_train, y_test):

    classifier = RandomForestClassifier(n_estimators=50,n_jobs=-1,criterion='gini',
                                        max_features='auto',class_weight='balanced',random_state=42)
    classifier = classifier.fit(x_train, y_train)

    #checking for overfitting
    all_accuracies = cross_val_score(estimator=classifier, X=x_train, y=y_train, cv=5)
    print("K fold accuracies : {}".format(all_accuracies))
    print("K fold accuracies mean {}".format(all_accuracies.mean()))
    print("K fold accuracies std dev {}".format(all_accuracies.std()))

    predictions = classifier.predict(x_test)
    probabilities = classifier.predict_proba(x_test)
    roc_auc = roc_auc_score(y_test, probabilities[:, 1])

    print("Accuracy score is {}".format(accuracy_score(y_test, predictions)))
    cm = confusion_matrix(y_test, predictions)
    print("Performance Metrics is : ")
    print(cm)
    print("roc auc score is : {}".format(roc_auc))
    filename = '/home/sunbeam/Dbda Project/AirlineDelayPrediction/Airline-Model.sav'
    joblib.dump(classifier, filename)


if __name__=='__main__':
    flight=pd.read_csv("/home/sunbeam/Dbda Project/flights_Top10_cleaned.csv")


    flight.drop(columns=['Unnamed: 0','CARRIER_CODE','ORIGIN_AIRPORT','DESTINATION_AIRPORT','DISTANCE','YEAR'],inplace=True)

    print(flight.info())

    #spliting the sample data into training and testting
    delay_label = flight['ARRIVAL_DELAY15']
    flight.drop(columns=['ARRIVAL_DELAY15'],inplace=True) #removing target variable

    x_train, x_test, y_train, y_test = train_test_split(flight, delay_label, test_size=0.2)

    flight_labels = flight.columns

    # featureSelection(flight_labels,x_train, x_test, y_train, y_test)
    randomForest(flight_labels,x_train, x_test, y_train, y_test)
    # LogisticClasifier(x_train, x_test, y_train, y_test)







