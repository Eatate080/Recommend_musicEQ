#モジュールを沢山
import Start_message
import joblib


def main():
    Start_message.start_Sys()

    loaded_model = joblib.load(rf".\model\learn-model.joblib")
    print("モデルを読み込みました")

    predictions = loaded_model.predict(new_data)
    #analyzer.pyから引っ張ってくる。(new_data)
    print("予測結果: ",predictions)

    return 0

#実行
main()


