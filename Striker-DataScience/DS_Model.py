import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import pickle

z = 0
def goalkeeper():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Reactions", "Composure", "Sprint_Speed", "Strength", "Jumping", "GK_Positioning", "GK_Diving",
         "GKReflexes", "GK_Handling", "GK_Kicking", "Vision", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1)) # drop overall to select other variables as dependent variables
    y = np.array(data[predict]) # select overall as independent variable

    # Splitting data into test and train
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    #linear = linear_model.LinearRegression()  # create the linear regression object

    #linear.fit(x_train, y_train)  # find the best fit line
    #acc = linear.score(x_test, y_test)

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
            print("The best accuracy", best)
            best = acc
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
    print("The accuracy of the module 1 is  ", acc)

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    #print("The Test value:\n")
    #print(linear.predict(np.array([[80.0, 30.0, 56.0, 45.0, 78.0, 56.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]]))[0])
    print("\n")


def leftWingBack():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Reactions", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best accuracy", best)
            best = acc
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    print("\n")




def centreMidfielder():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Reactions", "Vision", "Positioning",
         "Crossing", "Short_Passing", "Long_Passing", "Curve", "Long_Shots", "FK_Accuracy", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best accuracy", best)
            best = acc
            with open("centreMidfielder.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    """
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    print("\n")


def rightWingBack():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Reactions", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing",
         "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best accuracy", best)
            best = acc
            with open("rightWingBack.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    """
    # load file
    pickle_in = open("rightWingBack.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 4 is  ", acc)

    # prediction values of test data.
    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    print("\n")


def rightWingAttacker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Reactions", "Sprint_Speed", "Acceleration", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Aggression", "Agility", "Curve", "Long_Shots",
         "FK_Accuracy", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best acc", best)
            best = acc
            with open("rightWingAttacker.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    """
    # load file
    pickle_in = open("rightWingAttacker.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    #calculating the accuracy of the model
    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    print("\n")


def leftWingAttacker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Reactions", "Sprint_Speed", "Acceleration", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Aggression", "Agility", "Curve", "Long_Shots",
         "FK_Accuracy", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best accuracy", best)
            best = acc
            with open("leftWingAttacker.pickle", "wb") as f: # save the model to pickle file
                pickle.dump(linear, f)
    """
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
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
    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best accuracy", best)
            best = acc
            with open("rightCentreMidfielder.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f)
    """
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    print("\n")


def leftCentreMidfielder():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Marking", "Reactions", "Vision",
         "Composure", "Short_Passing", "Long_Passing", "Reactions", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best accuracy", best)
            best = acc
            with open("leftCentreMidfielder.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f)
    """
    # load file
    pickle_in = open("leftCentreMidfielder.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 8 is  ", acc)

    # prediction values of test data.

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    print("\n")


def striker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Reactions", "Vision", "Aggression", "Agility", "Curve",
         "Long_Shots", "Balance", "Finishing", "Heading_Accuracy", "Jumping", "Dribbling", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best accuracy", best)
            best = acc
            with open("striker.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f)
    """
    # load file
    pickle_in = open("striker.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 9 is  ", acc)

    # prediction values of test data.

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    print("\n")


def leftCenterDefender():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Reactions", "Interceptions", "Sliding_Tackle", "Standing_Tackle", "Vision", "Composure",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Jumping",
         "Heading_Accuracy","Long_Shots", "Aggression", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best accuracy", best)
            best = acc
            with open("leftCenterDefender.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f)
    """
    # load file
    pickle_in = open("leftCenterDefender.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    # calculating the accuracy of the model
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module is 10 ", acc)

    # prediction values of test data.
    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))
    print("\n")


def rightCenterDefender():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Reactions", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))#drop overall to select other variables as dependent variables
    y = np.array(data[predict])# select overall as independent variable

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
            print("The best accuracy", best)
            best = acc
            with open("rightCenterDefender.pickle", "wb") as f:  # save the model to pickle file
                pickle.dump(linear, f)
    """
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))

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
