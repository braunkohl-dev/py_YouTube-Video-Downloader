#Vorbereitungen:
#pip install pytube

from pytube import YouTube

url = input("Bitte die YouTube URL einfügen: ")

yt = YouTube(url)

stream = yt.streams.get_highest_resolution()

stream.download()
