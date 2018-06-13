import interfaz2 as i2
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
from Mensaje.Mensaje import Ui_Dialog
import threading
import time

prueba =[]


class Simulador(i2.Ui_MainWindow):
    
    def iniciarSimulador(self,MainWindow):
        super().setupUi(MainWindow)
        self.desactivar_procesofields()
        self.frameQuantum.show()
        self.frame.hide()
        self.TablaEstado.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.comboAlgoritmo.currentIndexChanged.connect(self.algoritmoActualCambio)
        self.btnBorrar.clicked.connect(self.borrarDatos)
        self.btnEliminartodo.clicked.connect(self.eliminarTodo)
        self.btnEliminar.clicked.connect(self.eliminarEspecifico)
        self.lockMemoria.clicked.connect(self.bloquearMemoria)
        self.btnAgregar.clicked.connect(self.funcagregarboton)
        self.btnRandom.clicked.connect(self.generarRandom)

        self.memoriaTotal=0

    def borrarDatos(self):
        self.fieldNombre.setText("")
        self.fieldMemoriaP.setText("")
        self.fieldPrioridad.setText("")
        self.fieldRafaga.setText("")

    def eliminarTodo(self):
        self.TablaEstado.setRowCount(0)

    def eliminarEspecifico(self):
        print(self.TablaEstado.currentRow())
        self.TablaEstado.removeRow(self.TablaEstado.currentRow())
    
    def algoritmoActualCambio(self):
        currentOpt = self.comboAlgoritmo.currentIndex()
        if(currentOpt==0):
            self.frameQuantum.show()
            self.frame.hide()
            if(self.TablaEstado.columnCount()>5):
                self.TablaEstado.removeColumn(self.TablaEstado.columnCount()-3)

        elif(currentOpt==3):
            self.frameQuantum.hide()
            self.frame.show()
            self.TablaEstado.setRowCount(0)
            self.TablaEstado.insertColumn(self.TablaEstado.columnCount()-2)
            self.TablaEstado.setHorizontalHeaderItem(3,QtWidgets.QTableWidgetItem("Prioridad"))
        else:
            self.frameQuantum.hide()
            self.frame.hide()
            if(self.TablaEstado.columnCount()>5):
                self.TablaEstado.removeColumn(self.TablaEstado.columnCount()-3)

    def bloquearMemoria(self):
        if(self.TablaEstado.rowCount()==0):
            
            if(self.lockMemoria.isChecked()):
                if(self.fieldMemoria.text()!=""):
                    self.fieldMemoria.setDisabled(True)
                    self.desactivar_procesofields()
                    self.memoriaTotal=int(self.fieldMemoria.text())
                    global memoriaRestante
                    memoriaRestante=self.memoriaTotal
                else:
                    self.lockMemoria.setChecked(False)
                    self.mostrarMensaje("Debes agregar un valor a la memoria total")

            else:
                self.fieldMemoria.setDisabled(False)
                self.desactivar_procesofields()
        else:
            self.mostrarMensaje("Debes borrar todos los procesos agregados")
            self.lockMemoria.setChecked(True)

    def camposLlenados(self):
        camposLlenos = {}
        if(self.fieldMemoriaP.text()!=""):
            camposLlenos["Memoria"]=self.fieldMemoriaP.text()

        if(self.fieldNombre.text()!=""):
            camposLlenos["Nombre"]=self.fieldNombre.text()

        if(self.fieldRafaga.text()!=""):
            camposLlenos["Rafaga"]=self.fieldRafaga.text()

        if((self.fieldPrioridad.text()!="") and (self.comboAlgoritmo.currentIndex()==3)):
            camposLlenos["Prioridad"]=self.fieldPrioridad.text()

        return camposLlenos
    
    def funcagregarboton(self):
        if(self.memoriaTotal>=int(self.fieldMemoriaP.text())):
            self.agregarProcesoTabla(self.camposLlenados())
        else:
            print("El proceso excede las especificaciones del computador")
            print(self.memoriaTotal)

    def agregarProcesoTabla(self,rellenados):

        if(not("Prioridad" in rellenados.keys())):
            indicededatos = ["Nombre","Rafaga","Memoria","Preparado","0"]

            rowposition = self.TablaEstado.rowCount()

            self.TablaEstado.insertRow(rowposition)

            for i in range(5):
                if(i<3):
                    self.TablaEstado.setItem(rowposition, i , QtWidgets.QTableWidgetItem(rellenados[indicededatos[i]]))
                else:
                    self.TablaEstado.setItem(rowposition, i , QtWidgets.QTableWidgetItem(indicededatos[i]))       
        else:
            indicededatos = ["Nombre","Rafaga","Memoria","Prioridad", "Preparado","0"] 

            rowposition = self.TablaEstado.rowCount()

            self.TablaEstado.insertRow(rowposition)

            for i in range(6):
                if(i<4):
                    self.TablaEstado.setItem(rowposition, i , QtWidgets.QTableWidgetItem(rellenados[indicededatos[i]]))
                else:
                    self.TablaEstado.setItem(rowposition, i , QtWidgets.QTableWidgetItem(indicededatos[i]))   

    def generarRandom(self):
        actual = self.comboAlgoritmo.currentIndex()
        relleno = {}
        if(actual==3):
            relleno["Nombre"] = "P"+str(self.TablaEstado.rowCount()+1)
            relleno["Rafaga"] = str(randint(3,20))
            relleno["Memoria"] = str(randint(1,self.memoriaTotal))
            relleno["Prioridad"] = str(randint(1,9))
        else:
            relleno["Nombre"] = "P"+str(self.TablaEstado.rowCount()+1)
            relleno["Rafaga"] = str(randint(3,20))
            relleno["Memoria"] = str(randint(1,self.memoriaTotal))
        self.agregarProcesoTabla(relleno)            

    def leerDatos_tabla(self):
        rowNumber = self.TablaEstado.rowCount()
        columnNumber = self.TablaEstado.columnCount()
        datos = []
        diccionario = {"Nombre":"","Rafaga":0,"Memoria":0,"Prioridad":None}
        etiquetas = ["Nombre","Rafaga","Memoria","Prioridad"]

        for i in range(rowNumber):
            for j in range(columnNumber-2):
                try:
                    temp=self.TablaEstado.item(i,j)
                    temp=int(temp.text())
                except:
                    temp=temp.text()
                diccionario[etiquetas[j]]=temp
            datos.append(Proceso(diccionario[etiquetas[0]],diccionario[etiquetas[1]],diccionario[etiquetas[2]],diccionario[etiquetas[3]]))
            Proceso.fila=i
        return datos

    def desactivar_procesofields(self):
        if(self.fieldMemoria.isEnabled()):
            self.fieldMemoriaP.setDisabled(True)
            self.fieldNombre.setDisabled(True)
            self.fieldRafaga.setDisabled(True)
            self.fieldPrioridad.setDisabled(True)
            self.btnAgregar.setDisabled(True)
            self.btnBorrar.setDisabled(True)
            self.btnRandom.setDisabled(True)
        else:
            self.fieldMemoriaP.setDisabled(False)
            self.fieldNombre.setDisabled(False)
            self.fieldRafaga.setDisabled(False)
            self.fieldPrioridad.setDisabled(False)
            self.btnAgregar.setDisabled(False)
            self.btnBorrar.setDisabled(False)
            self.btnRandom.setDisabled(False)
    
    def mostrarMensaje(self,text):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.label.setText(text)
        Dialog.show()
        Dialog.exec_()
                    
    def actualizarPorcentaje(self,row,column,porcentaje):
        temp=self.TablaEstado.item(row,column)
        temp.setText(porcentaje)


##---------------------
ui = Simulador()
app =QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui.iniciarSimulador(MainWindow)

##--------------------
mutex = QtCore.QMutex()

class Proceso(QtCore.QThread):
    actualizar = QtCore.pyqtSignal(int,int,int)
    def __init__(self,nombre,rafaga,memoria,prioridad=None):
        super(QtLock, self).__init__()
        self.fila=0
        self.nombre=nombre
        self.rafaga=rafaga
        self.memoria=memoria
        self.running=False
        self.Estado="En espera"
        self.rafagatotal=rafaga
        self.rafagacont=0

        if(prioridad!=None):
            self.prioridad=prioridad

    def tienePrioridad(self):
        if(self.prioridad!=None):
            return True
        else:
            return False

    def ejecutar_proceso(self,quantum=None):
        if(quantum!=None):
            for n in range(quantum):
                time.sleep(0.5)
                print(self.nombre ,self.rafaga)
                if(self.rafaga==quantum): 
                    break
                self.rafaga-=1
                self.rafagacont+=1
            self.running=False

        else:
            for n in range(self.rafaga):
                time.sleep(0.5)
                self.rafaga-=1
                self.rafagacont+=1
                print(self.nombre, self.calcular_porcentaje(),"%")
            self.running=False

    def calcular_porcentaje(self):
        return str(int(self.rafagacont/self.rafagatotal*100))


class MyThread(QtCore.QThread):
    updated = QtCore.pyqtSignal(str)

    def run( self ):
        # do some functionality
        for i in range(10000):
            self.updated.emit(str(i))

class correr(self,lock):
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
            ui.actualizarPorcentaje(i.fila,3,i.calcular_porcentaje())
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