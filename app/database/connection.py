#データベースへアクセスするモジュール(アクセスのみなため閉じない)

from supabase import create_client, Client
from dotenv import load_dotenv
import os

def connection_server():
    load_dotenv(r"C:\Users\eitom\Documents\love_audio\.env")
    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")


    try:
        
        supabase: Client = create_client(url, key)
        supabase.auth.sign_in_anonymously()
        print("接続成功！！")
        
        
    except Exception as e:
        
        print(f"エラー{e}")
        print(f"エラーの種類：{type(e)}")

    return 0

connection_server()