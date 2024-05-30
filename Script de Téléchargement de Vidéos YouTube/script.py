from pytube import YouTube

def download_video(url, path):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(path)

if __name__ == "__main__":
    download_video('https://www.youtube.com/watch?v=example', 'path/to/download')
