import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model

from pymongo import MongoClient
from pprint import pprint


#Getting theonnection from Mongo Db Atlas using MongoClient
cluster = MongoClient("mongodb+srv://admin:admin@striker-spfii.mongodb.net/test?retryWrites=true&w=majority")
#Acessing the Databse
db = cluster.get_database("PlayerDetails")
#acessing the collection
collection = db.get_collection("storedplayerdetails")

# #Counting all the documents(records) in the collection
# count = collection.count_documents({})
# print(count)


z = 0

def goalkeeper():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Reactions", "Composure", "Sprint_Speed", "Strength", "Jumping", "GK_Positioning", "GK_Diving",
         "GKReflexes", "GK_Handling", "GK_Kicking", "Vision", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module is 1 ", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    print("The Ratings of the Goal Keepers :\n")
    # val = 80.0;
    # val2 = 30.0;

    #Finding the values that contain Position = "GK" To get the goal keepers from the collection
    result = collection.find({"Position": "GK"})


    #Looping the result array to data2 array
    for x in result:
        data2 = [x["Reactions"], x["Composure"], x["Sprint_Speed"], x["Strength"], x["Jumping"],x["GK_Positioning"],
                 x["GK_Diving"], x["GKReflexes"], x["GK_Handling"], x["GK_Kicking"], x["Vision"], x["Age"]]

        #Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        #Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        # Printing the names and the rating of the player
        print("name :  ",name ,"                     rating :  ",re)

        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    # print(linear.predict(np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("\n")


def leftWingBack():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking","Reactions", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 4 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    print("The Ratings of the Left Wing Back:\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "LWB" To get the Left Wing Back from the collection
    result = collection.find({"Position": "LWB"})

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

        #Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        #Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict(np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 90.0, 34.0]]))[0])
    print("\n")




def centreMidfielder():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Reactions", "Vision", "Positioning",
         "Crossing", "Short_Passing", "Long_Passing", "Curve", "Long_Shots", "FK_Accuracy", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    print("The accuracy of the module is", acc)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    print("The Ratings of the Center MidFielder:\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "CM" To get the Center MidFielders from the collection
    result = collection.find({"Position": "CM"})

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

        # Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        # Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict(np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0,23.0]]))[0])

    print("\n")


def rightWingBack():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking","Reactions", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing",
         "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)

    print("The Ratings of the Right Wing Back :\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "RWB" To get the Right Wing Back from the collection
    result = collection.find({"Position": "RWB"})

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

        # Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        # Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict(np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0,80.0,78.04]]))[0])

    print("\n")


def rightWingAttacker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Reactions","Sprint_Speed", "Acceleration", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Aggression", "Agility", "Curve", "Long_Shots",
         "FK_Accuracy","Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)

    print("The Ratings of Right Wing Attacker:\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "RW" To get the Right Wing Attackers from the collection
    result = collection.find({"Position": "RW"})

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

        # Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        # Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict(np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0,90.0,34.0,90.0,45.0]]))[0])

    print("\n")


def leftWingAttacker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling","Reactions" ,"Sprint_Speed", "Acceleration", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Aggression", "Agility", "Curve", "Long_Shots",
         "FK_Accuracy", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    print("The accuracy of the module is", acc)
    print("The Ratings of the Left Wing Attacker:\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "LW" To get the Left Wing Attackers from the collection
    result = collection.find({"Position": "LW"})

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

        # Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        # Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict(np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0,90.0,34.0,90.0,45.0]]))[0])

    print("\n")


def rightCentreMidfielder():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Agility", "Balance", "Jumping", "Strength", "Stamina", "Sprint_Speed",
         "Acceleration", "Short_Passing", "Aggression", "Reactions", "Marking", "Standing_Tackle",
         "Sliding_Tackle", "Interceptions", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"
    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])

    print("The accuracy of the module is", acc)
    print("The Ratings of the Right Centre Midfielder:\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "RCM" To get the Right Center Midfielder from the collection
    result = collection.find({"Position": "RCM"})

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

        # Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        # Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict( np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0,50.0,90.0,34.0,90.0]]))[0])

    print("\n")


def leftCentreMidfielder():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Marking", "Reactions", "Vision",
         "Composure", "Short_Passing", "Long_Passing", "Reactions", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)

    print("The Ratings of the Left Centre Midfielder:\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "LCM" To get the Left Center Midfielder from the collection
    result = collection.find({"Position": "LCM"})

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

        # Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        # Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict( np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])

    print("\n")


def striker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Vision", "Aggression", "Agility", "Curve",
         "Long_Shots", "Balance", "Finishing", "Heading_Accuracy", "Jumping", "Dribbling", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)

    print("The Ratings of the Strikers :\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "ST" To get the Strikers from the collection
    result = collection.find({"Position": "ST"})

    # Looping the result array to data2 array
    for x in result:
        data2 = [x["Weak_Foot"], x["Ball_Control"], x["Vision"], x["Aggression"], x["Agility"], x["Curve"],x["Long_Shots"],
                 x["Balance"], x["Finishing"], x["Heading_Accuracy"], x["Jumping"], x["Dribbling"],x["Age"]]

        # Getting the short name of the player
        name = x["Short_name"]

        # Getting the object id of the collection of each player
        id = x["_id"]

        # Passing the data2 array to the pridiction
        re = linear.predict(np.array([data2]))[0]

        # Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        # Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict(np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 90.0,]]))[0])

    print("\n")


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

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)

    print("The Ratings of the Left Center Defenders:\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "LCB" To get the Left Center Defenders from the collection
    result = collection.find({"Position": "LCB"})

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

        # Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        # Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict(np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 90.0, 34.0,45.0,56.0,78.0]]))[0])

    print("\n")


def rightCenterDefender():
    data = pd.read_csv("FootballDataset.csv")
    data = data[["Overall", "Ball_Control", "Dribbling", "Marking", "Reactions","Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    # for i in range(len(predictions)):
    #     print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module3 is", acc)

    print("The Rating of the Right Center Defenders:\n")
    # val = 80.0;
    # val2 = 30.0;

    # Finding the values that contain Position = "RCB" To get the Right Center Defenders from the collection
    result = collection.find({"Position": "RCB"})

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

        # Printing the names and the rating of the player
        print("name :  ", name, "                     rating :  ", re)

        # Updating  the ratings of each player acordingly
        updateratings = collection.update_one({"_id": id}, {"$set": {"Ratings": re}})

    #print(linear.predict(np.array([[val, val2, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 90.0, 34.0]]))[0])

    print("\n")


while True:
    print("Player positions", "\n", "1. Goal Keeper", "\n", "2. central Midfielder", "\n", "3. Left Wing Back", "\n",
          "4. Right Wing Back", "\n", "5. Right Wing Attacker",
          "\n", "6. Left Wing Attacker", "\n", "7. Right Central Midfielder", "\n", "8. Left Central Midfielder", "\n",
          "9. Striker", "\n", "10. Left Central Defender", "\n", "11. Right Central Defender")
    try:
        player_Position = int(input("Enter the player position: "))

    except ValueError:
        print("Please enter integer value...")
        continue
    if 0 <= player_Position <= 11:
        if player_Position == 1:
            goalkeeper()
        elif player_Position == 2:
            centreMidfielder()

        elif player_Position == 3:
            leftWingBack()

        elif player_Position == 4:
            rightWingBack()

        elif player_Position == 5:
            rightWingAttacker()

        elif player_Position == 6:
            leftWingAttacker()

        elif player_Position == 7:
            rightCentreMidfielder()

        elif player_Position == 8:
            leftCentreMidfielder()

        elif player_Position == 9:
            striker()

        elif player_Position == 10:
            leftCenterDefender()

        elif player_Position == 11:
            rightCenterDefender()
    else:
        print("Please enter valid position")
