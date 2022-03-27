from msilib.schema import RadioButton
from tkinter import filedialog
from tkinter import *
import random
import math
import random
import moviepy.editor as mp
from moviepy import *
from moviepy.editor import concatenate_videoclips, vfx
import os
import os.path
from tkinter import *  
from PIL import ImageTk,Image
import webbrowser

def browse_video():
    global vid_filepath
    file = filedialog.askopenfile(mode='r', filetypes=[('MPEG-4', '*.mp4'),('Matroska', '*.mkv')])
    vid_filepath = os.path.abspath(file.name)
    VPath_Box.delete("1.0", "end")
    VPath_Box.insert(END,vid_filepath)

def browse_audio():
    global aud_filepath
    file = filedialog.askopenfile(mode='r', filetypes=[('MP3', '*.mp3'),('WAV', '*.wav')])
    aud_filepath = os.path.abspath(file.name)
    APath_Box.delete("1.0", "end")
    APath_Box.insert(END,aud_filepath)

def browse_output():
    global output_path
    file = filedialog.askdirectory()
    output_path.set(file)
    OPath_Box.delete("1.0", "end")
    OPath_Box.insert(END,output_path.get())

def new_window():
    window= Toplevel(root)
    window.title("MEET SINGLE CHRISTIANS NOW")
    window.iconbitmap(r".\img\dhruv1.ico")
    window.geometry("630x475")
    photo = PhotoImage(file = r".\img\Ad.png")

    url= r"https://www.youtube.com/channel/UCtzoF1qJOZ_kT2-D9UMQpVg"

    def openURL():
        webbrowser.open_new(url)

    def buttonY():
        ButtonZ= Button(root, text= "START", height= 2, width= 20, command= start, bg="#d9d9d9", font="Roboto")
        ButtonZ.place(x= 425, y= 500)
        window.destroy()

    def buttonX():
        Button2= Button(window, text = "X", width=1, command= buttonY)
        Button2.place(x= 10, y=10)    

    Button1= Button(window, text = 'Click Me !', image = photo, command= openURL)
    Button1.place(x=0,y=0)

    window.after(5000, buttonX)

    window.mainloop()

def start():
    out_filepath= output_path
    clip_length= int(Length_Input.get())
    video= mp.VideoFileClip(vid_filepath)
    audio= mp.AudioFileClip(aud_filepath)
    vid_duration=int(video.duration)
    aud_duration=int(audio.duration)
    if click.get()=="trim":
        clip_num= math.ceil(aud_duration/clip_length)
        clip=[]
        for i in range(0,clip_num):
            ran= random.randint(0, vid_duration-clip_length)
            clip_temp = video.subclip(ran, ran+clip_length)
            clip.insert(i, clip_temp)
        intermediate_clip= concatenate_videoclips(clip)
        output_clip= intermediate_clip.subclip(0, aud_duration)
        output_dest= str(out_filepath.get()) + "/output.mp4"
        file_exists= os.path.exists(output_dest)
        if file_exists:
            os.remove(output_dest)
        final_output= output_clip.set_audio(audio)
        final_output.write_videofile(output_dest)
    else:
        clip_num= math.floor(aud_duration/clip_length)
        clip=[]
        for i in range(0,clip_num):
            ran= random.randint(0, vid_duration-clip_length)
            clip_temp = video.subclip(ran, ran+clip_length)
            clip.insert(i, clip_temp)
        intermediate_clip= concatenate_videoclips(clip)
        output_clip= intermediate_clip.fx( vfx.speedx, (clip_num*clip_length)/aud_duration)
        output_dest= str(out_filepath.get()) + "/output.mp4"
        final_output= output_clip.set_audio(audio)
        final_output.write_videofile(output_dest)

def preview():
    prev_vid= Label(root, text= "Video Location: " + vid_filepath, font= "Georgia 9 italic", bg="#eaf1f5")
    prev_vid.place(x= 335, y= 375)
    prev_aud= Label(root, text= "Audio Location: " + aud_filepath, font= "Georgia 9 italic", bg="#eaf1f5")
    prev_aud.place(x= 335, y= 400)
    prev_len= Label(root, text= "Length of clip: " + Length_Input.get() + " seconds", font= "Georgia 9 italic", bg="#eaf1f5")
    prev_len.place(x= 335, y= 425)
    prev_out= Label(root, text= "Output Location: " + output_path.get(), font= "Georgia 9 italic", bg="#eaf1f5")
    prev_out.place(x= 335, y= 450)
    Prev_Start= Button(root, text= "START", height= 2, width= 20, command= new_window, bg="#d9d9d9", font="Roboto")
    Prev_Start.place(x= 425, y= 500)
    ButtonExit1.destroy()
    ButtonExit2= Button(root, text= "Exit", command= root.destroy, height= 1, width= 15, padx= 0, pady=0)
    ButtonExit2.place(x= 465, y=560)

root = Tk()
root.configure(bg="#eaf1f5")
root.geometry("1015x600")
root.iconbitmap(r".\img\dhruv.ico")
root.title("Video Editor for Dummies")

click= StringVar(root, "trim")
output_path= StringVar()

# Header
canvas = Canvas(root, bg="#eaf1f5")
canvas.place(x= 200, y=25)
image = Image.open(r".\img\img.png")
resized_img= image.resize((75,75), Image.ANTIALIAS)
img= ImageTk.PhotoImage(resized_img)
canvas.create_image(0, 10, anchor="nw", image=img)
Header1= Label(root, text= "The Greatest Video Editor Of All Time", font= "Roboto 25", bg="#eaf1f5", padx=0, pady=0)
Header1.place(x=285, y=35)
Header1= Label(root, text= "Made by the dumbest video editor of all time", font= "Georgia 15", bg="#eaf1f5", padx=0, pady=0)
Header1.place(x=285, y=75)

# Straight Line
Line1= Label(root, text= "______________________________________________________________________________", font= "Helvetica 12 bold", bg="#eaf1f5")
Line1.place(x=165, y=105)

# Path Of Video 
x=80
VPath_text= Label(root, text= "Enter Path To Video:", font= "Helvetica 12 bold", bg="#eaf1f5")
VPath_text.place(x=135+x, y=150)
VPath_Box= Text(root, width=39, height=1)
VPath_Box.place(x=300+x, y=152)
VidInputButton = Button(text="...", command=browse_video, border=1)
VidInputButton.place(x=625+x, y=149)

# Path Of Audio 
APath_text= Label(root, text= "Enter Path To Audio:", font= "Helvetica 12 bold", bg="#eaf1f5")
APath_text.place(x=135+x, y=175)
APath_Box= Text(root, width=39, height=1)
APath_Box.place(x=300+x, y=175)
AudInputButton = Button(text="...", command=browse_audio, border=1)
AudInputButton.place(x=625+x, y=174)

# Length Of Each Clip
Length_text= Label(root, text= "Length of Each Clip:", font= "Helvetica 12 bold", bg="#eaf1f5")
Length_text.place(x=135+x, y=200)
Length_Input= Entry(root, width= 10)
Length_Input.place(x=300+x, y= 199)

#Video File Type
RadioButton1= Radiobutton(root, text = "Trim Last Clip", variable = click, value = "trim", font= "Aerial 10", bg="#eaf1f5")
RadioButton1.place(x = 370+x, y= 195)
RadioButton2= Radiobutton(root, text = "Extend Entire Video", variable = click, value = "extend", font= "Aerial 10", bg="#eaf1f5")
RadioButton2.place(x = 475+x, y= 195)

# Path Of Output Folder 
OPath_text= Label(root, text= "Output Path:", font= "Helvetica 12 bold", bg="#eaf1f5")
OPath_text.place(x=135+x, y=225)
OPath_Box= Text(root, width=39, height=1)
OPath_Box.place(x=300+x, y=224)
OutputButton = Button(text="...", command=browse_output, border=1)
OutputButton.place(x=625+x, y=225)

# Preview Button
Prev_Button= Button(root, text= "PREVIEW", font= "Roboto", height= 2, width= 20, command= preview, padx=0, pady=0)
Prev_Button.place(x= 425, y= 260)

# Straight Line
Line2= Label(root, text= "______________________________________________________________________________", font= "Helvetica 12 bold", bg="#eaf1f5", padx=0, pady= 0)
Line2.place(x=165, y=325)

# Exit Button
ButtonExit1= Button(root, text= "Exit", command= root.destroy, height= 1, width= 15, padx= 0, pady=0)
ButtonExit1.place(x= 465, y=315)

root.mainloop() 

