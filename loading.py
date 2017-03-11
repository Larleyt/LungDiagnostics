import librosa

WAV_FOLDER = 'audio'

for path in librosa.util.find_files(WAV_FOLDER, ext='wav'):
    y, sr = librosa.load(path)
    mfccData = librosa.feature.mfcc(y=y, sr=sr)
    print(mfccData)
