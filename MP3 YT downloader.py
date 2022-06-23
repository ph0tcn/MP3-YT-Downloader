from pytube import YouTube

URL = input('Enter URL :')

video_object = YouTube(URL)

AorV = input('Download audio or video input a or v :')

if AorV == 'a':
    video_object.streams.get_audio_only().download()
    
if AorV == 'v':
    video_object.streams.get_audio_only().download()