#曲の解析をするモジュール
import numpy as np
import librosa
import sys
import io



def AudioAnalyzer(file_path) :
    try:

        if isinstance(file_path, bytes):

            file_path = io.BytesIO(file_path)

        y, sr = librosa.load(file_path,sr=None) #yがオーディオの時系列データ(サンプル数,)、srがサンプリングレート(None=自動)

        mel_spectrogram = librosa.feature.melspectrogram(y=y,sr=sr) #人間の可聴領域に合わせる
        
        Abs = np.abs(mel_spectrogram)

        Mean = np.mean(Abs, axis=1) #平均値を求める
        Max = np.max(Abs, axis=1) #一番周波数の大きい値を取る
        Std = np.std(Abs, axis=1) #標準偏差を求める
        Future = np.hstack([Mean,Max,Std]) #平均、最大、標準偏差の情報を持った[384,]の一次配列を作る
        Reshape = np.array(Future).reshape(1,-1) #[1,384]の二次配列に直す


        return Reshape.tolist()
            
    except FileNotFoundError as e:
        print(f"File is Not Found!!: {e}")
        sys.exit()
    
