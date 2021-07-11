from pytube import YouTube
yt_link = input("Enter the link of the video you would like to download here: ")
video = YouTube(yt_link)
video.streams.first().download()
