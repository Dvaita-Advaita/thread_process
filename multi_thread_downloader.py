import time
import threading

def downloader(file):
    print(f"Downloading {file}...")
    time.sleep(3)   # Simulates download time
    print(f"{file} downloaded!")


t1 = threading.Thread(target=downloader, args=("movie.mp4",))
t2 = threading.Thread(target=downloader, args=("song.mp3",))
t3 = threading.Thread(target=downloader, args=("image.jpg",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


