from vidstream import *
import tkinter as tk
import socket
import threading
import requests

local_ip_addr = socket.gethostbyname(socket.gethostname())
public_ip_addr = requests.get("https://api.ipify.org").text

print(local_ip_addr)
print(public_ip_addr)

server = StreamingServer(local_ip_addr, 9999) # send
receiver = AudioReceiver(local_ip_addr, 8888) # receive

#adding function for connecting two servers
def start_listening():
    t1 = threading.Thread(target = server.start_server)
    t2 = threading.Thread(target = receiver.start_server)
    t1.start()
    t2.start()

#adding function for video
def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'), 7777) # send
    t3 = threading.Thread(target = camera_client.start_stream)
    t3.start()

#adding function for screen sharing
def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'), 7777) # send
    t4 = threading.Thread(target = screen_client.start_stream)
    t4.start()

#adding function for audio streaming
def start_audio_stream():
    audio_sender = AudioSender(text_target_ip.get(1.0,'end-1c'), 6666) # receive
    t5 = threading.Thread(target = audio_sender.start_stream)
    t5.start()


window = tk.Tk()
window.title("My zoom app - streamer")
window.geometry("350x250")

label_target_ip = tk.Label(window, text="Target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start Listening", width=50, command=start_listening)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Stream", width=50, command=start_audio_stream)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()