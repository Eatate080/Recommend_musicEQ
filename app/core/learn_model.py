from sklearn.ensemble  import RandomForestRegressor as RFR
import joblib
import numpy as np
import pathlib 


def learn_model(result_features,result_myeq):
    

    #モデル作成
    model = RFR()


    model.fit(result_features,result_myeq)
    file_path: str = str(pathlib.Path("model") / "learn-model.joblib")
    joblib.dump(model,file_path)
    print("学習が完了し、モデルファイルが生成されました")

    return file_path


    