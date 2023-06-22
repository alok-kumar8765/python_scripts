# Python Downloader
# pip install internetdownloadmanager
import internetdownloadmanager as idm
def Downloader(url, output):
    pydownloader = idm.Downloader(worker=20,
                                part_size=1024*1024*10,
                                resumable=True,)

    pydownloader .download(url, output)
Downloader("https://www.youtube.com/watch?v=DvNQwzzB8pg", "image.jpg")
Downloader("https://www.youtube.com/watch?v=DvNQwzzB8pg", "video.mp4")