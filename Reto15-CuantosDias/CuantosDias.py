#  *
#  * Reto #15
#  * ¿CUÁNTOS DÍAS?
#  * Fecha publicación enunciado: 11/04/22
#  * Fecha publicación resolución: 18/04/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
#  * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
#  * - La función recibirá dos String y retornará un Int.
#  * - La diferencia en días será absoluta (no importa el orden de las fechas).
#  * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
#  *

from ast import Try
from datetime import date, datetime
from numbers import Number
import re



mesDia = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
};

diaM = 86400000; #Milisegundos en un dia.
regex = r"^(?:3[01]|[12][0-9]|0?[1-9])([\-/. ])(0?[1-9]|1[0-2])\1\d{4}$"; #Regular expression to check the correct format of the string.


# Checks and transforms a string representing a date into an integer map.
def testString(date:str)->int:
    if(len(re.findall(regex,date)) < 1):
        raise Exception("Day Error: The String does not represent a Date")
    
    arrDate = re.split("/",date);
    day   = int(arrDate[0]);
    month = int(arrDate[1]);
    year  = int(arrDate[2]);
  
    intDate ={
        'day'  : day,
        'month': month,
        'year' : year    
    }
    
    return intDate;

#TODO: VER PORQUE NO ACEPTA MES 10
def daysBeteween(date1:str, date2:str)->int:
    d1 = testString(date1);
    d2 = testString(date2);
    a = datetime(d1['year'], d1['month'], d1['day']);
    b = datetime(d2['year'], d2['month'], d2['day']);
    c = abs(a-b);
    return c

print("ESTOS DIAS HAN PASADO");
print(daysBeteween("14/09/1984","27/10/2022"));


