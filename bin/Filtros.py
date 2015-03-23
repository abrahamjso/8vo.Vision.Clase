import json
CONFIG_FILE = open('config.json')
data_json = json.load(CONFIG_FILE)
IMAGE_SOURCE = data_json['config']['path']['image_source']
IMAGE_RESULT = data_json['config']['path']['image_result']
IMAGE_FORMAT = data_json['config']['image_properties']['file_format']
CONFIG_FILE.close()

from PIL import Image
from collections import Counter
import random

class ImageModel(object):
    def __init__(self, image):
        self.img = image
        self._pixels = self.img.load()
        self._w = self.img.size[0]
        self._h = self.img.size[1]
        self.o_img = Image.new(self.img.mode, self.img.size)
        self.o_pixels = self.o_img.load()

class BaseImage(ImageModel): #heredan del modelo
    def grayScale(self):
        for i in range(self._w):
            for j in range(self._h):
                r = self._pixels[i,j][0]
                g = self._pixels[i,j][1]
                b = self._pixels[i,j][2]
                alpha = (r+g+b) / 3
                self.o_pixels[i,j] = (alpha, alpha, alpha)
        self.o_img.save(IMAGE_RESULT+'grayScale.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)


PORCIENTO_RUIDO = 1.5 #porcentaje de ruido

class Filtros(ImageModel): #heredan del modelo
    def duplicarImage(self):
        for i in range(self._w):
            for j in range(self._h):
                r = self._pixels[i,j][0]
                g = self._pixels[i,j][1]
                b = self._pixels[i,j][2]
                alpha = (r+g+b) / 3
                self.o_pixels[i,j] = (alpha, alpha, alpha)

    def salPimienta(self):
        _p_total = (self._w * self._h) # sacamos el porcentaje de ruido a meter a la image
        num_ruido = int((_p_total * PORCIENTO_RUIDO) / 100) # Sacamos el num de pixeles que se le asignara ruido

        for x in range(num_ruido):
            _sp = 0 # Color a asignar por default asignamos blanco
            i = random.randrange(0, self._w) #Escogemos de manera aleatoria
            j = random.randrange(0, self._h) # nuestro pixel a meter ruido

            _r = bool(random.getrandbits(1)) # Escogemos el color a asignar de sal y pimienta
            if _r == False: # En caso que sea falso, asignamos negro
                _sp = 255
            self.o_pixels[i,j] = (_sp, _sp, _sp)
        self.o_img.save(IMAGE_RESULT+'SalPimienta.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)

    def get_vecinos(self, i,j): #obtenemos el pixel vecino
        _p_vecinos = []
        #vecinos directos
        try:
            _p_vecinos.append(self._pixels[i-1,j][0])
        except:
            pass
        try:
            _p_vecinos.append(self._pixels[i+1,j][0])
        except:
            pass
        try:
            _p_vecinos.append(self._pixels[i,j-1][0])
        except:
            pass
        try:
            _p_vecinos.append(self._pixels[i,j+1][0])
        except:
            pass

        #vecinos indirectos
        try:
            _p_vecinos.append(self._pixels[i-1,j-1][0])
        except:
            pass
        try:
            _p_vecinos.append(self._pixels[i+1,j+1][0])
        except:
            pass
        try:
            _p_vecinos.append(self._pixels[i-1,j+1][0])
        except:
            pass
        try:
            _p_vecinos.append(self._pixels[i+1,j-1][0])
        except:
            pass
        _p_vecinos.append(self._pixels[i,j][0]) #Agregamos nuestro pixel para tener la matrix de 9x9
        return _p_vecinos

    def media(self):
        for i in range(self._w):
            for j in range(self._h):
                _p_vecinos = self.get_vecinos(i,j) #obtenemos los pixeles vecinos
                media = sum(_p_vecinos) / len(_p_vecinos)
                self.o_pixels[i,j] = (media, media, media)
        self.o_img.save(IMAGE_RESULT+'Media.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)

    def mediana(self):
        for i in range(self._w):
            for j in range(self._h):
                _p_vecinos = self.get_vecinos(i,j) #obtenemos los pixeles vecinos
                _p_vecinos.sort() #ordenamos nuesta lista para sacar la mediana
                mediana = _p_vecinos[len(_p_vecinos)/2] # Tomamos el pixel medio
                self.o_pixels[i,j] = (mediana, mediana, mediana)
        self.o_img.save(IMAGE_RESULT+'Mediana.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)

    def moda(self):
        for i in range(self._w):
            for j in range(self._h):
                _p_vecinos = self.get_vecinos(i, j)
                moda = Counter(_p_vecinos) #Sacamos la moda, regresandonos la frecuencia con la que se repiten los elementos en la lista
                moda = moda.most_common(1) #Obtenemos el elemento mas comun, regresandonos una tupla
                self.o_pixels[i,j] = (moda[0][0], moda[0][0], moda[0][0])
        self.o_img.save(IMAGE_RESULT+'Moda.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)


class Threshold(ImageModel):
    def duplicarImage(self):
        for i in range(self._w):
            for j in range(self._h):
                r = self._pixels[i,j][0]
                g = self._pixels[i,j][1]
                b = self._pixels[i,j][2]
                alpha = (r+g+b) / 3
                self.o_pixels[i,j] = (alpha, alpha, alpha)

    def threshold(self, umbral=16):
        for i in range(self._w):
            for j in range(self._h):
                _p = self._pixels[i,j][0]
                for x in range(umbral):
                    if _p >= (umbral*x) and _p <= (umbral * (x+1)):
                        if ((umbral * (x+1)) / 2) >= _p:
                            _p = umbral * (x+1)
                        else:
                            _p = umbral * (x+2)
                self.o_pixels[i,j] = (_p, _p, _p)
        self.o_img.save(IMAGE_RESULT+'Threshold.'+IMAGE_FORMAT.lower(), IMAGE_FORMAT)


if __name__ == '__main__':
    img = Image.open('../img/sample.png')
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
