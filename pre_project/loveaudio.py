import librosa
import numpy as np
from sklearn.ensemble  import RandomForestRegressor as RFR
import joblib

y, sr = librosa.load("sample.flac",sr=None)

print(len(y))
print(sr)
C=len(y)/sr
print(C)

S = librosa.stft(y)
print(S.shape)

mag = np.abs(S)
features = np.mean(mag,axis=1)
print(features.shape)
print(features)

a, sd = librosa.load("kuronuri.flac",sr=None)
K = librosa.stft(a)
magK = np.abs(K)
featuresK = np.mean(magK,axis=1)
print(featuresK)

b, sb = librosa.load("yanagi.flac",sr=None)
Y = librosa.stft(b)
magY = np.abs(Y)
featuresY = np.mean(magY,axis=1)
print(featuresY)

c, sc = librosa.load("sanbo.flac",sr=None)
Sa = librosa.stft(c)
magSa = np.abs(Sa)
featuresSa = np.mean(magSa,axis=1)
print(featuresSa)

X = np.array([featuresK,featuresY,featuresSa])
print(X.shape)

y = np.array([[+3,-2,0,+3,+4,+5],[+10,+8,+6,+7,+8,+10],[+5,+6,+8,+10,+6,+8]])
print(type(y),y)

love, slove = librosa.load("loveu.flac",sr=None)
Slove = librosa.stft(love)
magSlove = np.abs(Slove)
featuresSlove = np.mean(magSlove,axis=1)
print(featuresSlove)
print(featuresSlove.shape)
u = np.array(featuresSlove).reshape(1,-1)
print(u)

#学習フェーズ
model = RFR()

model.fit(X,y)

results = model.predict(u)
joblib.dump(model,"learn-model.joblib")
print(results)
print(type(results), results)
result = np.round(results, 0)
print(result)

