#Zoom Clone Project By Tan-the-developer

from vidstream import * #used to stream video over a network
import tkinter as tk #used to construct basic graphical user interface (GUI) application
import socket # used to send and receive data, and they can be used to create both client-server and peer-to-peer applications
import threading #allows you to have different parts of your process run concurrently (for audio and video simultaneously)

# to get IP address from Python (Private IP address )
local_ip_address = socket.gethostbyname(socket.gethostname())
#print(local_ip_address) 
#the above line will show the local IP address given by python.

######################################################### GUI #####################################################################

window = tk.Tk()
window.title("LinkUp")
window.geometry('300x200') #size of window

################# Adding elements in window for users window ################### 

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

#creating a text box to add the IP address
text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

#creating a button which says: start listing to incoming connections
btn_listen = tk.Button(window, text="Start Listening", width=50)
btn_listen.pack(anchor=tk.CENTER, expand=True)

#Creating a button for camera
btn_camera = tk.Button(window, text="Start Camera Stream", width=50)
btn_camera.pack(anchor=tk.CENTER, expand=True)

#creating a button for screen sharing 
btn_screen = tk.Button(window, text="Start Screen Sharing", width=50)
btn_screen.pack(anchor=tk.CENTER, expand=True)

#creating a button for audio streaming
btn_audio = tk.Button(window, text="Start Audio Stream", width=50)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()

