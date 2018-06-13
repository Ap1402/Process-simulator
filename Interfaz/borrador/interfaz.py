# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 571)
        font.setUnderline(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ## Field nombre
        self.NombreF = QtWidgets.QLineEdit(self.centralwidget)
        self.NombreF.setGeometry(QtCore.QRect(310, 130, 121, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.NombreF.setFont(font)
        self.NombreF.setObjectName("NombreF")
        ## End nombre

        ## Field Quantum
        self.QuantumF = QtWidgets.QLineEdit(self.centralwidget)
        self.QuantumF.setGeometry(QtCore.QRect(490, 130, 113, 29))
        font = QtGui.QFont()
        self.QuantumF.setFont(font)
        self.QuantumF.setValidator(QtGui.QIntValidator())
        self.QuantumF.setObjectName("QuantumF")
        #End Field

        ## Field Rafaga 
        self.RafagaF = QtWidgets.QLineEdit(self.centralwidget)
        self.RafagaF.setGeometry(QtCore.QRect(650, 130, 113, 29))
        self.RafagaF.setFont(font)
        self.RafagaF.setValidator(QtGui.QIntValidator())
        self.RafagaF.setObjectName("RafagaF")
        ##--End rafaga

        self.AlgoritmoCombo = QtWidgets.QComboBox(self.centralwidget)
        self.AlgoritmoCombo.setGeometry(QtCore.QRect(50, 130, 161, 20))
        self.AlgoritmoCombo.setObjectName("AlgoritmoCombo")
        self.AlgoritmoCombo.addItem("")
        self.AlgoritmoCombo.addItem("")
        self.AlgoritmoCombo.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 16, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 40, 111, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 100, 54, 17))
        self.label_4.setObjectName("label_4")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 100, 61, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(680, 100, 54, 17))
        self.label_6.setObjectName("label_6")

        ## Tabla 
        self.TablaEstado = QtWidgets.QTableWidget(self.centralwidget)
        self.TablaEstado.setGeometry(QtCore.QRect(150, 210, 511, 171))
        self.TablaEstado.setColumnCount(5)
        self.TablaEstado.setObjectName("TablaEstado")
        self.TablaEstado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaEstado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaEstado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEstado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEstado.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEstado.setHorizontalHeaderItem(4, item)
        ## End Tabla

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulador de procesos"))
        self.AlgoritmoCombo.setItemText(0, _translate("MainWindow", "Round-Robin"))
        self.AlgoritmoCombo.setItemText(1, _translate("MainWindow", "Shortest Job First"))
        self.AlgoritmoCombo.setItemText(2, _translate("MainWindow", "First-Come First-Served"))
        self.label.setText(_translate("MainWindow", "Simulador de Procesos"))
        self.label_2.setText(_translate("MainWindow", "Algoritmo de Planificacion"))
        self.label_3.setText(_translate("MainWindow", "Datos del proceso"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.label_5.setText(_translate("MainWindow", "Quantum"))
        self.label_6.setText(_translate("MainWindow", "Rafaga"))
        item = self.TablaEstado.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.TablaEstado.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rafaga"))
        item = self.TablaEstado.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantum"))
        item = self.TablaEstado.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Estado"))
        item = self.TablaEstado.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Porcentaje %"))


##if __name__ == "__main__":
  ##  import sys
    ##app = QtWidgets.QApplication(sys.argv)
    ##MainWindow = QtWidgets.QMainWindow()
    ##ui = Ui_MainWindow()
    ##ui.setupUi(MainWindow)
    ##MainWindow.show()
    ##sys.exit(app.exec_())

