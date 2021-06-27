
#!/usr/bin/python
from format_csv import csv_format
import wave
import struct
import sys
import csv
import numpy
from scipy.io import wavfile
from scipy.signal import resample


def write_wav(data, filename, framerate, amplitude):
    wavfile = wave.open(filename, 'w')
    nchannels = 1
    sampwidth = 2
    framerate = framerate
    nframes = len(data)
    comptype = "NONE"
    compname = "not compressed"
    wavfile.setparams((nchannels,
                       sampwidth,
                       framerate,
                       nframes,
                       comptype,
                       compname))
    frames = []
    for s in data:
        mul = int(s * amplitude)
        frames.append(struct.pack('h', mul))

    frames = ''.join(frames)
    wavfile.writeframes(frames)
    wavfile.close()
    print("%s written" % (filename))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("You must supply a filename to generate")
        exit(-1)
    for fname in sys.argv[1:]:
        csv_format(fname)
        data = []
        for time, value in csv.reader(open(fname, 'U'), delimiter=','):
            try:
                # Here you can see that the time column is skipped
                data.append(float(value))
            except ValueError:
                pass  # Just skip it

        arr = numpy.array(data)  # Just organize all your samples into an array
        # Normalize data
        # Divide all your samples by the max sample value
        arr /= numpy.max(numpy.abs(data))
        filename_head, extension = fname.rsplit(".", 1)
        data_resampled = resample(arr, len(data))
        audio_filename = fname.replace("csv", "wav")
        audio_filename = audio_filename.replace("data/", "")
        if 'Lab_1' in audio_filename:
            sr = 2000  # Sampling rate of 2kHz for csv files with 6000 lines
        elif 'Lab_3' in audio_filename:
            sr = 300  # 300 Hz for csv files with 1200 lines
        wavfile.write(f'data/Audio/{audio_filename}',
                      sr, data_resampled)
        print("File written succesfully !")
