
import sys
from pathlib import Path

def get_file_info(file_name) :
    
    print("ファイル情報を取得します")
    
    
    current_dir = Path(__file__).parent.parent.parent 
    file_path: str = str(current_dir / "data" / file_name)
    print(file_path)
    
    try:
        root = Path(file_path).stem
        ext = Path(file_path).suffix
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
            


