import argparse
import queue
import sys
import sounddevice as sd
import vosk
import json
import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skill import *


q = queue.Queue()

model = vosk.Model('model_small')

device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

def callback(indata, frames, time, status):

    q.put(bytes(indata))

def reco(data,vectorizer,clf):
    trg =  words.Triger.intersection(data.split())
    if not trg:
        return
    data.replace(list(trg)[0],'')
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func = answer.split()[0]
    exec(func + '()')


def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors,list(words.data_set.values()))

    del words.data_set

    with sd.RawInputStream(samplerate=samplerate, blocksize=40000, device=device[0],
                               dtype="int16", channels=1, callback=callback):


        rec = vosk.KaldiRecognizer(model,samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                a = json.loads(rec.Result())['text']
                reco(a,vectorizer,clf)

if __name__ =='__main__':
    main()
