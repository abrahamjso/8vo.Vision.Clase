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

	def binaryScale(self, beta=0):
		image = Image.open(self.original_image)
		pixel = image.load()
		w, h = image.size
		umbral = int(beta)

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

				alpha = (r+g+b) / 3
				alpha = 255 - alpha
				
				pixel[i, j] = (alpha, alpha, alpha)
		image.save(IMAGE_RESULT+'negativeScale.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)
		return image


	def lightenImage(self,beta=0):
		image = Image.open(self.original_image)
		pixel = image.load()
		w, h = image.size
		beta=int(beta)
		for i in range(w):
			for j in range(h):
				r = pixel[i,j][0]
				g = pixel[i,j][1]
				b = pixel[i,j][2]

				alpha = (r+g+b) / 3
				alpha = alpha + beta
				pixel[i, j] = (alpha, alpha, alpha)
		#image = image.point(lambda p: p * beta)
		image.save(IMAGE_RESULT+'lightenImage.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)
		return image

	def duplicate(self):
		image = Image.open(self.original_image)
		pixel = image.load()
		w, h = image.size

		image_2 = Image.new( 'RGB', (w,h), "black") # create a new black image
		pixel_2 = image_2.load() # create the pixel map

		for i in range(w):
			for j in range(h):
				r = pixel[i,j][0]
				g = pixel[i,j][1]
				b = pixel[i,j][2]

				alpha = (r+g+b) / 3
				pixel_2[i, j] = (alpha, alpha, alpha)
		image_2.save(IMAGE_RESULT+'duplicateImage.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)
		return image_2

