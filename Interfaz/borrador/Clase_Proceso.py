import threading
import time


class Proceso():
    def __init__(self,nombre,rafaga,memoria,prioridad=None):
        ##threading.Thread.__init__(self)
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