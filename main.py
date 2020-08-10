from pytube import YouTube
import sys
import os


def on_complete(a, b):
    print("Donwload completed")
    print(f"video at:\n{b}")


def progress_function(chunks, file_handler, bytes_remaining):
    if bytes_remaining > total_size:
        return
    else:
        print(f"{int((1-(float(bytes_remaining)/float(total_size)))*100)} %")


for video_link in sys.argv[1:]:
    try:
        video = YouTube(video_link, on_progress_callback=progress_function,
                        on_complete_callback=on_complete)
        filt = video.streams.filter(progressive=True, file_extension='mp4')
        total_size = filt.first().filesize
        filt.get_highest_resolution().download(
            output_path=os.environ['VIDEO_PATH'])
    except:
        print('no internet/video found')
