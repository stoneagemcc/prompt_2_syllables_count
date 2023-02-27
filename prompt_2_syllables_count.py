import speech_recognition as sr
from collections import Counter


file = 'ptk_2.wav'
phrase = 'pa ta ka'


r = sr.Recognizer()
wav = sr.AudioFile(file)

with wav as source:
    #r.adjust_for_ambient_noise(source, duration=1.2)
    audio = r.record(source, offset=1.2)


count = Counter()
for i in range(11):
    sensitivity = i*0.1 # 0 ~ 1
    try:
        syllables = r.recognize_sphinx(audio, keyword_entries=[(phrase, sensitivity)])
        n_match = len(syllables.strip().split('  ')) # phrase separated by double spaces '  '
    except sr.UnknownValueError:
        n_match = 0
    count.update([n_match])
    print(f'sensitivity:{i*0.1:.1f} , count:{n_match}')

print(f'"{phrase}" has occured {count.most_common()[0][0]} times in "{file}"')





# check audio spectrum vs time
"""
import numpy as np
import matplotlib.pyplot as plt
import librosa
y, sr = librosa.load("ptk_2.wav")
#plt.plot(np.arange(len(y))/sr, y); plt.show() # time series

D = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

librosa.display.specshow(D, x_axis='time', y_axis='log'); plt.show()
"""
