import os
import sys

def get_file_info(file_name) :
    
    print("ファイル情報を取得します")
    
    
    file_path: str = fr"...\data\{file_name}"
    print(file_path)
    
    try:
        root, ext = os.path.splitext(file_path)
        if ext == ".flac": #本番環境では.mp3に変更、学習時はOK

            eq_data =Enter_EQ()

            return root,eq_data,file_path
            
        else :
            print("拡張子がmp3じゃないです")
            sys.exit()


    except FileExistsError as e :
        print(f"ファイル名が間違えています(Not finf file_title){e}\n")
        print(f"Error Type:{e}\n")
        sys.exit()




def Enter_EQ():
    while True:
        try:
            eq_data: list[int]  = [int(x.strip()) for x in input("EQ設定(6周波数帯)を教えてください(値ごとにカンマで区切ってください:").split(",")]
            if not all(-10 <= val <=10 for val in eq_data):
                print("全ての要素数を-10~10の間で設定する必要があります")
                continue

            if len(eq_data) != 6:
                print("EQの要素数を6つにする必要があります")
                continue

            print(f"EQ設定はこちらでよろしいでしょうか->{eq_data}")
            confirm: str = input("y/n:->")

            if confirm == "y":
                return eq_data

            else :
                print("EQ入力からやり直してください")
                continue
        except ValueError:
            print("入力エラーです(数値以外のものは入力しないでください)")
            continue
            


get_file_info("kuronuri.flac")