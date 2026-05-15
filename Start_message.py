import Enter_data as Ed

def start_Sys():
    print("-- LoveAudio System --")
    print("1: 練習データを追加する(学習モード)")
    print("2: 新しい曲でEQを予測する(テストモード)") 

    select = int(input("値(半角数字)を入力してください: "))
    if (select == 1):
        print("-- 学習モードに移行します --")
        print("練習に使う音楽ファイル名を入力してください")
        file_name = input("->")
        print("練習に使う音楽ファイルの拡張子名を入力してください(例：flac)")
        file_extension = input("->")
        file_path = f"{file_name}.{file_extension}"
        print(file_path)

        Ed.Enter_practice_data(file_path,file_extension,file_name)
    elif (select == 2):
        print("テストモードに移行します")
        #Test_data()
    else :
        print("バカ野郎どんな値入れやがった。再入力しやがれ")
        start_Sys()
    return 0