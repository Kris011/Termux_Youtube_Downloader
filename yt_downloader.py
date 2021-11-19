import pyfiglet
import os
from pytube import YouTube
os.system('clear')
#Windows
os.system('cls')
ban = pyfiglet.figlet_format("Youtube #")
print("\033[1;31m"+ban)
print("\033[0m----------------------------------")
print("\033[0mCreado por Kris")
print("\033[0mSe recomienda ultilizar el programa en")
print("\033[0mEscritorio")
print("\033[0m----------------------------------")
x=input("Link del Video: ")
video = YouTube(x)
download = video.streams.get_highest_resolution()
download.download()
