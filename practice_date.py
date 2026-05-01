import csv
import librosa
import numpy as np
import pandas as pd

def send_music_detail():
    confirmation = np.load("practice_date.npy")
    print("今の配列データ")
    print(confirmation.shape)


    print("what is music_name?")
    music_name = input()
    
    try:
        y, sr = librosa.load(music_name,sr=None)
        
    except FileNotFoundError as e:
        print(f"File is Not Found!!: {e}")
        return 0
    

    write_music_name = []
    write_music_name.append(music_name)
    with open('music_name.csv', 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(write_music_name)

    with open('music_name.csv', newline="") as f:
        print(f.read())

    print(len(y))
    print(sr)

    mel_spectrogram = librosa.feature.melspectrogram(y=y,sr=sr)
    print(mel_spectrogram)
    print(mel_spectrogram.shape)
    
    Abs = np.abs(mel_spectrogram)

    Mean = np.mean(Abs, axis=1)
    Max = np.max(Abs, axis=1)
    Std = np.std(Abs, axis=1)

    print(Mean.shape)
    print(Max.shape)
    print(Std.shape)

    Future = np.hstack([Mean,Max,Std])
    print(Future.shape)
    Reshape = np.array(Future).reshape(1,-1)

    result = np.vstack([confirmation,Reshape])

    np.save("practice_date.npy", result)
    
    confirmation = np.load("practice_date.npy")
    print("今の配列データ")
    print(confirmation)
    print(confirmation.shape)


    return 0
    
send_music_detail()
