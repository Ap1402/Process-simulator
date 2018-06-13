from Clase_Proceso import Proceso
from logica import Simulador
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threading
import time

##---------------------
ui = Simulador()
app =QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui.iniciarSimulador(MainWindow)

##--------------------


memoriaRestante=4000    
prueba= []
def correr(self,lock):
    global memoriaRestante
    global prueba
    n=0
    for i in prueba:
        while(memoriaRestante>=i.memoria and i.rafaga!=0 and i.running==False):
            lock.acquire()
            memoriaRestante-=i.memoria
            i.running=True
            lock.release()
            ##i.start()
            i.ejecutar_proceso()
            ##ui.actualizarPorcentaje(i)
            lock.acquire()
            memoriaRestante+=i.memoria
            lock.release()

def prueba_btn():
    global prueba
    prueba = ui.leerDatos_tabla()
    lock=threading.Lock()
    t=[]
    flag = True
    for n in range(len(prueba)):
        t.append(threading.Thread(target=correr,args=(prueba,lock)))
    for n in range(len(prueba)):
        t[n].start()
    

ui.btnIniciar.clicked.connect(prueba_btn)

MainWindow.show()
sys.exit(app.exec_())








