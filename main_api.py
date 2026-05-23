from fastapi import FastAPI,UploadFile,File
import uvicorn
import joblib
import numpy as np
from app.core.analyzer import AudioAnalyzer

app = FastAPI()

MODEL_PATH = r"./model/learn-model.joblib"
loaded_model = joblib.load(MODEL_PATH)

@app.post("/predict_eq")
def predict_eq_api(file: UploadFile = File(...)):
    
    audio_bytes = file.file.read() #サーバーのメモリ上で一時的に読み込む

    features = AudioAnalyzer(audio_bytes)

    predictions = loaded_model.predict(np.asarray(features))
    final_features = np.rint(predictions[0]).astype(int)

    return {
        "status": "success",
        "filename": file.filename,  # 曲名も勝手に取得できます
        "recommended_eq": final_features.tolist()
    }

if __name__ == "__main__":
    uvicorn.run("main_api:app",host="127.0.0.1",port=8000,reload=True)