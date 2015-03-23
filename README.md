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
		|--__init__.py
		|--Filtros.py   //tarea 2
		|--ImageFilter.py //tarea 1
	|--img/
	|--config.json
	|--main.py
```

####**Referencias**
- [http://www.mathworks.com/help/images/](http://www.mathworks.com/help/images/)
- [http://homepages.inf.ed.ac.uk/rbf/HIPR2/median.htm](http://homepages.inf.ed.ac.uk/rbf/HIPR2/median.htm)
