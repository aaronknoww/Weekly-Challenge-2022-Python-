# /*
# * Reto #14
# * ¿ES UN NÚMERO DE ARMSTRONG?
# * Fecha publicación enunciado: 04/04/22
# * Fecha publicación resolución: 11/04/22
# * Dificultad: FÁCIL
# *
# * Enunciado: Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
# * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
# *  Un número es de Armstrong es la suma de los dígitos que lo componen al cubo (por ser 3 digitos) a la 4ta (si son 4) es igual al número.
# *  Por ejemplo el 153, ya que 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# */



import math


def isArmstrong(number:int)->bool:
    aux = number;
    digits = [];
    sum = 0;
    pot = 0;

    while (True):
        digits.append(aux%10);
        aux = math.trunc(aux/10);
        if(aux==0):
            break;

    pot = len(digits);
    
    for d in digits:
        sum += math.pow(d,pot);
    
    if(sum == number):
        return True;
    else:
        return False;


print(isArmstrong(153));
print(isArmstrong(8208));    



