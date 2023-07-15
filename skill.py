import os, webbrowser,sys
import sys
from sound import *
#v = int(input("Введите громкость звука в единицах (0..100): "))  зависит в telebot если удалить
#если удалить v тут то еще надо удалить в tgbot
def soundup10(v):
    Sound.volume_set(v)
def sounddown10(v):
    Sound.volume_set(v)
def soundup5():
    Sound.volume_set(5)
def sounddown5():
    Sound.volume_set(5)

def browser():
    webbrowser.open('https://www.youtube.com/watch?v=4RIXR-I-jaU', new=2)
def offbot():
    sys.exit()

