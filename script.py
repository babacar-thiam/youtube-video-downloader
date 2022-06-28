""" A Simple python script to Download a youtube video and save it to a file.
    Athor: @babacar-thiam
    E-mail: bahertaleb@gmail.com
    Full Name: Babacar Thiam """

from pytube import YouTube

link = input('Paste the youtube video you want to download: ')
yt = YouTube(link)
yt.streams.filter(res='720p').first().download() # Download the video in 720p
print('Downloaded!', link)