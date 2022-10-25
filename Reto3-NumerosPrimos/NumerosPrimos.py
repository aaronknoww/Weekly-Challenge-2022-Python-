#  *
#  * Reto #3
#  * ¿ES UN NÚMERO PRIMO?
#  * Fecha publicación enunciado: 17/01/22
#  * Fecha publicación resolución: 24/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  *

from ast import Return
import math

n= 9;
print(math.sqrt(n));
print(math.isqrt(n)); 

# Funcition to know if squer root return a number with out decimals.
def sqrIsExact(n):
    if(math.sqrt(n) > math.isqrt(n)):
        return False;
    else:
        return True;

# This Function return true if is prime.

def isPrime(number)->bool:
    if(number<2):
        return False;


    if((number==2) or (number==3) or ( number==5) or (number==7)):
        return True;
        
    if (sqrIsExact(number)):
        return False; 
    
    if((number%2) and (number%3) and ( number%5) and (number%7) !=0):
       return True;
    
    return False;

prime =[];

for n in range(101):
    if(isPrime(n)):
        prime.append(n);

print(prime)
