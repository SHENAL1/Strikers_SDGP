import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


def goalkeeper():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data=data[["Overall","Reactions", "Composure", "Sprint_Speed", "Strength", "Jumping","GK_Positioning","GK_Diving",
               "GKReflexes","GK_Handling","GK_Kicking","Vision","Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module1 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)



    predictions = linear.predict(x_test)
    #accuracy of the model
    print('r2 score: ' + str(r2_score(y_test, predictions)))
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))

    #for i in range(len(predictions)):
       # print(predictions[i], x_test[i], y_test[i])

def leftCenterDefender():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data = data[
        ["Overall", "Reactions", "Interceptions", "Sliding_Tackle", "Standing_Tackle", "Vision", "Composure", "Crossing",
         "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina","Jumping","Heading_Accuracy","Long_Shots","Aggression","Reactions","Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module2 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)
    print('r2 score: ' + str(r2_score(y_test, predictions)))
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))


#for i in range(len(predictions)):
       # print(predictions[i], x_test[i], y_test[i])


def rightCenterDefender():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing","Reactions", "Age"]]


    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module3 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)


    predictions = linear.predict(x_test)
    print('r2 score: ' + str(r2_score(y_test, predictions)))
    print('RMSE : ' + str(np.sqrt(mean_squared_error(y_test, predictions))))

    #for i in range(len(predictions)):
        #print(predictions[i], x_test[i], y_test[i])

def leftWingBack():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing","Reactions", "Age"]]

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

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

def rightWingBack():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data = data[
        ["Overall", "Ball_Control", "Dribbling", "Marking", "Sliding_Tackle", "Standing_Tackle", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Acceleration", "Sprint_Speed", "Stamina", "Finishing","Reactions", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 5 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

def centreMidfielder():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
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
    print("The accuracy of the module 6 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

def rightCentreMidfielder():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data = data[
        ["Overall", "Agility", "Balance", "Jumping", "Strength", "Stamina", "Sprint_Speed",
         "Acceleration", "Short_Passing", "Aggression", "Reactions", "Marking", "Standing_Tackle","Sliding_Tackle","Interceptions", "Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 7 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

def leftCentreMidfielder():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Marking", "Reactions", "Vision",
         "Composure", "Short_Passing", "Long_Passing", "Reactions","Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 8 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

def leftWingAttacker():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Sprint_Speed", "Acceleration", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Aggression", "Agility","Curve","Long_Shots","FK_Accuracy","Finishing","Reactions","Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 9 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

def rightWingAttacker():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Dribbling", "Sprint_Speed", "Acceleration", "Vision",
         "Crossing", "Short_Passing", "Long_Passing", "Aggression", "Agility", "Curve", "Long_Shots", "FK_Accuracy",
         "Finishing","Reactions","Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 10 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])

def striker():
    data = pd.read_csv("C:/Users/Sanuri/Desktop/JupiterNoteBook/ModifyDatasetFootballByme3.csv")
    data = data[
        ["Overall", "Weak_Foot", "Ball_Control", "Vision", "Aggression", "Agility", "Curve",
         "Long_Shots", "Balance", "Finishing", "Heading_Accuracy", "Jumping", "Dribbling", "Reactions","Age"]]

    # Drop the rows where at least one element is missing:
    data = data.dropna()
    predict = "Overall"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("The accuracy of the module 11 is", acc)

    print("Coefficient:\n", linear.coef_)
    print("Intercept:\n", linear.intercept_)

    predictions = linear.predict(x_test)

    for i in range(len(predictions)):
        print(predictions[i], x_test[i], y_test[i])
        
#goalkeeper()
leftCenterDefender()
#rightCenterDefender()
#leftWingBack()
#rightWingBack()
#centreMidfielder()
#rightCentreMidfielder()
#leftCentreMidfielder()
#leftWingAttacker()
#rightWingAttacker()
#striker()
