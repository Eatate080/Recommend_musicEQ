#データベース上の保存、読み取り機能の実装(supabase_connection.pyから取ってくるだけで保存は行ける)
from app.moduls.schema import MusicData
from app.database.connection import connection_server

Client= connection_server()


def save_data(file_title: str,features:list[float],my_eq:list[int]):

    m_name = file_title
    extracted_features = features
    setting_eq = my_eq
    try:
        data: MusicData = {
            "music_name": m_name,
            "features": extracted_features,
            "my_eq": setting_eq
        }
        Client.table("music_data").insert(data).execute()
        print("書き込みが完了しました")

    except Exception as e:
        print(f"エラー{e}")
        print(f"エラーの種類: {type(e)}")

    return 0
    
def all_read_data():
    
    try:
        response = Client.table("music_data").select("features").execute()
        all_features = [row["features"] for row in response.data]
        print(all_features)
        return all_features
    except Exception as e:
        print(f"エラー{e}")
        print(f"エラーの種類: {type(e)}")
        return None
    
all_read_data()