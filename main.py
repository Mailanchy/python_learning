import wave
import numpy as np
import sounddevice as sd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

sample_rate = 44100
duration = 5
print("Recording...")
timeArray = np.linspace(0,duration,int(sample_rate*duration))
firstRecord = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype=np.int16) #standard for wav int16
sd.wait() #waiting to finsh the record
print("Completed recording")
with wave.open('firstRecord.wav','wb') as first:
    first.setnchannels(1)
    first.setsampwidth(2)
    first.setframerate(sample_rate)
    first.writeframes(firstRecord.tobytes())
print("Recorded a .wav audio file and saved")

# plt.xlim(0,0.1)
plt.plot(timeArray,firstRecord)
plt.show()

