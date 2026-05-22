from sklearn.ensemble  import RandomForestRegressor as RFR
import joblib
import numpy as np


def learn_model(result_features,result_myeq):
    

    #モデル作成
    model = RFR()


    model.fit(result_features,result_myeq)
    joblib.dump(model,"learn-model.joblib")
    print("学習が完了し、モデルファイルが生成されました")

    return 0


    