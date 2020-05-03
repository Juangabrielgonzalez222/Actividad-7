class FechaHora():
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __minutos=0
    __segundos=0
    def __init__(self,dia=1,mes=1,año=2020,hora=0,minutos=0,segundos=0):
        if((hora<24 and hora>-1)and (minutos<60 and minutos>-1) and(segundos<60 and segundos>-1) and (mes>0 and mes<13)):
            if ((año%400==0)or(año%100!=0 and año%4==0)):
                listameses=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                listameses=[31,28,31,30,31,30,31,31,30,31,30,31]
            if(dia<=listameses[mes-1] and dia>0):     
                self.__dia=dia
                self.__mes=mes
                self.__año=año
                self.__hora=hora
                self.__minutos=minutos
                self.__segundos=segundos
            else:
                print("dia incorrecto el rango segun el mes ingresado {} es entre:1-{}".format(mes,listameses[mes-1]))
        else:
            print("verifique valor de hora 0-23,minutos 0-59,segundos 0-59 y mes 1-12")
    def Mostrar(self):
        print("{}/{}/{} {}:{}:{}".format(self.__dia, self.__mes,self.__año,self.__hora, self.__minutos,self.__segundos))
    def __add__(self,nuevo):
        dia=self.__dia
        mes=self.__mes
        año=self.__año
        hora=self.__hora
        minutos=self.__minutos
        segundos=self.__segundos
        if ((self.__año%400==0)or (self.__año%100!=0 and self.__año%4==0)):
            listameses=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listameses=[31,28,31,30,31,30,31,31,30,31,30,31]
        
        if(type(nuevo)==int):
            if (nuevo>-1):
                dia+=nuevo
                while(dia>listameses[mes-1]):
                    dia-=listameses[mes-1]
                    if(mes==12):
                        mes=1
                        año+=1
                    else:
                        mes+=1
            else:
                print("Ingresar un valor positivo o utilizar función resta")
        else:
            hora+=nuevo.getHora()
            minutos+=nuevo.getMinutos()
            segundos+=nuevo.getSegundos()
            if segundos>59:
                segundos-=60
                minutos+=1
            if minutos>59:
                minutos-=60
                hora+=1
            if hora>23:
                hora-=24
                dia+=1
            if dia>listameses[mes-1]:
                dia-=listameses[mes-1]
                mes+=1
            if mes>12:
                mes-=12
                año+=1
            return FechaHora(dia,mes,año,hora,minutos,segundos)
    def __radd__(self,nuevo):
        dia=self.__dia
        mes=self.__mes
        año=self.__año
        hora=self.__hora
        minutos=self.__minutos
        segundos=self.__segundos
        if ((self.__año%400==0)or (self.__año%100!=0 and self.__año%4==0)):
            listameses=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listameses=[31,28,31,30,31,30,31,31,30,31,30,31]
        
        if(type(nuevo)==int):
            if (nuevo>-1):
                dia+=nuevo
                while(dia>listameses[mes-1]):
                    dia-=listameses[mes-1]
                    if(mes==12):
                        mes=1
                        año+=1
                    else:
                        mes+=1
            else:
                print("Ingresar un valor positivo no se admiten negativos")
        else:
            hora+=nuevo.getHora()
            minutos+=nuevo.getMinutos()
            segundos+=nuevo.getSegundos()
            if segundos>59:
                segundos-=60
                minutos+=1
            if minutos>59:
                minutos-=60
                hora+=1
            if hora>23:
                hora-=24
                dia+=1
            if dia>listameses[mes-1]:
                dia-=listameses[mes-1]
                mes+=1
            if mes>12:
                mes-=12
                año+=1
        return FechaHora(dia,mes,año,hora,minutos,segundos)
    def __sub__(self,dia):
        if ((self.__año%400==0)or (self.__año%100!=0 and self.__año%4==0)):
            listameses=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            listameses=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(type(dia)==int):
            if (dia>-1):        
                dia2=self.__dia
                mes=self.__mes
                año=self.__año
                dia2-=dia
                while(dia2<1):
                    if(mes==1):
                        dia2+=31
                        mes=12
                        año-=1
                    else:
                        dia2+=listameses[mes-2]
                        mes-=1
                return FechaHora(dia2,mes,año,self.__hora,self.__minutos,self.__segundos)    
            else:
                print("Dia debe ser positivo, no se admiten negativos")
    def Test(self):
        print("test funciones")
        
        self.Mostrar()
            