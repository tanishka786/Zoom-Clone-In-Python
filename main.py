#Zoom Clone Project By Tan-the-developer

from vidstream import * #used to stream video over a network
import tkinter as tk #used to construct basic graphical user interface (GUI) application
import socket # used to send and receive data, and they can be used to create both client-server and peer-to-peer applications
import threading #allows you to have different parts of your process run concurrently (for audio and video simultaneously)

# to get IP address from Python (Private IP address )
local_ip_address = socket.gethostbyname(socket.gethostname())
#print(local_ip_address) 
#the above line will show the local IP address given by python.

