import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model

z=0
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

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print("\n")

def leftWingBack():
    football_data = pd.read_csv("FootballDataset.csv")
    data = football_data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Sliding_Tackle", "Standing_Tackle", "Vision",
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print("The accuracy of the module is", acc)
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

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print("The accuracy of the module is", acc)
    print("\n")


def rightWingBack():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Sliding_Tackle", "Standing_Tackle", "Vision",
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

    print("The accuracy of the module is", acc)
    print("\n")


def rightWingAttacker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Sprint_Speed", "Acceleration", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Aggression", "Agility", "Curve", "Long_Shots",
         "FK_Accuracy",
         "Finishing", "Age"]]

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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)
    
    print("\n")


def leftWingAttacker():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Sprint_Speed", "Acceleration", "Vision",
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)
    
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)
    
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)
    
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)
    print("\n")


def leftCenterDefender():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Reactions", "Interceptions", "Sliding_Tackle", "Standing_Tackle", "Vision", "Composure",
         "Crossing","Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Jumping", "Heading_Accuracy",
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module is", acc)
    print("\n")


def rightCenterDefender():
    data = pd.read_csv("FootballDataset.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Sliding_Tackle", "Standing_Tackle", "Vision",
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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
    print("The accuracy of the module3 is", acc)
    
    print("\n")


while True:
    print("Player positions","\n","1. Goal Keeper","\n","2. central Midfielder","\n","3. Left Wing Back","\n","4. Right Wing Back","\n","5. Right Wing Attacker",
          "\n","6. Left Wing Attacker","\n","7. Right Central Midfielder","\n","8. Left Central Midfielder","\n","9. Striker","\n","10. Left Central Defender","\n","11. Right Central Defender")
    try:
        player_Position=int(input("Enter the player position: "))
        
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
