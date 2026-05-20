from supabase import create_client, Client
from dotenv import load_dotenv
import os
def save_music_data():
    load_dotenv(r".env")

    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")


    try:
        
        supabase: Client = create_client(url, key)
        supabase.auth.sign_in_anonymously()
        
        
    except Exception as e:
        
        print(f"エラー{e}")
        
    try:
        data = {
    
            "music_name": "test_success",
            "features": [0.1, 0.2, 0.3],
            "my_eq": [1, 2, 3, 4, 5, 6]
        }
        supabase.table("music_data").insert(data).execute()

    except Exception as e:
        print(f"エラー{e}")
        print(f"エラーの種類: {type(e)}")

save_music_data()