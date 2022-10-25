# /*
#  * Reto #13
#  * FACTORIAL RECURSIVO
#  * Fecha publicación enunciado: 28/03/22
#  * Fecha publicación resolución: 04/04/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
#  */


from asyncio.windows_events import NULL

def factorial(number:int)->int:
    if(number<0):
        return NULL;

    if(number == 0):
        return 1;
    
    return factorial(number-1)*number;


print(factorial(10));

