#noiceReduce.py
import noisereduce as nr
import librosa
import soundfile as sf

def reduce_noise(input_file, output_file):
    y, sr = librosa.load(input_file)
    reduced_noise = nr.reduce_noise(y=y, sr=sr)
    sf.write(output_file, reduced_noise, sr)

