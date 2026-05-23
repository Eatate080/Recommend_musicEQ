#モジュールを沢山
from app.core.get_file_info import get_file_info ,test_file_info
from app.core.analyzer import AudioAnalyzer
from app.core.learn_model import learn_model
from app.database.repository import save_data,all_read_data
import joblib
import sys
import numpy as np


def main():
    
    while True:
        print("\n-- LoveAudio System --\n")
        print("1: 練習データを追加する(学習モード)\n")
        print("2: 新しい曲でEQを予測する(テストモード)\n")
        print("3: 学習モデルを作る\n")
        print("0: システムを終了する\n")  
        
        try:
            select_number = int(input("値(半角数字)を入力してください: "))
        except ValueError:
            print("エラー: 半角数字で入力してください。\n")
            continue  
        

        
        if select_number == 1:
            print("\n-- 学習モードに移行します --")
            print("練習に使う音楽ファイル名を入力してください\n")
            file_name = input("-> ")
            print(f"入力されたファイル: {file_name}")

            file_title,own_eq,file_path=get_file_info(file_name)
            features = AudioAnalyzer(file_path)[0]
            save_data(file_title,features,own_eq)
        
            print("\nこのまま学習させますか？")
            select_func = input("y/n : ")
            if select_func == "y":
                all_features,all_eq = all_read_data()
                learn_model(all_features,all_eq)
                break
            
            elif select_func == "n":
                print("\n学習をせずに終了します")
                break
            
            else:
                print("\n予期せぬ文字が入力されたため終了します")
                break



        elif select_number == 2:
            print("\n-- テストモードに移行します --\n")
            print("練習に使う音楽ファイル名を入力してください\n")
            file_name = input("-> ")
            print(f"入力されたファイル: {file_name}")

            file_path=test_file_info(file_name)
            test_features = AudioAnalyzer(file_path)


            loaded_model = joblib.load(rf".\model\learn-model.joblib")
            print("モデルを読み込みました")

            predictions = loaded_model.predict(test_features)
            final_features = np.rint(predictions).astype(int)
            print("予測結果: ",final_features)
            sys.exit()



        elif select_number == 3:
            print("学習モデルを生成します")
            all_features,all_eq = all_read_data()
            learn_model(all_features,all_eq)
            break


        elif select_number == 0:
            print("システムを終了します。")
            sys.exit()  
        else:
            print("1, 2, 0 のいずれかを入力してください。")
            continue
                


    return 0

if __name__ == "__main__":
    main()