#  * Reto #8
#  * DECIMAL A BINARIO
#  * Fecha publicación enunciado: 18/02/22
#  * Fecha publicación resolución: 02/03/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.



def decimalToBinary(number:int)->str:
    if(number==0):
        return 0;
    binary = "";
    while (number > 0):
        binary = str(number%2)+binary;
        number = int(number/2);
    
    return binary;

print(decimalToBinary(15));
