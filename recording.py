
import sounddevice as sd
from scipy.io.wavfile import write
import speechRecognition

fs = 44100  # Sample rate
seconds = 1000  # Duration of recording

# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
myrecording = sd.rec(samplerate=fs, channels=2)
x = input()
if x == 1:
    sd.stop()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file
speechRecognition.recognition('output.wav')
