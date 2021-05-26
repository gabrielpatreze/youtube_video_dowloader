import time
from pytube import YouTube

#url = 'https://www.youtube.com/watch?v=_RrA-R5VHQs'
url = 'https://www.youtube.com/watch?v=m4P9XkF9gsI'
my_video = YouTube(url)

print('Video Title is: ')
print(my_video.title)

print('Thumbnail Image: ')
print(my_video.thumbnail_url)

print('Let´s Dowload!')

my_video = my_video.streams.get_highest_resolution()

#or my_video = my_video.streams.first()

my_video.download()

print('Your video has been downloaded in this folder!')

