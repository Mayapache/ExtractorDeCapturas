# -*- coding: utf-8 -*-
"""
@author: Mayapache

Este programa esta diseñado para automatizar acciones repetitivas en la computadora
Se toma captura de pantalla después de interaccionar con la pantalla y
posteriormente todas las capturas son guardadas en un documento pdf
(las coordenadas estan colocadas para el modo "pantalla completa" en la computadora
para la página de scribd y poder "descargar" virtualmente un documento de "solo lectura")
¡PirateⒶ y difunde!
"""

import pyscreenshot 
import mouse
import time
import random
Paginas=2  #Cantidad de páginas del documento/libro

#Posiciones x,y del mouse (a donde va a dar click)
x_click=1315 
y_click=360  


#Posiciones del cuadro del que se tomará la captura (para que sea solo una zona de la pantalla)
#Esquina superior izquierda
x1=96
y1=56
#Esquina inferior derecha
x2=1270
y2=680

#Tienes 6 segundos para poner el modo completo de la pantalla de libro a capturar!
time.sleep(6)


image = pyscreenshot.grab(bbox=(x1,y1,x2,y2)) #Primera imagen
im = image.convert('RGB')
imagelist = []

#Valores aleatorios intentando esquivar posible software de detección de copia

for i in range(Paginas):
    mouse.move(x_click+random.randrange(-7,13), y_click+random.randrange(-17,18), absolute=True, duration=random.randrange(1,10)/10)
    mouse.click('left')
    time.sleep(2) #Tiempo encontrado de carga de sig. página (variará despendiendo de tu conexión a internet)

    #Insertar verificacion
    image = pyscreenshot.grab(bbox=(x1,y1,x2,y2)) 
    im1 = image.convert('RGB')
    imagelist.append(im1)

im.save(r'C:\Users\Public\Documents\P_p.pdf',save_all=True, append_images=imagelist)
