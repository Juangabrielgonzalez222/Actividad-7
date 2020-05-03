from clase_FechaHora import FechaHora
from clase_Hora import Hora
if __name__ == '__main__':
   d = int(input("Ingrese Dia: "))

   mes = int(input("Ingrese Mes: "))

   a = int(input("Ingrese Año: "))

   h = int(input("Ingrese Hora: "))

   m = int(input("Ingrese Minutos: "))

   s = int(input("Ingrese Segundos: "))

   f = FechaHora(d,mes,a,h, m, s)
   f.Mostrar()
   h1 = int(input("Ingrese Hora de r: "))

   m1 = int(input("Ingrese Minutos de r: "))

   s1 = int(input("Ingrese Segundos de r: "))

   r = Hora(h1, m1, s1)
   r.Mostrar()
   print("Suma de f + r: ")

   f2 = f + r

   f2.Mostrar()

   print("Suma de r + f: ")

   f3 = r + f

   f3.Mostrar()

   dias=int(input("Ingrese la cantidad de dias a restar a f3:"))

   f4 = f3 - dias # Al restar un número entero a un objeto FechaHora se debe restar la cantidad de

                   # días indicada por el número entero

   f4.Mostrar()
   dias=int(input("Ingrese la cantidad de dias a sumar a f2:"))
   f4 = dias + f2 # suma un día a un objeto FechaHora
   f4.Mostrar() 