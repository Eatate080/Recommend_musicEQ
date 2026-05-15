import os
import sqlite3 
import Data_Analysis

def Enter_practice_data(path,extension,name):
        musicfile_path = f"./music_data/{path}"
        try:
                print(f"ファイルパス確認{os.path.exists(musicfile_path)}")
                db_name = "Love_Audio.db"
                conn = sqlite3.connect(db_name)
                cur = conn.cursor()
                cur.execute(
                        'CREATE TABLE IF NOT EXISTS music_list(id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                        'music_name TEXT,' \
                        'music_extension TEXT,' \
                        'data BLOB)'
                )
                conn.commit()
                cur.execute('INSERT INTO music_list(music_name) values(?)', (name,))
                cur.execute('INSERT INTO music_list(music_extension) values(?)', (extension,))
                conn.commit()
                cur.close()
                conn.close()


                return path


        
        except Exception as e:
                print(f"予期しないエラーが発生しました: {e}")

                return 0