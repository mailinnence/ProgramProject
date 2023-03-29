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
from datetime import datetime
import tkinter
import os
import moviepy.editor as mp
import time
window=tkinter.Tk()
window.title("Sound Seperate Program")
window.geometry("900x620+100+100")
window.resizable(True, True)




class main:
    def __init__(self):
        self.selectNum=2
    def mainpage(self):
        #버튼으로 지우는 함수
        def convert():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginTwo1.pack_forget()
            marginTwo2.pack_forget()
            marginTwo3.pack_forget()
            mp3filelist.pack_forget()
            spfilelist.pack_forget()
            convertfilelist.pack_forget()
            main().convert()
        def Seperate():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginTwo1.pack_forget()
            marginTwo2.pack_forget()
            marginTwo3.pack_forget()
            mp3filelist.pack_forget()
            spfilelist.pack_forget()
            convertfilelist.pack_forget()
            main().Seperate()
        def openfile(num):
            print(os.getcwd)
            if num==1:
                os.system('nautilus convert')
            if num==2:
                os.system('nautilus mp3')
            if num==3:
                os.system('nautilus seperated')
        #메뉴바 초기화
        menubar=tkinter.Menu(window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        window.config(menu=menubar)
        #한칸띄우기 용 위젯
        marginTwo1=tkinter.Label(window, height=10)
        marginTwo2=tkinter.Label(window, width=10 )
        marginTwo3=tkinter.Label(window, width=10 )
        marginTwo1.pack()
        #메인 테마 라벨
        marginOne1=tkinter.Label(window, text="Sound Seperation Program")
        marginOne1.configure(font=("", 40, ""))
        marginOne1.pack()
        #plaintext
        marginOne2=tkinter.Label(window, height=5 ,text="Convert : This page converts mp4 files to mp3 in convert folder\n Seperate : This page seperates mp3 files in mp3 folder ")
        marginOne2.configure(font=("", 16, ""))
        marginOne2.pack()
        #mp3 전환 페이지로 이동
        fbutton1 = tkinter.Button(window, width=15 , text="Convert" , command=convert )
        fbutton1.configure(font=("", 16, ""))
        marginTwo2.pack(side="left")
        fbutton1.pack(side="left")
        #mp3 분리 페이지로 이동
        fbutton2 = tkinter.Button(window, width=15 , text="Seperate", command=Seperate  )
        fbutton2.configure(font=("", 16, ""))
        marginTwo3.pack(side="right")
        fbutton2.pack(side="right")
        #한칸 내리기
        marginOne3=tkinter.Label(window, height=8)
        marginOne3.pack()
        #convert 리스트를 보여줌
        convertfilelist= tkinter.Button(window, width=15 , text="Open Convert File",command=lambda: openfile(1) )
        convertfilelist.configure(font=("", 16, ""))
        convertfilelist.pack()
        #한칸 내리기
        marginOne4=tkinter.Label(window)
        marginOne4.pack()
        #mp3 리스트를 보여줌
        mp3filelist= tkinter.Button(window, width=15 , text="Open Mp3 File",command=lambda: openfile(2) )
        mp3filelist.configure(font=("", 16, ""))
        mp3filelist.pack()
        #한칸 내리기
        marginOne5=tkinter.Label(window)
        marginOne5.pack()
        #sepearted 리스트를 보여줌
        spfilelist= tkinter.Button(window, width=18 , text="Open Seperated File",command=lambda: openfile(3) )
        spfilelist.configure(font=("", 16, ""))
        spfilelist.pack()
        window.mainloop()
    def convert(self):
        def movemainpage():
            marginTwo1.pack_forget()
            mp4list.pack_forget()
            plaintext1.pack_forget()
            convertbutton.pack_forget()
            showconvertfilebutton1.pack_forget()
            showconvertfilebutton2.pack_forget()
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginOne6.pack_forget()
            main().mainpage()
        def openfile(num):
            if num==1:
                os.system('nautilus convert')
            if num==2:
                os.system('nautilus mp3')
        def convertmv():
            try:
                path = os.getcwd()
                file_names = os.listdir(file_path)
                file_names
                for name in file_names:
                    name2=name.split('.')
                    if name2[1]=="mp4":
                        name1=path+"/convert/"+name
                        name2=name.split('.')
                        clip = mp.VideoFileClip(name1)
                        clip.audio.write_audiofile(path+"/mp3/"+name[0]+".mp3")
                        marginOne6['text']="Complete!!\n Show mp3 folder"
            except:
                marginOne6['text']="error"
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movemainpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)
        window.config(menu=menubar)
        #한칵 띄우기
        marginTwo1=tkinter.Label(window, width=2 )
        marginTwo1.pack(side="left")
        #mp4 파일 리스트 목록
        mp4list=tkinter.Text(window,width=23,height=18)
        mp4list.insert(tkinter.CURRENT, "_<Video List>__________\n")
        file_path = './convert'
        file_names = os.listdir(file_path)
        file_names
        for name in file_names:
            name2=name.split('.')
            if name2[1]=="mp4":
                name+="\n"
                mp4list.insert(tkinter.CURRENT, name)
        mp4list.configure(font=("", 24, "") , state='disabled')
        mp4list.pack(side="left")
        #한칸 띄우기
        marginOne1=tkinter.Label(window, height="5" )
        marginOne1.pack()
        #설명문
        plaintext1=tkinter.Label(window , text="Press Open Convert File button\n to insert the video file to be converted to mp3 \n\nThe converted file to mp3 can be checked \nby pressing the Open Mp3 File button.")
        plaintext1.configure(font=("", 16, ""))
        plaintext1.pack()
        #한칸 띄우기
        marginOne2=tkinter.Label(window )
        marginOne2.pack()
        #전환 버튼
        convertbutton = tkinter.Button(window, width=15,text="Convert" ,command=convertmv)
        convertbutton.configure(font=("", 16, ""))
        convertbutton.pack()
        #한칸 띄우기
        marginOne3=tkinter.Label(window)
        marginOne3.pack()
        #파일열기 버튼
        showconvertfilebutton1 = tkinter.Button(window, width=15,text="Open Convert File" ,command=lambda: openfile(1))
        showconvertfilebutton1.configure(font=("", 16, ""))
        showconvertfilebutton1.pack()
        #한칸 띄우기
        marginOne4=tkinter.Label(window)
        marginOne4.pack()
        #파일열기 버튼
        showconvertfilebutton2 = tkinter.Button(window, width=15,text="Open Mp3 File" ,command=lambda: openfile(2))
        showconvertfilebutton2.configure(font=("", 16, ""))
        showconvertfilebutton2.pack()
        #한칸 띄우기
        marginOne5=tkinter.Label(window ,text="")
        marginOne5.pack()
        #예외처리 결과
        marginOne6=tkinter.Label(window ,text="")
        marginOne6.configure(font=("", 16, ""))
        marginOne6.pack()
    def Seperate(self):
        def movemainpage():
            marginTwo1.pack_forget()
            mp4list.pack_forget()
            plaintext1.pack_forget()
            speratebutton.pack_forget()
            showfilelistbutton1.pack_forget()
            showfilelistbutton2.pack_forget()
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginOne6.pack_forget()
            radio1.pack_forget()
            radio2.pack_forget()
            radio3.pack_forget()
            main().mainpage()
        def openfile(num):
            if num==1:
                os.system('nautilus mp3')
            if num==2:
                os.system('nautilus seperated')
        def selectNum(num):
            self.selectNum=num
        def ssperate():
            try:
                from spleeter.separator import Separator
                from spleeter.audio.adapter import AudioAdapter
                path = os.getcwd()
                file_names = os.listdir(file_path)
                file_names
                for name in file_names:
                    name2=name.split('.')
                    if name2[1]=="mp3" or "wav":
                        separator=Separator(f"spleeter:{self.selectNum}stems")
                        separator.separate_to_file(os.getcwd()+"/mp3/"+name , "./seperated/")
                        marginOne6['text']="Complete!!\n Show Seperated folder"
            except:
                marginOne6['text']="error"
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movemainpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)
        window.config(menu=menubar)
        #한칵 띄우기
        marginTwo1=tkinter.Label(window, width=2 )
        marginTwo1.pack(side="left")
        #mp4 파일 리스트 목록
        mp4list=tkinter.Text(window,width=23,height=18)
        mp4list.insert(tkinter.CURRENT, "_<Mp3 List>___________\n")
        file_path = './mp3'
        file_names = os.listdir(file_path)
        file_names
        for name in file_names:
            name+="\n"
            mp4list.insert(tkinter.CURRENT, name)
        mp4list.configure(font=("", 24, "") , state='disabled')
        mp4list.pack(side="left")
        #한칸 띄우기
        marginOne1=tkinter.Label(window, height="5" )
        marginOne1.pack()
        #설명문
        plaintext1=tkinter.Label(window , text="If you press a separate button,\n the mp3 file in the mp3 folder isseparated")
        plaintext1.configure(font=("", 16, ""))
        plaintext1.pack()
        #한칸 띄우기
        marginOne2=tkinter.Label(window )
        marginOne2.pack()
        #mode selecter
        RadioVariety_1=tkinter.IntVar()
        radio1=tkinter.Radiobutton(window, text="vocals / other (defalut) ", value=1, variable=RadioVariety_1 ,command=lambda: selectNum(2) )
        radio1.configure(font=("", 16, ""))
        radio1.pack()
        radio2=tkinter.Radiobutton(window, text="vocals / bass / drums / other", value=3, variable=RadioVariety_1 ,command=lambda: selectNum(4))
        radio2.configure(font=("", 16, ""))
        radio2.pack()
        radio3=tkinter.Radiobutton(window, text="vocals / bass / drums / piano / other", value=9, variable=RadioVariety_1 ,command=lambda: selectNum(5))
        radio3.configure(font=("", 16, ""))
        radio3.pack()
        #한칸 띄우기
        marginOne3=tkinter.Label(window )
        marginOne3.pack()
        #분리 버튼
        speratebutton = tkinter.Button(window, width=15,text="Seperate" ,command=ssperate)
        speratebutton.configure(font=("", 16, ""))
        speratebutton.pack()
        #한칸 띄우기
        marginOne3=tkinter.Label(window)
        marginOne3.pack()
        #파일열기 버튼
        showfilelistbutton1 = tkinter.Button(window, width=15,text="Open Mp3 File" ,command=lambda: openfile(1))
        showfilelistbutton1.configure(font=("", 16, ""))
        showfilelistbutton1.pack()
        #한칸 띄우기
        marginOne4=tkinter.Label(window )
        marginOne4.pack()
        #파일열기 버튼
        showfilelistbutton2 = tkinter.Button(window, width=18,text="Open Seperated File" ,command=lambda: openfile(2))
        showfilelistbutton2.configure(font=("", 16, ""))
        showfilelistbutton2.pack()
        #한칸 띄우기
        marginOne5=tkinter.Label(window ,text="")
        marginOne5.pack()
        #예외처리 결과
        marginOne6=tkinter.Label(window ,text="")
        marginOne6.configure(font=("", 16, ""))
        marginOne6.pack()









if __name__=='__main__':
    main().mainpage()
