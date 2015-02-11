import json
CONFIG_FILE = open('config.json')
data_json = json.load(CONFIG_FILE)
IMAGE_SOURCE = data_json['config']['path']['image_source']
IMAGE_RESULT = data_json['config']['path']['image_result']
IMAGE_FORMAT = data_json['config']['image_properties']['file_format']
CONFIG_FILE.close()

from PIL import Image

class ImageFilter(object):
	def __init__(self, image):
		self.original_image = image
		#self.original_image = Image.open(image)
		#self.original_image_pixel = self.original_image.load()

	def grayScale(self):
		image = Image.open(self.original_image)
		pixel = image.load()
		w, h = image.size
		
		for i in range(w):
			for j in range(h):
				r = pixel[i,j][0]
				g = pixel[i,j][1]
				b = pixel[i,j][2]

				alpha = (r+g+b) / 3
				pixel[i, j] = (alpha, alpha, alpha)
		image.save(IMAGE_RESULT+'grayScale.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)
		return image

	def grayScaleMax(self):
		image = Image.open(self.original_image)
		pixel = image.load()
		w, h = image.size

		for i in range(w):
			for j in range(h):
				
				alpha = max(pixel[i,j])
				pixel[i, j] = (alpha, alpha, alpha)
		image.save(IMAGE_RESULT+'grayScaleMax.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)
		return image

	def grayScaleMin(self):
		image = Image.open(self.original_image)
		pixel = image.load()
		w, h = image.size

		for i in range(w):
			for j in range(h):
				
				alpha = min(pixel[i,j])
				pixel[i, j] = (alpha, alpha, alpha)
		image.save(IMAGE_RESULT+'grayScaleMin.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)
		return image

	def binaryScale(self):
		image = Image.open(self.original_image)
		pixel = image.load()
		w, h = image.size
		umbral = 122

		for i in range(w):
			for j in range(h):
				r = pixel[i,j][0]
				g = pixel[i,j][1]
				b = pixel[i,j][2]

				alpha = (r+g+b) / 3
				if alpha > umbral:
					alpha = 255
				else:
					alpha = 0

				pixel[i, j] = (alpha, alpha, alpha)
		image.save(IMAGE_RESULT+'binaryScale.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)
		return image

	def negativeScale(self):
		image = Image.open(self.original_image)
		pixel = image.load()
		w, h = image.size

		for i in range(w):
			for j in range(h):
				r = pixel[i,j][0]
				g = pixel[i,j][1]
				b = pixel[i,j][2]

				alpha_r = 255 - r
				alpha_g = 255 - g
				alpha_b = 255 - b

				pixel[i, j] = (alpha_r, alpha_g, alpha_b)
		image.save(IMAGE_RESULT+'negativeScale.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)
		return image


	def lightenImage(self):
		image = Image.open(self.original_image)
		pixel = image.load()
		w, h = image.size
		
		for i in range(w):
			for j in range(h):
				r = pixel[i,j][0]
				g = pixel[i,j][1]
				b = pixel[i,j][2]

				alpha = (r+g+b) / 3
				pixel[i, j] = (alpha, alpha, alpha)
		image = image.point(lambda p: p * 10)
		image.save(IMAGE_RESULT+'lightenImage.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)
		return image
