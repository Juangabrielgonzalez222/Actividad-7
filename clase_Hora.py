class Hora():
    __hora=0
    __minutos=0
    __segundos=0
    def __init__(self,hora,minutos,segundos): 
        if((hora<24 and hora>-1)and (minutos<60 and minutos>-1) and(segundos<60 and segundos>-1)):
            self.__hora=hora
            self.__minutos=minutos
            self.__segundos=segundos
        else:
            print("Error en algun valor recordar rango horario ,hs:0-23,min=0-59,seg,0-59")
    def getHora(self):
        return self.__hora
    def getMinutos(self):
        return self.__minutos
    def getSegundos(self):
        return self.__segundos
    def Mostrar(self):
        print("{}:{}:{}".format(self.__hora, self.__minutos,self.__segundos))