from PyQt5 import QtCore,QtWidgets,QtGui

class MyThread(QtCore.QThread):
    updated = QtCore.pyqtSignal(str)

    def run( self ):
        # do some functionality
        for i in range(10000):
            self.updated.emit(str(i))

class Windows(QtGui.QWidget):
    def __init__( self, parent = None ):
        super(Windows, self).__init__(parent)

        self._thread = MyThread(self)
        self._thread.updated.connect(self.updateText)

        # create a line edit and a button

        self._button.clicked.connect(self._thread.start)

    def updateText( self, text ):
        self.widget.setText(text)