import tkinter
import os
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex
import moviepy.editor as mp
window=tkinter.Tk()
window.title("Converter to audio file")
window.geometry("800x500+100+100")
window.resizable(False, False)
def convert(src,dst):
    try:
        src=src[0:-1]
        dst=dst[0:-1]
        clip = mp.VideoFileClip(src)
        clip.audio.write_audiofile(dst)
        text1.delete("1.0","end")
        text2.delete("1.0","end")
        label5.config(text="Finish")
    except:
        label5.config(text="The file does not exist or the path to the file is incorrect")
    
    

label4=tkinter.Label(window)
label4.configure(font=("", 16, ""))
label4.pack()
label1=tkinter.Label(window, height=3,text="Input the video file to be converted to an mp3 file.\n ex) C:\\\\Users\\\\aaaa\\\\OneDrive\\\\back\\\\aa.mp3")
label1.configure(font=("", 16, ""))
label1.pack()
text1=tkinter.Text(window,width=50,height=2 )
text1.configure(font=("", 16, ""))
text1.pack()
label2=tkinter.Label(window, height=3,text="Input the location and name to output the converted file. \n ex) C:\\\\Users\\\\aaaa\\\\OneDrive\\\\back\\\\aa.mp4")
label2.configure(font=("", 16, ""))
label2.pack()
text2=tkinter.Text(window,width=50,height=2 )
text2.configure(font=("", 16, ""))
text2.pack()
label3=tkinter.Label(window, height=2)
label3.configure(font=("", 16, ""))
label3.pack()
button = tkinter.Button(window, width=15,height=1 , text="Convert" , command=lambda:convert(text1.get("1.0","end"),text2.get("1.0","end")))
button.configure(font=("",16 , ""))
button.pack()
label5=tkinter.Label(window, height=2)
label5.configure(font=("", 16, ""))
label5.pack()
window.mainloop()

