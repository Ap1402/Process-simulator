from __future__ import division
from PyQt4 import QtGui
from PyQt4 import QtCore
import Mensaje
import sys
import interfaz  
import time
import random

colaProcesos=[]
memoriaRestante=0
memoriaTotal=0
quantum=None
mutex=QtCore.QMutex()
currentOpt=0

class Simulador(QtGui.QMainWindow,interfaz2.Ui_MainWindow):
    global colaProcesos
    def __init__(self,parent=None):
        super(Simulador,self).__init__(parent)
        self.setupUi(self)
        self.desactivar_procesofields()
        self.frameQuantum.show()
        self.frame.hide()
        self.TablaEstado.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.btnAgregar.clicked.connect(self.btnAgregarFuncion)
        self.btnBorrar.clicked.connect(self.borrarCampos)
        self.lockMemoria.clicked.connect(self.bloquearMemoria)
        self.btnEliminar.clicked.connect(self.eliminarEspecifico)
        self.btnEliminartodo.clicked.connect(self.eliminarTodo)
        self.comboAlgoritmo.currentIndexChanged.connect(self.algoritmoActualCambio)
        self.btnEstablecerQuantum.clicked.connect(self.establecerQuantum)
        self.btnRandom.clicked.connect(self.crearProcesoRandom)

        self.probando = relojlcd()
        self.btnIniciar.clicked.connect(self.probando.start)
        self.connect(self.probando,QtCore.SIGNAL("Comenzar"),self.actualizarReloj)

        self.inicio=probar()
        self.btnIniciar.clicked.connect(self.inicio.start)
        self.TablaEstado.connect(self.inicio,QtCore.SIGNAL("actualizarPorcentaje"),self.updateTablePercent)

    def agregarTabla(self,arrayDatos):
        global colaProcesos

        temp1 = arrayDatos
        prioridad=None
        if(temp1[3]!=None and temp1[3]!=""):
            prioridad=int(temp1[3])

        temp1[3] ="Preparado"
        temp1.append("0")
        rowPosition = self.TablaEstado.rowCount()
        columnNumber = self.TablaEstado.columnCount()
        self.TablaEstado.insertRow(rowPosition)

        ##----
        temp = Proceso()
        temp.setValues(temp1[0],temp1[1],temp1[2],rowPosition,prioridad)
        colaProcesos.append(temp)
        ##-----

        

        for i in range(columnNumber):
            if(i<3):
                self.TablaEstado.setItem(rowPosition ,i ,QtGui.QTableWidgetItem(str(temp1[i])))
            else:
                self.TablaEstado.setItem(rowPosition,i,QtGui.QTableWidgetItem(temp1[i]))
        self.borrarCampos()
        
    def obtenerDatosFields(self):
        memoriaP=self.fieldMemoriaP.text()
        memoriaP=int(memoriaP)
        rafaga = self.fieldRafaga.text()
        rafaga = int(rafaga)
        nombre = self.fieldNombre.text()
        prioridad = self.fieldPrioridad.text()
        datos = [nombre,rafaga,memoriaP,prioridad]

        return datos

    def btnAgregarFuncion(self):
        datos = self.obtenerDatosFields()
        self.agregarTabla(datos)

    def crearProcesoRandom(self):
        global memoriaRestante
        actual = self.comboAlgoritmo.currentIndex()
        relleno = [0,0,0,0]
        if(actual==3):
            relleno[0] = "P"+str(self.TablaEstado.rowCount()+1)
            relleno[1] = random.randint(3,20)
            relleno[2] = random.randint(1,memoriaRestante)
            relleno[3] = random.randint(1,9)
        else:
            relleno[0] = "P"+str(self.TablaEstado.rowCount()+1)
            relleno[1] = random.randint(3,20)
            relleno[2] = random.randint(1,memoriaRestante)
            relleno[3] = None

        self.agregarTabla(relleno)   

    def borrarCampos(self):
        self.fieldMemoriaP.setText("")   
        self.fieldNombre.setText("")   
        self.fieldPrioridad.setText("")   
        self.fieldRafaga.setText("")   

    def updateTablePercent(self,val,row):
        item=self.TablaEstado.item(row,4)
        item.setText(str(val))

    def bloquearMemoria(self):
        global memoriaRestante
        temp=self.fieldMemoria.text()
        if(self.TablaEstado.rowCount()==0):
            
            if(self.lockMemoria.isChecked()):
                if(temp!=""):
                    self.fieldMemoria.setDisabled(True)
                    self.desactivar_procesofields()
                    memoriaRestante=int(temp)
                else:
                    self.lockMemoria.setChecked(False)
                    self.mostrarMensaje("Debes agregar un valor a la memoria total")

            else:
                self.fieldMemoria.setDisabled(False)
                self.desactivar_procesofields()
        else:
            self.mostrarMensaje("Debes borrar todos los procesos agregados")
            self.lockMemoria.setChecked(True)

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
        Dialog = QtGui.QDialog()
        ui = Mensaje.Ui_Dialog()
        ui.setupUi(Dialog)
        ui.label.setText(text)
        Dialog.show()
        Dialog.exec_()

    def eliminarEspecifico(self):
        currentRow=self.TablaEstado.currentRow()
        colaProcesos.pop(currentRow)
        print(currentRow)
        self.TablaEstado.removeRow(currentRow)
    
    def eliminarTodo(self):
        colaProcesos=[]
        self.TablaEstado.setRowCount(0)
    
    def algoritmoActualCambio(self):
        global currentOpt
        currentOpt = self.comboAlgoritmo.currentIndex()
        if(currentOpt==0):
            self.frameQuantum.show()
            self.frame.hide()

        elif(currentOpt==3):
            self.frameQuantum.hide()
            self.frame.show()
            self.TablaEstado.setRowCount(0)

        else:
            self.frameQuantum.hide()
            self.frame.hide()

    def establecerQuantum(self):
        global quantum
        temp = self.fieldQuantum.text()
        if(temp!="" and temp>0 and  not self.btnEstablecerQuantum.isChecked()):
            quantum=int(temp)
            self.btnEstablecerQuantum.setChecked(True)
            print "establecido"
        else:
            print "no"

    def actualizarReloj(self,number):
        self.lcdTotal.display(number)


class relojlcd(QtCore.QThread):
    def __init__(self,parent=None):
        super(relojlcd,self).__init__(parent)
        self.n=0
    def run(self):
        while True:
            time.sleep(1)
            self.n+=1
            self.emit(QtCore.SIGNAL("Comenzar"),self.n)

class Proceso(QtCore.QThread):
    def __init__(self,parent=None):
        super(Proceso,self).__init__(parent)
        self.running=False
    def setValues(self,nombre,rafaga,memoria,fila,prioridad=None):
        self.nombre = nombre 
        self.rafaga = rafaga
        self.memoria = memoria
        self.prioridad=prioridad
        self.porcentaje = 0
        self.rafagaTotal=rafaga
        self.fila=fila
        self.rafagacont=0
        self.liberado=True
    def run(self):
        global memoriaRestante
        if(quantum==None):
            for n in range(self.rafaga):
                time.sleep(1)
                self.rafaga-=1
                self.rafagacont+=1
                self.porcentaje=self.calcularporcentaje()
                self.emit(QtCore.SIGNAL("datosporcent"),self.porcentaje,self.fila)

    def calcularporcentaje(self):
        return (int(self.rafagacont/self.rafagaTotal*100))


class probar(QtCore.QThread):
    def __init__(self,parent=None):
        super(probar,self).__init__(parent)   
    def run(self):
        global colaProcesos
        global memoriaRestante
        procesos=colaProcesos
        flag = True
        procesosliberados=0
        while flag:
            for n in procesos:
                if(memoriaRestante>=n.memoria and n.rafaga!=0 and n.isRunning()==False):
                    memoriaRestante-=n.memoria
                    print "Iniciando "+n.nombre
                    n.start()
                    n.liberado=False
                    self.connect(n,QtCore.SIGNAL("datosporcent"),self.enviarsignal)
                n.wait()
                print "Terminando "+n.nombre
                if(n.liberado==False):
                    print "prueba"                    
                    memoriaRestante+=n.memoria
                    n.liberado=True
                    procesosliberados+=1
                else:
                    continue
                if(procesosliberados!=len(procesos)):
                    flag=False
                    
        print "Terminado"

    def enviarsignal(self,porcentaje,row):
        self.emit(QtCore.SIGNAL("actualizarPorcentaje"),porcentaje,row)


        


if __name__=='__main__':
    a = QtGui.QApplication(sys.argv)
    app=Simulador()
    app.show()
    a.exec_()