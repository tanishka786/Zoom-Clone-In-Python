#Zoom Clone Project By Tan-the-developer

from vidstream import * #used to stream video over a network
import tkinter as tk #used to construct basic graphical user interface (GUI) application
import socket # used to send and receive data, and they can be used to create both client-server and peer-to-peer applications
import threading #allows you to have different parts of your process run concurrently (for audio and video simultaneously)
import customtkinter # create modern looking user interfaces in python with tkinter

#customizing the background theme LEFT PROGRAMMING $$$$$$$$$$$$
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# to get IP address from Python (Private IP address )
local_ip_address = socket.gethostbyname(socket.gethostname())
#print(local_ip_address) 
#the above line will show the local IP address given by python.

########################################## Adding functionalities to buttons created ########################################################

server = StreamingServer(local_ip_address, 9999)
receiver = AudioReceiver(local_ip_address, 8888)

#Note: we are not calling the functions, we are just refering them so eg, start_server() is wriitrn without this '()'

#adding function for connecting two servers
def start_listening():
    t1 = threading.Thread(target = server.start_server)
    t2 = threading.Thread(target = receiver.start_server)
    t1.start()
    t2.start()


#adding function for video
def start_camera_stream():
    camera_client = CameraClient(entry1.get(1.0,'end-1c'), 7777)
    t3 = threading.Thread(target = camera_client.start_stream)
    t3.start()

#adding function for screen sharing
def start_screen_sharing():
    screen_client = ScreenShareClient(entry1.get(1.0,'end-1c'), 7777)
    t4 = threading.Thread(target = screen_client.start_stream)
    t4.start()

#adding function for audio streaming
def start_audio_stream():
    audio_sender = AudioSender(entry1.get(1.0,'end-1c'), 6666)
    t5 = threading.Thread(target = audio_sender.start_stream)
    t5.start()


######################################################### GUI #####################################################################

window = tk.Tk()
window = customtkinter.CTk()
window.title("Zoom clone")
window.geometry('300x200') #size of window

################# Adding elements in window for users window ################### 

label_target_ip = tk.Label(window, text = "Target IP:")
label_target_ip.pack()

#creating a text box to add the IP address
entry1 = customtkinter.CTkEntry(window, height=1, placeholder_text = "Enter your IP address:")
entry1.pack(expand = True)

#creating a button which says: start listing to incoming connections
btn_listen = customtkinter.CTkButton(window, text="Start Listening", width=50, command = start_listening)
btn_listen.pack(anchor=customtkinter.CENTER, expand=True)

#Creating a button for camera
btn_camera = customtkinter.CTkButton(window, text="Start Camera Stream", width=50, command = start_camera_stream)
btn_camera.pack(anchor=customtkinter.CENTER, expand=True)

#creating a button for screen sharing 
btn_screen = customtkinter.CTkButton(window, text="Start Screen Sharing", width=50, command = start_screen_sharing)
btn_screen.pack(anchor=customtkinter.CENTER, expand=True)

#creating a button for audio streaming
btn_audio = customtkinter.CTkButton(window, text="Start Audio Stream", width=50, command = start_audio_stream)
btn_audio.pack(anchor=customtkinter.CENTER, expand=True)

window.mainloop()



