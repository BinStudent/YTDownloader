import tkinter as tk
from pytube import YouTube
import os
import itertools
import threading
import time
import sys


def get_link():

    yt = YouTube(entry.get())

    done = False

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            entry.delete(0, tk.END)
            entry.insert(0, "\rloading " + c)
            sys.stdout.flush()
            time.sleep(0.1)
        entry.delete(0, tk.END)
        entry.insert(0, "Finished in " + dirpath + "!")

    t = threading.Thread(target=animate)
    t.start()

    ys = yt.streams.get_audio_only()
    winname = os.getenv('username')
    dirpath = r"C:/Users/" + winname + "/Music/YTDownloads"

    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    out_file = ys.download(dirpath)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    done = True


window = tk.Tk()
window.title("MP3 Downloader | 1.0")
window.geometry("330x150")
window.resizable(False, False)
window.wm_iconbitmap(".\logo.ico")


label = tk.Label(window,
                text="Type the YouTube link below to download!")

label.pack(expand=True)

entry = tk.Entry(window,
                justify="center",
                width=35)

button = tk.Button(window, text="Download", command=get_link, width=15)
button.pack()

entry.pack(fill="both")

window.mainloop()