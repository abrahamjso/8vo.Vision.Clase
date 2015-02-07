8vo.Vision.Clase
===================


Repositorio de la clase de Visión Computacional.
> **Nota:**
> - El proyecto está programado en python.
> - Para su mejor funcionamiento usar en un entorno Linux/Unix.

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
- **ImageFilter.py**: Es la clase encargada de procesar las imagenes. Para crear un nuevo método que haga otro tipo de procesamiento se hace lo siguiente:
```python
class ImageFilter(object):
	def __init__(self, image):
		self.original_image = image
	
	...
	def nombre_metodo(self):
		#codigo del proceso de la imagen
		return image # Regresamos la imagen procesada para mostrarla en la ventana
	...
```

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
 - **Metodos de los botones**: Los cuáles son que mandan llamar a la clase **ImageFilter** para el proceso de la imagen. Ej: 
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
