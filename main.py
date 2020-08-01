from tkinter import*
import webbrowser
from tkinter import filedialog,messagebox
from pytube import YouTube
def link():
    webbrowser.open_new('https://www.youtube.com/')
def downloadevideo():
    try:
        link=Entery_box.get()
        down_video_btn.config(text="please wait..")
        down_video_btn.config(state=DISABLED)
        path_of_save_video=filedialog.askdirectory()
        if path_of_save_video is None:
            return
        yt_video=YouTube(link)
        video=yt_video.streams.first()
        video.download(path_of_save_video)
        down_video_btn.config(text="Downloade video")
        down_video_btn.config(state=NORMAL)
        messagebox.showinfo("download complete","download successful")
    except Exception as e:
        messagebox.showerror("Error..", "please check Link")
def downloadeaudio():
    try:
        link = Entery_box.get()
        down_audio_btn.config(text="please wait..")
        down_audio_btn.config(state=DISABLED)
        save_path = filedialog.askdirectory()
        youtube_link = YouTube(link)
        video = youtube_link.streams.get_audio_only()
        video.download(save_path)
        down_audio_btn.config(text="Downloade audio")
        down_audio_btn.config(state=NORMAL)
        messagebox.showinfo("download complete", "download successful")
    except Exception as e:
        print(e)

window=Tk()
window.title("youtube videos Downloader")
window.geometry("600x300")
icon=PhotoImage(file="icon.png")
window.iconphoto(FALSE,icon)
frame=Frame(window)
frame.pack(sid=TOP)
photo=Label(frame,image=icon)
title_text=Label(frame,text="YouTube video Downloader",font="arial 20")

Entery_box=Entry(frame,width=50,font="safron 10")
search_btn=Button(frame,text="Get Link",width=20,relief="groove",command=link)

down_video_btn=Button(frame,text="Download video ",width=30,font="Viner",relief='ridge',
                       command=downloadevideo,fg="red")
down_audio_btn=Button(frame,text="Download audio ",width=20,font="arial 12 bold",relief='ridge',
                       command=downloadeaudio,fg="green")
# pack
photo.grid(row=0,column=0)
title_text.grid(row=1,column=0)
Entery_box.grid(row=2,column=0)
search_btn.grid(row=2,column=1)
down_video_btn.grid(row=3,column=0,pady=10)
down_audio_btn.grid(row=3,column=1)
window.mainloop()
