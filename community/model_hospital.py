import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

class MH :
    def __init__(self, age, weight, waist, AST, GTP, TGS, HDL, hemo):
        self.age = age
        self.weight = weight
        self.waist = waist
        self.AST = AST
        self.GTP = GTP
        self.TGS = TGS
        self.HDL = HDL
        self.hemo = hemo

    def setBMI(self, weight, height):
        self.BMI = weight / ((height/100.0)**2)

def runModel(MH):
    df_mh = pd.read_csv('./static/Health_data_mh.csv')
    df_mh_y = df_mh['(혈청지오티)ALT']
    df_mh_x = df_mh.drop(['Unnamed: 0', '(혈청지오티)ALT'], axis=1)

    gb = GradientBoostingRegressor(criterion="mse", random_state=1234)
    gb.fit(df_mh_x, df_mh_y)
    df_real = pd.DataFrame(data=[[MH.AST, MH.GTP, MH.weight, MH.age, MH.BMI, MH.HDL, MH.hemo, MH.TGS]], columns=df_mh_x.columns)
    ALT = gb.predict(df_real)
    result = ((ALT-40) / ALT) * 100
    return result