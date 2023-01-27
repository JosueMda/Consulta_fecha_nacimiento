#Funcion que dice la edad de acuerdo al año y mes de nacimiento

from datetime import  datetime                        #--------> Importamos datos de libreria
def main():
  ano_nac=int(input("ingrese su año de nacimiento: "))
  mes_nac=int(input("ingrese su mes de nacimiento: "))
  dia_nac=int(input("ingrese su dia de nacimiento: "))

  edad=calcularEdad (ano_nac,mes_nac,dia_nac)

  print (f"Usted tiene {edad} años".center(50,"*")) # ----->   .center centra el texto
def calcularEdad (ano,mes,dia):
  d=datetime.now()   #--------> Toma valores de la computadora  con .now()
  anoActual=d.year
  mesactual=d.month
  diaactual=d.day
  if mes <= mesactual and dia < diaactual:
    edad=(anoActual) - ano
  elif mes < mesactual:
    edad=(anoActual) - ano
  else:
    edad=(anoActual-1)-ano
  return edad#.... Para que devuelva algo


if __name__=="__main__":
  main()   