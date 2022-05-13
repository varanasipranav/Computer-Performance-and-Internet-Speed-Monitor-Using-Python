# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:16:29 2022

@author: Pranav Varanasi
"""
from tkinter import *
root =Tk()
import math
import psutil
from PIL import Image,ImageTk


image=Image.open('122.png')
tk_image=ImageTk.PhotoImage(image)
import speedtest

st=speedtest.Speedtest()

root.geometry("1300x1080")
root.title("CPU STATS")
cpu_count_label=Label(root,font=("Orbitron",40,'bold'),text="0")
cpu_count_label.grid(row=0,column=0)
cpu_usage_label = Label(root,font=("Orbitron",40,'bold'),text="0")
cpu_usage_label.grid(row=0,column=1)
ram_count_label=Label(root,font=("Orbitron",40,'bold'),text="0")
ram_count_label.grid(row=0,column=3)
ram_usage_label=Label(root,font=("Orbitron",40,'bold'),text="0")
ram_usage_label.grid(row=0,column=4)
avail_ram_label=Label(root,font=("Orbitron",40,'bold'),text="")
avail_ram_label.grid(row=0,column=5)
download_label =Label(root,font=("Orbitron",40,'bold'),text="0 Mbps")
download_label.grid(row=3,column=1)
upload_label =Label(root,font=("Orbitron",40,'bold'),text="0 Mbps")
upload_label.grid(row=3,column=3)
ping_label =Label(root,font=("Orbitron",40,'bold'),text="0 Mbps")
ping_label.grid(row=3,column=4)


def usage():
    cpu_count=psutil.cpu_count()
    cpu_count_label.config(text=cpu_count,image=tk_image,compound='center',fg='#00ffff')
    cpu_usage = psutil.cpu_percent(1)
    cpu_usage_label.config(text=cpu_usage,image=tk_image,compound='center',fg='#00ffff')
    cpu_usage_label.after(100,usage)
    ram_count=math.floor(psutil.virtual_memory()[0]/1000000000)
    ram_count_text=str(ram_count)+"GB"
    ram_count_label.config(text=ram_count_text,image=tk_image,compound='center',fg='#00ffff')
    ram_usage=psutil.virtual_memory()[2]
    ram_usage_text=str(ram_usage)+"%"
    ram_usage_label.config(text=ram_usage_text,image=tk_image,compound='center',fg='#00ffff')
    available_ram=math.floor(psutil.virtual_memory()[1]/1000000000)
    available_ram_text=str(available_ram)+"GB"
    avail_ram_label.config(text=available_ram_text,image=tk_image,compound='center',fg='#00ffff')
def inter_speed():
    print("Testing Internet Speed")
    download_speed=str(math.floor(st.download()/1000000))+"Mb/S"
    upload_speed=str(math.floor(st.upload()/1000000))+"MB/S"
    ping=str(math.floor(st.results.ping))+ "MS"
    upload_label.config(text=upload_speed,image=tk_image,compound='center',fg='#00ffff')
    download_label.config(text=download_speed,image=tk_image,compound='center',fg='#00ffff')
    ping_label.config(text=ping,image=tk_image,compound='center',fg='#00ffff')
    
usage()
l1=Label(root,font=("Orbitron",20,'bold'),fg='black',text='No of CPUS')
l1.grid(row=1,column=0)
l2=Label(root,font=("Orbitron",20,'bold'),fg='black',text='CPU usage in %')
l2.grid(row=1,column=1)
l3=Label(root,font=("Orbitron",20,'bold'),fg='black',text="Total RAM")
l3.grid(row=1,column=3)
l4=Label(root,font=("Orbitron",20,'bold'),fg='black',text="% Ram used")
l4.grid(row=1,column=4)
l5=Label(root,font=("Orbitron",20,'bold'),fg='black',text="Available Ram")
l5.grid(row=1,column=5)
l6=Label(root,font=("Orbitron",20,'bold'),fg='black',text="Download speed")
l6.grid(row=4,column=1)
l7=Label(root,font=("Orbitron",20,'bold'),fg='black',text="Upload speed")
l7.grid(row=4,column=3)
l8=Label(root,font=("Orbitron",20,'bold'),fg='black',text="PING")
l8.grid(row=4,column=4)
speed_button=Button(root,text="test internet speed",command=inter_speed)
speed_button.grid(row=3,column=0 )


root.mainloop()