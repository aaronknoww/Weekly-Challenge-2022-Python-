#  *
#  * Reto #19
#  * CONVERSOR TIEMPO
#  * Fecha publicación enunciado: 09/05/22
#  * Fecha publicación resolución: 16/05/22
#  * Dificultad: FACIL
#  *
#  * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
#  *
#  *


diaM = 86400000; #Milisegundos en un día.
horaM = diaM/24;
minutosM = horaM/60;

def dateToMilliseconds( dias:int, horas:int, minutos:int, segundos:int )->int:
    return dias*diaM + horas*horaM + minutos*minutosM + segundos*1000;


print(dateToMilliseconds(1,1,1,1));
    