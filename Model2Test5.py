import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.model_selection import cross_val_score

data=pd.read_csv('C:/Users/Sanuri/Desktop/DataScience/FootballData.csv')

data=data[['Overall','Age','Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys',
       'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl',
       'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance',
       'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots',
       'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties',
       'Composure', 'Marking', 'StandingTackle', 'SlidingTackle']]
#data.head()

#Drop the rows where at least one element is missing:
data = data.dropna()

predict="Overall"

X=np.array(data.drop([predict],1))
y=np.array(data[predict])

x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(X,y,test_size=0.2,random_state=1)
linear=linear_model.LinearRegression()

linear.fit(x_train,y_train)
acc=linear.score(x_test,y_test)
print("The accuracy of the module is ",acc)

Rcross=cross_val_score(linear,X,y,cv=4)
print(Rcross)

print("Coefficient:\n",linear.coef_)
print("Intercept:\n",linear.intercept_)

predictions=linear.predict(x_test)

for i in range(len(predictions)):
    print(predictions[i],x_test[i],y_test[i])

print("The Test value:\n")
print(linear.predict(np.array([[30.0,30.0,56.0,45.0,78.0,56.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0,50.0]]))[0])

#print(x_test.shape,x_train.shape)


