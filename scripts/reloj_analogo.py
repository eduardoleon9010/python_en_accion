"""
Este código en Python utiliza la biblioteca OpenGL para crear un reloj analógico 2D con una ventana gráfica interactiva. 
Aquí está lo que hace:

Importaciones de bibliotecas: Importa las bibliotecas necesarias de OpenGL (OpenGL.GL, OpenGL.GLUT, OpenGL.GLU) y datetime.

Inicialización de variables globales: Establece variables globales i, j, y k en 0.0.

Función initGL: Inicializa la ventana gráfica. Obtiene la hora actual y asigna los segundos, minutos y horas a i, j, y k 
respectivamente. Establece el color de fondo usando glClearColor.

Función disp: Esta función dibuja la interfaz gráfica del reloj. Usa comandos OpenGL para dibujar las manecillas del 
reloj (segundos, minutos y horas) y el marco del reloj.

Cada manecilla está representada como una línea con su respectivo color y tamaño, rotada según los segundos, minutos 
y horas obtenidos previamente.
También dibuja el contorno del reloj.
Función main: Inicializa la ventana GLUT, define su tamaño y título, llama a initGL para inicializar los gráficos, 
define disp como la función de renderizado y ejecuta el bucle principal de la interfaz gráfica con glutMainLoop.

Llamada a la función main: Inicia la ejecución del programa.

Este código crea una ventana gráfica utilizando OpenGL que muestra un reloj analógico 2D en tiempo real, 
donde las manecillas se actualizan cada segundo para reflejar la hora actual del sistema.


"""


import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *

from OpenGL.GLU import *
from datetime import datetime

i = 0.0
j = 0.0
k = 0.0

def initGL():
    global i
    global j
    global k
    glClearColor(0.0,0.1,0.0,0.1)
    now = datetime.now()
    sec = int(now.strftime("%S"))
    min = int(now.strftime("%M"))
    hr = int(now.strftime("%H"))
    i = -6 * sec
    j = -6 * min
    k = -30 * hr
    
def disp(id=0):
    global i
    global j
    global k
    glClear(GL_COLOR_BUFFER_BIT)
    glClearWidth(5.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.7)
    glVertex2f(0.0, 0.6)
    
    glVertex2f(0.38, 0.7)
    glVertex2f(0.34, 0.6)
    
    glVertex2f(-0.38, 0.7)
    glVertex2f(-0.34, 0.6)
    
    glVertex2f(-0,38, -0.7)
    glVertex2f(-0.34, -0.6)
    
    glVertex2f(0.7, 0.35)
    glVertex2f(0.6, 0.32)
    
    glVertex2f(0.7, -0.35)
    glVertex2f(0.6, -0.32)
   
    glVertex2f(-0.7, -0.35)
    glVertex2f(-0.6, -0.32)
   
    glVertex2f(0.7, 0.0)
    glVertex2f(0.6, 0.0)
   
    glVertex2f(0.0, -0.7)
    glVertex2f(0.0, -0.6)
   
    glVertex2f(0.38, -0.7)
    glVertex2f(0.34, -0.6)
   
    glVertex2f(-0.7, 0.0)
    glVertex2f(-0.6, 0.0)
   
    glEnd()
   
    glLoadIdentity()
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(0.7, 0.7) 
    
    glVertex2f(-0.7, 0.7)
    glVertex2f(-0.7, -0.7)
   
    glVertex2f(-0.7, -0.7)
    glVertex2f(0.7, -0.7)
   
    glVertex2f(0.7, -0.7)
    glVertex2f(0.7, 0.7)
   
   
    glVertex2f(0.75, 0.75)
    glVertex2f(-0.75, 0.75)
   
    glVertex2f(-0.75, 0.75)
    glVertex2f(-0.75, -0.75)
   
    glVertex2f(-0.75, -0.75)
    glVertex2f(0.75, -0.75)
   
    glVertex2f(0.75, -0.75)
    glVertex2f(0.75, 0.75)
   
    glEnd()
   
    glPushMatrix()
    glRotatef(i, 0.0, 0.0, 0.1) 
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  # segundos
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 0.6)
   
    glEnd()
    glPopMatrix()
   
    glPushMatrix()
    glRotatef(j, 0.0, 0.0, 0.1)
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0) # minutos
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 0.5)
   
    glEnd()
    glPopMatrix()
  
    glPushMatrix()
    glRotatef(k, 0.0, 0.0, 0.1)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 0.0) # horas
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 0.3)
   
    glEnd()
    glPopMatrix()
    i -= 6
    if i <= -360:
       if j <= -360:
          k -= 5.0
          i = 0.0
          j = 0.0
       else:
          j -= 6.0
          i = 0.0
    glutTimerFunc(1000, disp, 0)
    glutSwapBuffers()
   
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow("Reloj 2D")
    initGL()
    glutDisplayFunc(disp)
    glutMainLoop()
   
main()
