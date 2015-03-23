#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
CONFIG_FILE = open('config.json')
data_json = json.load(CONFIG_FILE)
IMAGE_SOURCE = data_json['config']['path']['image_source']
IMAGE_RESULT = data_json['config']['path']['image_result']
IMAGE_FORMAT = data_json['config']['image_properties']['file_format']
CONFIG_FILE.close()

from Tkinter import *
from PIL import Image, ImageTk
from bin.ImageFilter import ImageFilter
from bin.Filtros import BaseImage, Filtros, Threshold

PATH_IMAGE = IMAGE_SOURCE + 'sample.png'

class VisionApp(object):
	def __init__(self):
		#Filter class
		self.imageFilterapp = ImageFilter(PATH_IMAGE)

		#GUI
		self.create_window()
		self.create_buttons()
		self.load_image(Image.open(PATH_IMAGE))
		self.root.mainloop()


	def create_window(self):
		self.root = Tk()
		self.frame = Frame()
		self.frame.pack(fill=X, padx=5, pady=5)
		self.root.title("Tarea 1")
		self.frameButtons1 = Frame()
		self.frameButtons1.pack(fill=X, padx=1, pady=1)
		self.frameButtons2 = Frame()
		self.frameButtons2.pack(fill=X, padx=1, pady=1)

	def create_buttons(self):
		btnOriginal = Button(text="Original", command=self.original_image)
		btnOriginal.pack(in_=self.frame, side=LEFT)

		btnGrayScale = Button(text="GrayScale", command=self.grayScale_image)
		btnGrayScale.pack(in_=self.frame, side=LEFT)

		btnGrayScaleMin = Button(text="GrayScaleMin", command=self.grayScaleMin_image)
		btnGrayScaleMin.pack(in_=self.frame, side=LEFT)

		btnGrayScaleMax = Button(text="GrayScaleMax", command=self.grayScaleMax_image)
		btnGrayScaleMax.pack(in_=self.frame, side=LEFT)


		lbl = Label(text="Ingresa un valor:")
		lbl.pack(in_=self.frameButtons1, side=LEFT)
		self.eFrame1 = Entry(width=3)
		self.eFrame1.insert(0, "0")
		self.eFrame1.pack(in_=self.frameButtons1, side=LEFT)

		btnBinaryScale = Button(text="BinaryScale", command=self.BinaryScale_image)
		btnBinaryScale.pack(in_=self.frameButtons1, side=LEFT)

		btnLightenImage = Button(text="Lighten", command=self.lighten_image)
		btnLightenImage.pack(in_=self.frameButtons1, side=LEFT)

		btnNegativeScale = Button(text="Negative", command=self.NegativeScale_image)
		btnNegativeScale.pack(in_=self.frameButtons2, side=LEFT)

	def load_image(self, image): # Method witch gonna help to load the images
		image = ImageTk.PhotoImage(image)
		self.panel = Label(image = image)
		self.panel.pict = image
		self.panel.pack()

	## Images Tools
	def original_image(self):
		self.panel.destroy()
		return self.load_image(Image.open(PATH_IMAGE))

	def grayScale_image(self):
		self.panel.destroy()
		return self.load_image(self.imageFilterapp.grayScale())

	def grayScaleMin_image(self):
		self.panel.destroy()
		return self.load_image(self.imageFilterapp.grayScaleMin())

	def grayScaleMax_image(self):
		self.panel.destroy()
		return self.load_image(self.imageFilterapp.grayScaleMax())

	def NegativeScale_image(self):
		self.panel.destroy()
		return self.load_image(self.imageFilterapp.negativeScale())

	def BinaryScale_image(self):
		self.panel.destroy()
		beta = self.eFrame1.get()
		return self.load_image(self.imageFilterapp.binaryScale(beta=beta))

	def lighten_image(self):
		self.panel.destroy()
		beta = self.eFrame1.get()
		return self.load_image(self.imageFilterapp.lightenImage(beta=beta))

if __name__ == '__main__':
	#app = VisionApp()
	img = Image.open('img/sample.png')
	bi = BaseImage(img)
	bi.grayScale()

	filtros = Filtros(bi.o_img) #mandamos la imagen de salida
	filtros.duplicarImage()
	filtros.salPimienta()

	filtros = Filtros(bi.o_img) #mandamos la imagen de salida
	filtros.media()
	filtros.mediana()
	filtros.moda()

	threshold = Threshold(bi.o_img)
	threshold.duplicarImage()
	threshold.threshold(16)
