import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class MS:
    def __init__(self, diab, liver, health, gender, age, height, weight, waist):
        self.diab = diab
        self.liver = liver
        self.health = health
        self.score = -1
        self.gender = 1 if gender == '남' else 2
        self.age = (age/5) + 1
        self.height = height
        self.weight = weight
        self.waist = waist

    def get_score(self):
        if (self.diab == 'off' and self.liver == 'off' and self.health == 'off'):
            self.score = 0
        elif (self.diab != 'off' and self.liver == 'off' and self.health == 'off'):
            self.score = 1
        elif (self.diab == 'off' and self.liver != 'off' and self.health == 'off'):
            self.score = 2
        elif (self.diab == 'off' and self.liver == 'off' and self.health != 'off'):
            self.score = 3
        elif (self.diab != 'off' and self.liver != 'off' and self.health == 'off'):
            self.score = 4
        elif (self.diab == 'off' and self.liver != 'off' and self.health != 'off'):
            self.score = 5
        elif (self.diab != 'off' and self.liver == 'off' and self.health != 'off'):
            self.score = 6
        else:
            self.score = 7

def return_state(MS, score):
    df_mh = pd.read_csv('./static/Health_data_cancer.csv')
    df_mh_y = df_mh['암진단결과']
    df_mh_x = df_mh.drop(['Unnamed: 0', '암진단결과'], axis=1)

    rf = RandomForestClassifier(random_state=1234)
    rf.fit(df_mh_x, df_mh_y)
    print(MS.score)

    df_real = pd.DataFrame(data=[[MS.score, MS.gender, MS.age, MS.height, MS.weight, MS.waist]],
                           columns=df_mh_x.columns)
    test = rf.predict(df_real)
    if (test == 'B'):
        return -1
    if(score == 0):
        return 0
    elif (score == 1):
        return 0.537
    elif (score == 2):
        return 0.545
    elif (score == 3):
        return 0.683
    elif (score == 4):
        return 0.742
    elif (score == 5):
        return 0.852
    elif (score == 6):
        return 0.800
    else:
        return 0.920

def return_diagnosis(score):
    if (score == 0):
        return ['']
    elif (score == 1):
        return ['당뇨 개선', '내용']
    elif (score == 2):
        return ['간질환 개선', '내용']
    elif (score == 3):
        return ['']
    elif (score == 4):
        return 0.742
    elif (score == 5):
        return 0.852
    elif (score == 6):
        return 0.800
    else:
        return 0.920