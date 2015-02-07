from Tkinter import * 
from PIL import ImageTk

class VisionApp(object):
	def __init__(self):
		root = Tk()
		frame = Frame()
		frame.pack(fill=X, padx=5, pady=5)
		root.title("Imagen Original")