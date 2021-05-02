from pytube import YouTube

url = input("Enter the url: ")
video = YouTube(url)
content = video.streams.get_highest_resolution()
content.download()
print("\nDownload Completed !")