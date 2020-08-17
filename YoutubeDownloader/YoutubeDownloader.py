try:
    from pytube import YouTube
    import tkinter as tk

except:
  print("An error with the module has occurred")

#Code 
#video function - downloads youtube videos
def video():
    user_link = link.get()
    yt_link = YouTube(' ' + user_link + ' ')

    #label asking to select itag
    label = tk.Label(frame2, text="Video information (Input itag number in the itag field)", pady = 20, bg="#212121", fg="white")
    label.pack()

    for itag in yt_link.streams.filter(progressive=True):
        print(itag)
        itg_label = tk.Label(frame2, text=itag, bg="#212121", fg="white")
        itg_label.pack()

#audio function - downloads youtube videos audio
def audio():
    user_link = link.get()
    yt_link = YouTube(' ' + user_link + ' ')

    #label asking to select itag
    label = tk.Label(frame2, text="Video information (Input itag number in the itag field)", pady = 1, bg="#212121", fg="white")
    label.pack()

    for itag in yt_link.streams.filter(only_audio=True):
        print(itag)
        itg_label = tk.Label(frame2, text=itag, bg="#212121", fg="white")
        itg_label.pack()

#download function via itag - sends download to path
def download():
    yt_itag = itag_input.get()
    yt_link = YouTube(' ' + link.get() + ' ')

    yt_video = yt_link.streams.get_by_itag(yt_itag)

    path = paths.get()
    yt_video.download(path)

    title = ("\nDownloading " + yt_link.title)
    download_label = tk.Label(frame2, text=title, bg="#212121", fg="white", font=('bold'), pady = 5)
    download_label.pack()

#GUI 
#create root
root = tk.Tk()

#create title
root.title("Youtube Downloader")
root.configure(bg="#424242")

window = tk.Canvas(root, height = 400, width = 800, bg="#424242")
window.pack()

#create frame
frame = tk.Frame(root, bg = "#212121")
frame.place(relwidth = 0.98, relheight = 0.35, relx = 0.01, rely = 0.05)

frame2 = tk.Frame(root, bg = "#212121")
frame2.place(relwidth = 0.98, relheight = 0.5, relx = 0.01, rely = 0.42)

#create link label/input-field
link_label = tk.Label(frame, text="Please enter the youtube link: ", bg="#212121", fg="white")
link_label.place(relx = 0.15, rely = 0.15)

link = tk.Entry(frame, width=50, bg="#AAAAAA")
link.place(relx = 0.4, rely = 0.15)

#create audio label/input-field/buttons
audio = tk.Button(frame, text="Audio", command=audio)
audio.place(relwidth = 0.1, relheight = 0.15, relx = 0.48, rely = 0.35)

#create video label/input-field/buttons
video = tk.Button(frame, text="Video", command=video)
video.place(relwidth = 0.1, relheight = 0.15, relx = 0.61, rely = 0.35)

#create itags label/input-field
itag_label = tk.Label(frame, text="Please enter the itag number: ", bg="#212121", fg="white")
itag_label.place(relx = 0.15, rely = 0.60)

itag_input = tk.Entry(frame, width=50, bg="#AAAAAA")
itag_input.place(relx = 0.4, rely = 0.60)

#create paths label/input-field
path_label = tk.Label(frame, text="Please enter the path: ", bg="#212121", fg="white")
path_label.place(relx = 0.15, rely = 0.80)

paths = tk.Entry(frame, width=50, bg="#AAAAAA")
paths.place(relx = 0.4, rely = 0.80)

#create download button
downloads = tk.Button(root, text="Press to download", command=download, pady= 1)
downloads.pack()

root.mainloop()



