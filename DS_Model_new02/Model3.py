import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

#sns.set_style('darkgrid')

football_data=pd.read_csv('ModifyDatasetFootballByme3.csv')

z=0
player_Position=1
# weights
a = 0.5
b = 1
c = 2
d = 3


def choosing_defenders():
    football_data['centre_backs'] = (d * football_data.Reactions + c * football_data.Interceptions + d * football_data.Sliding_Tackle + d * football_data.Standing_Tackle +
                                     b * football_data.Vision + b * football_data.Composure + b * football_data.Crossing + a * football_data.Short_Passing + b * football_data.Long_Passing +
                                     c * football_data.Acceleration + b * football_data.Sprint_Speed + d * football_data.Stamina + d * football_data.Jumping + d * football_data.Heading_Accuracy +
                                     b * football_data.Long_Shots + d * football_data.Marking + c * football_data.Aggression) / (1 * a + 6 * b + 3 * c + 7 * d)

    football_data['Wing_Backs'] = (b * football_data.Ball_Control + a * football_data.Dribbling + a * football_data.Marking + d * football_data.Sliding_Tackle + d * football_data.Standing_Tackle +
                                   c * football_data.Vision + c * football_data.Crossing + b * football_data.Short_Passing + c * football_data.Long_Passing + d * football_data.Acceleration +
                                   d * football_data.Sprint_Speed + c * football_data.Stamina + a * football_data.Finishing) / (3 * a + 2 * b + 4 * c + 4 * d)
while True:
    print("Player positions","\n","1. Goal Keeper","\n","2. Centre Back","\n","3. Wing Back","\n","4. Playmaker/Attacking Midfielder","\n","5. Right central mid filder",
          "\n","6. Left central mid filder","\n","7. Left Wing","\n","8. Right Wing","\n","9. Striker","\n","10. Left Central Deffender","\n","11. Right Central Defender")
    try:
        player_Position=int(input("Enter the player position: "))
        z=int(input("Enter the number of top players you want:"))
    except ValueError:
        print("Please enter integer value...")
        continue

    if 0<=z<=20:
        if 0<player_Position<2:
                # GoalKeeping Characteristics
                football_data['gk'] = (b * football_data.Reactions + b * football_data.Composure + a * football_data.Sprint_Speed + a * football_data.Strength + a * football_data.Short_Passing +
                                        a * football_data.Long_Passing + c * football_data.Jumping + b * football_data.GK_Positioning + c * football_data.GK_Diving + d * football_data.GKReflexes +
                                        b * football_data.GK_Handling+ d * football_data.GK_Kicking + c * football_data.Vision) / (4 * a + 4 * b + 3 * c + 2 * d)
                sd = football_data.sort_values('gk', ascending=False)[:z]
                print('Number of goal keepers: {0}'.format(football_data['gk'].nunique()))
                print("Top", z, " goal keepers:")
                x1 = np.array(list(sd['Name']))
                y1 = np.array(list(sd['gk']))
                print("\n".join(x1))
                print("Values of the ratings:")
                print(y1)
                print("\n")

        elif 1<player_Position <3:
            choosing_defenders()
            sd1 = football_data[(football_data['Position'] == 'LCB') | (football_data['Position'] == 'RCB')].sort_values('centre_backs', ascending=False)[:z]
            print('Number of Left Central Defenders: {0}'.format(football_data['centre_backs'].nunique()))
            print("Top", z, "Left Central Defenders:")
            x2 = np.array(list(sd1['Name']))
            y2 = np.array(list(sd1['centre_backs']))
            print("\n".join(x2))
            print("Values of the ratings:")
            print(y2)
            print("\n")

        elif 2<player_Position<4:
            choosing_defenders()
            sd2 = football_data[(football_data['Position'] == 'LWB') | (football_data['Position'] == 'RWB')].sort_values('Wing_Backs', ascending=False)[:z]
            print('Number of wing backs: {0}'.format(football_data['Wing_Backs'].nunique()))
            print("Top", z, "wing Backs:")
            x3 = np.array(list(sd2['Name']))
            y3 = np.array(list(sd2['Wing_Backs']))
            print("\n".join(x3))
            print("Values of the ratings:")
            print(y3)
            print("\n")

        elif 3<player_Position<5:
            # Midfielding Indices
            football_data['playmaker'] = (d * football_data.Ball_Control + d * football_data.Dribbling + a * football_data.Marking + d * football_data.Reactions + d * football_data.Vision +
                                          c * football_data.Crossing + d * football_data.Short_Passing + c * football_data.Long_Passing + c * football_data.Curve + b * football_data.Long_Shots +
                                          c * football_data.FK_Accuracy) / (1 * a + 1 * b + 4 * c + 5 * d)
            sd3 = football_data[(football_data['Position'] == 'CAM') | (football_data['Position'] == 'LAM') | (football_data['Position'] == 'RAM')].sort_values('playmaker', ascending=False)[:z]
            x4 = np.array(list(sd3['Name']))
            y4 = np.array(list(sd3['playmaker']))
            print('Number of playmakers: {0}'.format(football_data['playmaker'].nunique()))
            print("Top", z, "playmakers:")  # A playmaker is someone who will move the ball to the attacking 3rd from defence or midfield.
            print("\n".join(x4))
            print("Values of the ratings:")
            print(y4)
            print("\n")

        elif 4<player_Position<6:
            football_data['beast'] = (d * football_data.Agility + c * football_data.Balance + b * football_data.Jumping + c * football_data.Strength + d * football_data.Stamina +
                                      a * football_data.Sprint_Speed + c * football_data.Acceleration + d * football_data.Short_Passing + c * football_data.Aggression + d * football_data.Reactions +
                                      b * football_data.Marking + b * football_data.Standing_Tackle + b * football_data.Sliding_Tackle + b * football_data.Interceptions) / (
                                      1 * a + 5 * b + 4 * c + 4 * d)

            sd4 = football_data[(football_data['Position'] == 'RCM') | (football_data['Position'] == 'RM')].sort_values('beast', ascending=False)[:z]
            x5 = np.array(list(sd4['Name']))
            y5 = np.array(list(sd4['beast']))  # A beast is a typical box-to-box player with loads of energy and who can boss the midfield.
            print('Number of Right central mid fielders: {0}'.format(football_data['beast'].nunique()))
            print("Top", z, "Right central mid fielders:")
            print("\n".join(x5))
            print("Values of the ratings:")
            print(y5)
            print("\n")

        elif 5<player_Position <7:
            football_data['controller'] = (b * football_data.Weak_Foot + d * football_data.Ball_Control + a * football_data.Dribbling + a * football_data.Marking +
                                           a * football_data.Reactions +c * football_data.Vision + c * football_data.Composure + d * football_data.Short_Passing +
                                           d * football_data.Long_Passing) / (2 * c + 3 * d + 3 * a + b)

            sd5 = football_data[(football_data['Position'] == 'LCM') | (football_data['Position'] == 'LM')].sort_values('controller', ascending=False)[:z]
            x6 = np.array(list(sd5['Name']))
            y6 = np.array(list(sd5['controller']))      #A controller is the person who is orchestrating your midfield engine by either sitting back or going forward based on dynamic needs.
            print('Number of Left Central Midfielders: {0}'.format(football_data['controller'].nunique()))
            print("Top", z, "Left Central Midfielders:")
            print("\n".join(x6))
            print("Values of the ratings:")
            print(y6)
            print("\n")

        elif 6<player_Position<8:
            # Attackers
            football_data['left_wing'] = (c * football_data.Weak_Foot + c * football_data.Ball_Control + c * football_data.Dribbling + c * football_data.Sprint_Speed + d * football_data.Acceleration +
                                          b * football_data.Vision + c * football_data.Crossing + b * football_data.Short_Passing + b * football_data.Long_Passing + b * football_data.Aggression +
                                          b * football_data.Agility + a * football_data.Curve + c * football_data.Long_Shots + b * football_data.FK_Accuracy + d * football_data.Finishing) / (
                                          a + 6 * b + 6 * c + 2 * d)

            sd6 = football_data[(football_data['Position'] == 'LW') | (football_data['Position'] == 'LM') | (football_data['Position'] == 'LS')].sort_values('left_wing', ascending=False)[:z]
            x7 = np.array(list(sd6['Name']))
            y7 = np.array(list(sd6['left_wing']))
            print('Number of Left wing players: {0}'.format(football_data['left_wing'].nunique()))
            print("Top", z, "Left wing players:")
            print("\n".join(x7))
            print("Values of the ratings:")
            print(y7)
            print("\n")

        elif 7<player_Position <9:
            football_data['right_wing'] = (c * football_data.Weak_Foot + c * football_data.Ball_Control + c * football_data.Dribbling + c * football_data.Sprint_Speed + d * football_data.Acceleration +
                                           b * football_data.Vision + c * football_data.Crossing + b * football_data.Short_Passing + b * football_data.Long_Passing + b * football_data.Aggression +
                                           b * football_data.Agility + a * football_data.Curve + c * football_data.Long_Shots + b * football_data.FK_Accuracy + d * football_data.Finishing) / (
                                           a + 6 * b + 6 * c + 2 * d)
            sd7 = football_data[(football_data['Position'] == 'RW') | (football_data['Position'] == 'RM') | (football_data['Position'] == 'RF')].sort_values('right_wing', ascending=False)[:z]
            x8 = np.array(list(sd7['Name']))
            y8 = np.array(list(sd7['right_wing']))
            print('Number of right wing players: {0}'.format(football_data['right_wing'].nunique()))
            print("Top", z, "right wing players:")
            print("\n".join(x8))
            print("Values of the ratings:")
            print(y8)
            print("\n")

        elif 8<player_Position<10:
            football_data['striker'] = (b * football_data.Weak_Foot + b * football_data.Ball_Control + a * football_data.Vision + b * football_data.Aggression + b * football_data.Agility +
                                        a * football_data.Curve + a * football_data.Long_Shots + d * football_data.Balance + d * football_data.Finishing + d * football_data.Heading_Accuracy +
                                        c * football_data.Jumping + c * football_data.Dribbling) / (3 * a + 4 * b + 2 * c + 3 * d)

            sd8 = football_data[(football_data['Position'] == 'ST') | (football_data['Position'] == 'LS') | (football_data['Position'] == 'RS') | (football_data['Position'] == 'CF')].sort_values('striker',ascending=False)[:z]
            x9 = np.array(list(sd8['Name']))
            y9 = np.array(list(sd8['striker']))
            print('Number of Strikers: {0}'.format(football_data['striker'].nunique()))
            print("Top", z, "Strikers:")
            print("\n".join(x9))
            print("Values of the ratings:")
            print(y9)
            print("\n")

        elif 9<player_Position<11:
            choosing_defenders()
            sd9 = football_data[(football_data['Position'] == 'LCB')].sort_values('centre_backs', ascending=False)[:z]
            print('Number of Left Central Defenders: {0}'.format(football_data['centre_backs'].nunique()))
            print("Top", z, "Left Central Defenders:")
            x10 = np.array(list(sd9['Name']))
            y10 = np.array(list(sd9['centre_backs']))
            print("\n".join(x10))
            print("Values of the ratings:")
            print(y10)
            print("\n")

        elif 10<player_Position<12:
            choosing_defenders()
            sd10 = football_data[(football_data['Position'] == 'RCB')].sort_values('centre_backs', ascending=False)[:z]
            print('Number of Right Central Defenders: {0}'.format(football_data['centre_backs'].nunique()))
            print("Top", z, "Right Central Defenders:")
            x11 = np.array(list(sd10['Name']))
            y11 = np.array(list(sd10['centre_backs']))
            print("\n".join(x11))
            print("Values of the ratings:")
            print(y11)
            print("\n")
    else:
        print("You can select only 20 players")
    break
#Player with maximum Potential and Overall Performance
print('Player with Maximum Potential : '+str(football_data.loc[football_data['Potential'].idxmax()][2]))

print('Player with Maximum Overall Perforamnce : '+str(football_data.loc[football_data['Overall'].idxmax()][2]))
print("\n")
"""
pr_cols=['Crossing', 'Finishing', 'Heading_Accuracy', 'Short_Passing', 'Volleys',
       'Dribbling', 'Curve', 'FK_Accuracy', 'Long_Passing', 'Ball_Control',
       'Acceleration', 'Sprint_Speed', 'Agility', 'Reactions', 'Balance',
       'Shot_Power', 'Jumping', 'Stamina', 'Strength', 'Long_Shots',
       'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties',
       'Composure', 'Marking', 'Standing_Tackle', 'Sliding_Tackle', 'GK_Diving',
       'GK_Handling', 'GK_Kicking', 'GK_Positioning', 'GKReflexes']
i=0
while i < len(pr_cols):
    print('Best player in {0} : {1}'.format(pr_cols[i],football_data.loc[football_data[pr_cols[i]].idxmax()][2]))
    i += 1
print("\n")
"""
#Cleaning some of values so that we can interpret them
def value_to_int(df_value):
    try:
        value = float(df_value[1:-1])
        suffix = df_value[-1:]

        if suffix == 'M':
            value = value * 1000000
        elif suffix == 'K':
            value = value * 1000
    except ValueError:
        value = 0
    return value

football_data['Value'] = football_data['Value'].apply(value_to_int)
football_data['Wage'] = football_data['Wage'].apply(value_to_int)

#Top earners
print('Most valued player : '+str(football_data.loc[football_data['Value'].idxmax()][2]))
print('Highest earner : '+str(football_data.loc[football_data['Wage'].idxmax()][2]))
print("\n")

#Number of countries available and top 5 countries with highest number of players
print('Total number of countries : {0}'.format(football_data['Nationality'].nunique()))
print(football_data['Nationality'].value_counts().head(5))

#DROP UNNECESSARY VALUES
drop_cols = football_data.columns[28:54]
football_data = football_data.drop(drop_cols, axis = 1)
#df.drop(['Unnamed: 0','Photo','Flag','Club_Logo','Loaned_From'],axis=1,inplace=True)
football_data = football_data.drop(['Unnamed: 0','ID','Photo','Flag','Club_Logo','Jersey_Number','Joined','Special','Loaned_From','Body_Type', 'Release_Clause',
               'Weight','Height','Contract_Valid_Until','Wage','Value','Name','Club'], axis = 1)
football_data = football_data.dropna()

# Turn Real Face into a binary indicator variable
def face_to_num(football_data):
    if football_data['Real_Face'] == 'Yes':
        return 1
    else:
        return 0


# Turn Preferred Foot into a binary indicator variable
def right_footed(football_data):
    if (football_data['Preferred_Foot'] == 'Right'):
        return 1
    else:
        return 0


# Create a simplified position varaible to account for all player positions
def simple_position(football_data):
    if (football_data['Position'] == 'GK'):
        return 'GK' #GK = Goal keeper

    elif ((football_data['Position'] == 'RB') | (football_data['Position'] == 'LB') | (football_data['Position'] == 'CB') | (football_data['Position'] == 'LCB') | (
            football_data['Position'] == 'RCB') | (football_data['Position'] == 'RWB') | (football_data['Position'] == 'LWB')):
        return 'DF' #DF = Deffenders

    elif ((football_data['Position'] == 'LDM') | (football_data['Position'] == 'CDM') | (football_data['Position'] == 'RDM')):
        return 'DM' #DM = Defensive midfielder

    elif ((football_data['Position'] == 'LM') | (football_data['Position'] == 'LCM') | (football_data['Position'] == 'CM') | (
            football_data['Position'] == 'RCM') | (football_data['Position'] == 'RM')):
        return 'MF' #MF = MidFeilder

    elif ((football_data['Position'] == 'LAM') | (football_data['Position'] == 'CAM') | (football_data['Position'] == 'RAM') | (
            football_data['Position'] == 'LW') | (football_data['Position'] == 'RW')):
        return 'AM' #AM = Attacking MidFeilder

    elif ((football_data['Position'] == 'RS') | (football_data['Position'] == 'ST') | (football_data['Position'] == 'LS') | (football_data['Position'] == 'CF') | (
            football_data['Position'] == 'LF') | (football_data['Position'] == 'RF')):
        return 'ST' #ST= Striker

    else:
        return football_data.Position


# Get a count of Nationalities in the Dataset, make of list of those with over 250 Players (our Major Nations)
nat_counts = football_data.Nationality.value_counts()
nat_list = nat_counts[nat_counts > 250].index.tolist()


# Replace Nationality with a binary indicator variable for 'Major Nation'
def major_nation(football_data):
    if (football_data.Nationality in nat_list):
        return 1
    else:
        return 0

# Create a copy of the original dataframe to avoid indexing errors
df1 = football_data.copy()

# Apply changes to dataset to create new column
df1['Real_Face'] = df1.apply(face_to_num, axis=1)
df1['Right_Foot'] = df1.apply(right_footed, axis=1)
df1['Simple_Position'] = df1.apply(simple_position, axis=1)
df1['Major_Nation'] = df1.apply(major_nation, axis=1)

# Split the Work Rate Column in two
tempwork = df1["Work_Rate"].str.split("/ ", n=1, expand=True)
# Create new column for first work rate
df1["WorkRate1"] = tempwork[0]
# Create new column for second work rate
df1["WorkRate2"] = tempwork[1]
# Drop original columns used
df1 = df1.drop(['Work_Rate', 'Preferred_Foot', 'Real_Face', 'Position', 'Nationality'], axis=1)

#Split ID as a Target value
target = df1.Overall
df2 = df1.drop(['Overall'], axis = 1)

#Splitting into test and train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df2, target, test_size=0.2)

#One Hot Encoding
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)
print(X_test.shape,X_train.shape)
print(y_test.shape,y_train.shape)


#Applying Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)


#Finding the r2 score and root mean squared error
from sklearn.metrics import r2_score, mean_squared_error
print('Accuracy: '+str(r2_score(y_test, predictions)))
print('Mean Squared error : '+str(np.sqrt(mean_squared_error(y_test, predictions))))

#Visualising the results
plt.figure(figsize=(18,10))
sns.regplot(predictions,y_test,scatter_kws={'alpha':0.3,'color':'blue'},line_kws={'color':'red','alpha':0.5})
plt.xlabel('Predictions')
plt.ylabel('Overall')
plt.title("Linear Prediction of Player Rating")
plt.show()
