import os, webbrowser,sys
import sys
from sound import *
#vol = int(input("Введите громкость звука в единицах (0..100): "))
def soundup10():
    Sound.volume_set(10)
def sounddown10():
    Sound.volume_set(10)
def soundup5():
    Sound.volume_set(5)
def sounddown5():
    Sound.volume_set(5)

def browser():
    webbrowser.open('https://www.youtube.com/watch?v=4RIXR-I-jaU', new=2)
def offbot():
    sys.exit()