8vo.Vision.Clase - Equipo
===================


Repositorio de la clase de Visión Computacional.
> **Nota:**
> - El proyecto está programado en python.
> - Para su mejor funcionamiento usar en un entorno Linux/Unix.
> - La visualización del resultado de las imágenes son guardadas en un directorio que más adelante es especificado y el programa muestra una imagen previa.
> - Todas las imágenes son pasadas primero a una conversión de escala de grises, para continuar de su proceso.
> - Si se quiere usar otra imagen, hay que guardar la imagen en la carpeta de img/ y poner como nombre sample

----------


Librerías
-------------

Para el correcto funcionamiento del proyecto, es necesario instalar las siguientes librerías:

- **[Tkinter:](https://wiki.python.org/moin/TkInter)** Entorno de GUI para su visualización,
- **[PIL:](http://www.pythonware.com/products/pil/)** Es la librería que usamos para el manipulado de imágenes.

Directorio del proyecto
------------
El directorio esta constituído de la siguiente manera:

```
|--8vo.Vision.Clase/
	|--bin/
	|--img/
	|--config.json
	|--main.py
```
####**bin**
Es el directorio donde tenemos alojado los scripts.
```
|--8vo.Vision.Clase/
	|--bin/
		|--__init__.py
		|--ImageFilter.py
	|--img/
	|--config.json
	|--main.py
```

- **__init__.py**: Archivo de inicialización.
- **ImageFilter.py**: Es la clase encargada de procesar las imagenes. 

####**img**
Es el directorio donde se tiene alojado las imágenes, tanto de entrada, como de salida.
```
|--8vo.Vision.Clase/
	|--bin/
	|--img/
		|--sample.png
		|--...
	|--config.json
	|--main.py
```

- **sample.png**: Es la imagen de ejemplo.

####**config.json**
Es un archivo de configuración, el cuál indica donde se guardarán las imágenes de entrada y de salida, tanto también algunas elementos globales, como la extensión de los archivos a usarse.
```json
{
	"config":{
		"image_properties":{
			"file_format": "PNG"
			},
		"path":{
			"image_source": "img/",
			"image_result": "img/"
		}
	}
}
```

####main.py
Es el encargado de ejecutar y mandar llamar las clases y librerías a emplearse. Aquí es donde se encuentra alojado la clase (**VisionApp**) que crea el entorno de GUI.
Los metodos importantes son:

 - **create_buttons**: Donde ponemos los botones para la interacción del GUI con la imagen. Ej:
```python
def create_buttons(self):
	btnGrayScale = Button(text="GrayScale", command=self.grayScale_image) #Nombre de nuestro botón y método a acceder
	btnGrayScale.pack(in_=self.frame, side=LEFT) #Posición de nuestro boton
```
 - **load_image**: Donde carga la imagen procesada en la ventana.
 - **Metodos de los botones**: Los cuáles son que mandan llamar a las funciones de la clase **ImageFilter** para el proceso de la imagen. Ej: 
```python
def grayScale_image(self):
		self.panel.destroy()  #Destrímos el panel anterior (imagen anterior)
		return self.load_image(self.imageFilterapp.grayScale()) #Cargamos la nueva imagen procesada
```

Ejecutar programa
------------
Para poder ejecutar el programa es necesario haber instalado las librerías anteriormente descritas, descargado el repositorio y ejecutar siguiente comando en terminal desde la raíz de nuestro proyecto.
```bash
$  cd 8vo.Vision.Clase/
$ ls
README.md   bin         config.json img         main.py
$ python main.py
```

Algoritmos o procesamientos importantes
--------------

Lo primero que hay que entender es lo siguiente, ya que a partir de ello, algúnos fragmentos del código se repiten
```python
def method(image):
	pixel = image.load() #Cargamos la imagen a una matris de pixeles
	w, h = image.size #Obtenemos las medidas de nuestra imaen
	
	for i in range(w):#Hacemos el recorrido de nuestra imagen para asi sacar los pixeles de ella
		for j in range(h):
			r = pixel[i,j][0] #Tomamos el rgb de nuestro pixel
			g = pixel[i,j][1]
			b = pixel[i,j][2]
	...
```

####grayScale
```python
def grayScale(image):
	pixel = image.load()
	w, h = image.size
	
	for i in range(w):
		for j in range(h):
			r = pixel[i,j][0]#Tomamos el rgb de nuestro pixel
			g = pixel[i,j][1]
			b = pixel[i,j][2]

			alpha = (r+g+b) / 3 # Sacamos la media de nuestro pixel para asi sacar la escla de grises
			pixel[i, j] = (alpha, alpha, alpha) #Asignamos nuevo valor
```

####grayScaleMax
```python
def grayScaleMax(image):
	pixel = image.load()
	w, h = image.size

	for i in range(w):
		for j in range(h):
			
			alpha = max(pixel[i,j]) #Obtenemos nuestro valor max del pixel en este caso será de nuestra escala rgb
			pixel[i, j] = (alpha, alpha, alpha)
```

####grayScaleMin
```python
def grayScaleMax(image):
	pixel = image.load()
	w, h = image.size

	for i in range(w):
		for j in range(h):
			
			alpha = min(pixel[i,j]) #Obtenemos nuestro valor min del pixel en este caso será de nuestra escala rgb
			pixel[i, j] = (alpha, alpha, alpha)
```

####binaryScale
```python
def binaryScale(image, beta):
	pixel = image.load()
	w, h = image.size
	umbral = int(beta)#Valor umbral que será para tomar cual será el limite para nuestra binarización

	for i in range(w):
		for j in range(h):
			r = pixel[i,j][0]
			g = pixel[i,j][1]
			b = pixel[i,j][2]

			alpha = (r+g+b) / 3 #Obtenemos escala de grises
			if alpha > umbral: #A partir de nuestro limite determinamos si es blanco o negro
				alpha = 255
			else:
				alpha = 0

			pixel[i, j] = (alpha, alpha, alpha)
```

####negativeScale
```python
def negativeScale(image):
	pixel = image.load()
	w, h = image.size

	for i in range(w):
		for j in range(h):
			r = pixel[i,j][0]
			g = pixel[i,j][1]
			b = pixel[i,j][2]

			alpha = (r+g+b) / 3 #Escala de grises
			alpha = 255 - alpha #Aplicamos fórmula donde a 255 le restamos nuestra alpha
			
			pixel[i, j] = (alpha, alpha, alpha)
```

####lightenImage
```python
def lightenImage(image,beta):
	image = Image.open(self.original_image)
	pixel = image.load()
	w, h = image.size
	beta=int(beta)
	for i in range(w):
		for j in range(h):
			r = pixel[i,j][0]
			g = pixel[i,j][1]
			b = pixel[i,j][2]

			alpha = (r+g+b) / 3 #Escala de grises
			alpha = alpha + beta #A partir de nuestro alpha le sumamos el valor de entrada que es el valor a aumentar
			pixel[i, j] = (alpha, alpha, alpha)
	#image = image.point(lambda p: p * beta) #Otra forma para aumentar el brillo con lambda
```
