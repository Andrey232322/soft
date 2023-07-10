#!/usr/bin/env python3

# prerequisites: as described in https://alphacephei.com/vosk/install and also python module `sounddevice` (simply run command `pip install sounddevice`)
# Example usage using Dutch (nl) recognition model: `python test_microphone.py -m nl`
# For more help run: `python test_microphone.py -h`

import argparse
import queue
import sys
import sounddevice as sd
import vosk
import json

q = queue.Queue()

model = vosk.Model('model_small')

device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
def callback(indata, frames, time, status):

    q.put(bytes(indata))


with sd.RawInputStream(samplerate=samplerate, blocksize=40000, device=device[0],
                           dtype="int16", channels=1, callback=callback):


    rec = vosk.KaldiRecognizer(model,samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            a = json.loads(rec.Result())['text']
            #print(a)
        # else:
        #     print(rec.PartialResult())

