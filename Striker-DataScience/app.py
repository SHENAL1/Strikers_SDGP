from flask import Flask, jsonify

import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import pickle
from pymongo import MongoClient
#from pymongo import dnspython
#import matplotlib.pyplot as plt
#import seaborn as sns

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

#Getting the connection from Mongo Db Atlas using MongoClient
cluster = MongoClient("mongodb+srv://admin:admin@striker-spfii.mongodb.net/test?retryWrites=true&w=majority")
#Acessing the Database
db = cluster.get_database("StrikerDatabase")
#acessing the collection
collection = db.get_collection("playerdetails")


@app.route('/goalkeeper')
def goalkeeper():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Reactions", "Composure", "Sprint_Speed", "Strength", "Jumping", "GK_Positioning", "GK_Diving",
         "GKReflexes", "GK_Handling", "GK_Kicking", "Vision", "Age"]]

    # Drop the rows where at least one element is null:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  # drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

    """"
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("goalkeeper.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    """
    # load file
    pickle_in = open("goalkeeper.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module is 1 ", acc)

    # prediction values of test data.
    predictions = linear.predict(x_test)

    # Plot the actual value vs model predict value
    """
    width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")

    plt.title("Actual vs fitted value for goalkeeper")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("Top Ratings of the Goal Keepers :\n")

    # Finding the values that contain Position = "GK" To get the goal keepers from the collection
    result = collection.find({"Position": "GK"})

    # create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Reactions"], x["Composure"], x["Sprint_Speed"], x["Strength"], x["Jumping"], x["GK_Positioning"],
                 x["GK_Diving"], x["GKReflexes"], x["GK_Handling"], x["GK_Kicking"], x["Vision"], x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Passing the data2 array to the prediction
        re = linear.predict(np.array([data2]))[0]

        # append values to the list
        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/leftWingBack')
def leftWingBack():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking","Reactions", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  # drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    """
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("leftWingBack.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    """
    # load file
    pickle_in = open("leftWingBack.pickle", "rb")
    linear = pickle.load(pickle_in)
    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    #calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 2 is  ", acc)

    #prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")

    plt.title("Actual vs fitted value for leftWingBack")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Ratings of the Left Wing Back:\n")

    # Finding the values that contain Position = "LWB" To get the Left Wing Back from the collection
    result = collection.find({"Position": "LWB"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Ball_Control"], x["Dribbling"], x["Marking"], x["Reactions"], x["Sliding_Tackle"], x["Standing_Tackle"], x["Vision"],x["Crossing"],
                 x["Short_Passing"], x["Long_Passing"], x["Acceleration"], x["Sprint_Speed"],x["Stamina"],x["Finishing"],x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/centreMidfielder')
def centreMidfielder():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Reactions", "Vision", "Positioning",
         "Crossing", "Short_Passing", "Long_Passing", "Curve", "Long_Shots", "FK_Accuracy", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  #drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    '''
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("centreMidfielder.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    '''
    # load file
    pickle_in = open("centreMidfielder.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    #calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 3 is  ", acc)

    #prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """
    width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")

    plt.title("Actual vs fitted value for centreMidfielder")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""


    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Ratings of the Center MidFielder:\n")

    # Finding the values that contain Position = "CM" and Position = "CAM" To get the Center MidFielders and Center Atacking Midfielders from the collection
    result = collection.find({"Position": "CM","Position": "CAM"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Ball_Control"], x["Dribbling"], x["Marking"], x["Reactions"], x["Vision"],x["Positioning"], x["Crossing"],
                 x["Short_Passing"], x["Long_Passing"], x["Curve"], x["Long_Shots"], x["FK_Accuracy"],x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/rightWingBack')
def rightWingBack():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking","Reactions", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing",
         "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  #drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    '''
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("rightWingBack.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    '''
    # load file
    pickle_in = open("rightWingBack.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    #calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 4 is  ", acc)

    #prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """
    width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")

    plt.title("Actual vs fitted value for rightWingBack")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Ratings of the Right Wing Back :\n")

    # Finding the values that contain Position = "RWB" To get the Right Wing Back from the collection
    result = collection.find({"Position": "RWB"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Ball_Control"], x["Dribbling"], x["Marking"],x["Reactions"], x["Sliding_Tackle"], x["Standing_Tackle"], x["Vision"],x["Crossing"],
                 x["Short_Passing"], x["Long_Passing"], x["Acceleration"], x["Sprint_Speed"], x["Stamina"],x["Finishing"], x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/rightWingAttacker')
def rightWingAttacker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Reactions","Sprint_Speed", "Acceleration", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Aggression", "Agility", "Curve", "Long_Shots",
         "FK_Accuracy","Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  #drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    '''
      #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("rightWingAttacker.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    '''
    # load file
    pickle_in = open("rightWingAttacker.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    #calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 5 is  ", acc)

    #prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """
    width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")

    plt.title("Actual vs fitted value for rightWingAttacker")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Ratings of Right Wing Attacker:\n")

    result = collection.find({"Position": "RW"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Weak_Foot"],x["Ball_Control"], x["Dribbling"],x["Reactions"], x["Sprint_Speed"], x["Acceleration"], x["Vision"],x["Crossing"],x["Short_Passing"],
                 x["Long_Passing"], x["Aggression"], x["Agility"], x["Curve"],x["Long_Shots"],x["FK_Accuracy"],x["Finishing"],x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        # updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})
        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating

    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    #Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/leftWingAttacker')
def leftWingAttacker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling","Reactions" ,"Sprint_Speed", "Acceleration", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Aggression", "Agility", "Curve", "Long_Shots",
         "FK_Accuracy", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  #drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    '''
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("leftWingAttacker.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    '''
    # load file
    pickle_in = open("leftWingAttacker.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    #calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 6 is  ", acc)

    #prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """
    width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")

    plt.title("Actual vs fitted value for leftWingAttacker")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Ratings of the Left Wing Attacker:\n")

    # Finding the values that contain Position = "LW" To get the Left Wing Attackers from the collection
    result = collection.find({"Position": "LW"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Weak_Foot"], x["Ball_Control"], x["Dribbling"], x["Reactions"],x["Sprint_Speed"], x["Acceleration"], x["Vision"],x["Crossing"], x["Short_Passing"],
                 x["Long_Passing"], x["Aggression"], x["Agility"], x["Curve"], x["Long_Shots"], x["FK_Accuracy"],x["Finishing"], x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/rightCentreMidfielder')
def rightCentreMidfielder():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Agility", "Balance", "Jumping", "Strength", "Stamina", "Sprint_Speed",
         "Acceleration", "Short_Passing", "Aggression", "Reactions", "Marking", "Standing_Tackle",
         "Sliding_Tackle", "Interceptions", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  # drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    '''
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("rightCentreMidfielder.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f) 
    '''
    # load file
    pickle_in = open("rightCentreMidfielder.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 7 is ", acc)

    # prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """
    width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")

    plt.title("Actual vs fitted value for rightCentreMidfielder")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Ratings of the Right Centre Midfielder:\n")

    # Finding the values that contain Position = "RCM" To get the Right Center Midfielder from the collection
    result = collection.find({"Position": "RCM"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Agility"], x["Balance"], x["Jumping"], x["Strength"], x["Stamina"], x["Sprint_Speed"],x["Acceleration"], x["Short_Passing"],
                 x["Aggression"], x["Reactions"], x["Marking"], x["Standing_Tackle"], x["Sliding_Tackle"], x["Interceptions"],x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/leftCentreMidfielder')
def leftCentreMidfielder():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Marking", "Reactions", "Vision",
         "Composure", "Short_Passing", "Long_Passing", "Reactions", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  # drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    '''
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("leftCentreMidfielder.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f)
    '''
    # load file
    pickle_in = open("leftCentreMidfielder.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 9 is  ", acc)

    # prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """
     width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")
    plt.title("Actual vs fitted value for leftCentreMidfielder")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Ratings of the Left Centre Midfielder:\n")

    # Finding the values that contain Position = "LCM" To get the Left Center Midfielder from the collection
    result = collection.find({"Position": "LCM"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Weak_Foot"], x["Ball_Control"], x["Dribbling"], x["Marking"], x["Reactions"], x["Vision"],
                 x["Composure"], x["Short_Passing"], x["Long_Passing"], x["Reactions"], x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/striker')
def striker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Reactions","Vision", "Aggression", "Agility", "Curve",
         "Long_Shots", "Balance", "Finishing", "Heading_Accuracy", "Jumping", "Dribbling", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  # drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    '''
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("striker.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f)
    '''
    # load file
    pickle_in = open("striker.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 10 is  ", acc)

    # prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """
    width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")
    plt.title("Actual vs fitted value for striker")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Ratings of the Strikers :\n")

    # Finding the values that contain Position = "ST" To get the Strikers from the collection
    result = collection.find({"Position": "ST"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Weak_Foot"], x["Ball_Control"],x["Reactions"], x["Vision"], x["Aggression"], x["Agility"], x["Curve"],x["Long_Shots"],
                 x["Balance"], x["Finishing"], x["Heading_Accuracy"], x["Jumping"], x["Dribbling"],x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/leftCenterDefender')
def leftCenterDefender():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Reactions", "Interceptions", "Sliding_Tackle", "Standing_Tackle", "Vision", "Composure",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Jumping",
         "Heading_Accuracy",
         "Long_Shots", "Aggression", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  # drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    '''
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("leftCenterDefender.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f)
    '''
    # load file
    pickle_in = open("leftCenterDefender.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module is 1 ", acc)

    # prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """
    width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")
    plt.title("Actual vs fitted value for leftCenterDefender")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Ratings of the Left Center Defenders:\n")

    # Finding the values that contain Position = "LCB" To get the Left Center Defenders from the collection
    result = collection.find({"Position": "LCB"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Reactions"], x["Interceptions"], x["Sliding_Tackle"], x["Standing_Tackle"], x["Vision"], x["Composure"],x["Crossing"],
                 x["Short_Passing"], x["Long_Passing"], x["Acceleration"], x["Sprint_Speed"], x["Stamina"], x["Jumping"],
                 x["Heading_Accuracy"], x["Long_Shots"], x["Aggression"], x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


@app.route('/rightCenterDefender')
def rightCenterDefender():
    data = pd.read_csv("FootballDataset.csv")
    data = data[["Overall", "Ball_Control", "Dribbling", "Marking", "Reactions","Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))  # drop overall to select other variables as dependent variables
    y = np.array(data[predict])  # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    '''
    #saving the model using pickle
    best = 0
    for _ in range(100):

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
        linear = linear_model.LinearRegression() #create the linear regression object
        linear.fit(x_train, y_train)    #find the best fit line
        acc = linear.score(x_test, y_test)
        print("The accuracy of the module1 is", acc)
        #check the best accuracy in the model
        if acc > best:
            best = acc
            print("The best acc", best)
            with open("rightCenterDefender.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f)
    '''
    # load file
    pickle_in = open("rightCenterDefender.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 11 is  ", acc)

    # prediction values of test data.
    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    # Plot the actual value vs model predict value
    """width = 6
    height = 5
    plt.figure(figsize=(width, height))
    sns.distplot(data['Overall'], hist=False, color="r", label="Actual Value")
    sns.distplot(predictions, hist=False, color="b", label="Fitted Value")
    plt.title("Actual vs fitted value for rightCenterDefender")
    plt.xlabel('Overall')
    plt.ylabel('Player attribute')
    plt.show()
    plt.close()"""

    # Printing Root Mean Squared Error of the Model
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    # print("The Test value:\n")
    # print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("The Rating of the Right Center Defenders:\n")

    # Finding the values that contain Position = "RCB" To get the Right Center Defenders from the collection
    result = collection.find({"Position": "RCB"})

    #create empty arrays to store names and ratings
    names = []
    ratings = []
    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Ball_Control"], x["Dribbling"], x["Marking"],x["Reactions"] ,x["Sliding_Tackle"], x["Standing_Tackle"],x["Vision"], x["Crossing"],
                 x["Short_Passing"], x["Long_Passing"], x["Acceleration"], x["Sprint_Speed"], x["Stamina"],x["Finishing"],x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        ratings.append(re)
        names.append(name)

    # Create new dictionary called newdict and assign name and new predicted rating
    newdict = dict(zip(names, ratings))

    # Printing the names and the rating of the player
    print("Name :   Rating   ")

    # Sorting acording to the rating
    array3 = sorted(newdict.items(), key=lambda x: x[1], reverse=True)

    tempArray = []

    # Printing the names and the ratings of each player in the console
    for i in array3:
        tempArray.append({'name': i[0], 'rating': i[1]})
        print(i)

    # returning the name of the players and their ratings
    return jsonify(tempArray)

    print("\n")


# Need to implement
# @app.route('/checkRating')
# def checkRating():
#     data=pd.read_csv('FootballDataset.csv')
#     #data.head()
#
#     #data=data[["Crossing", "Finishing", "HeadingAccuracy", "ShortPassing", "Volleys"]]
#     data=data[['Overall','Age','Crossing', 'Finishing', 'Heading_Accuracy', 'Short_Passing', 'Volleys',
#            'Dribbling', 'Curve', 'FK_Accuracy', 'Long_Passing', 'Ball_Control',
#            'Acceleration', 'Sprint_Speed', 'Agility', 'Reactions', 'Balance',
#            'Shot_Power', 'Jumping', 'Stamina', 'Strength', 'Long_Shots',
#            'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties',
#            'Composure', 'Marking', 'Standing_Tackle', 'Sliding_Tackle']]
#     # Drop the rows where at least one element is null:
#     data = data.dropna()
#     predict = "Overall"
#     X = np.array(data.drop([predict], 1))  # drop overall to select other variables as dependent variables
#     y = np.array(data[predict])  # select overall as independent variable
#
#     # Splitting data into test and train
#     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
#     """
#     #saving the model using pickle
#     best = 0
#     for _ in range(100):
#
#         x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
#         linear = linear_model.LinearRegression() #create the linear regression object
#         linear.fit(x_train, y_train)    #find the best fit line
#         acc = linear.score(x_test, y_test)
#         print("The accuracy of the module1 is", acc)
#         #check the best accuracy in the model
#         if acc > best:
#
#             best = acc
#             print("The best acc", acc)
#             with open("FootballPlayer3.pickle", "wb") as f: # save the model to pickle file
#                 pickle.dump(linear, f)"""
#
#     # load file
#     pickle_in = open("FootballPlayer3.pickle", "rb")
#     linear = pickle.load(pickle_in)
#
#     print("Coefficient:\n", linear.coef_)
#     print("Intercept:\n", linear.intercept_)
#
#     # calculating the accuracy of the model
#     acc = linear.score(x_test, y_test)
#     print("The accuracy of the module 12 is ", acc)
#
#     print("The Rating of the player is :\n")
#     print(linear.predict(np.array([[30.0,30.0,56.0,45.0,78.0,56.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0]]))[0])


# @app.route('/variable/<int:age>/<int:x>')
# def variable(age:int,x:int):
#     y = x+age
#
#     return y



if __name__ == '__main__':
    app.run()
