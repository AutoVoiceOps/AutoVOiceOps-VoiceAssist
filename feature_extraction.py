import numpy as np
import librosa

def extract_features(filename):
    y, sr = librosa.load(filename)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)
