#  *
#  * Reto #6
#  * INVIRTIENDO CADENAS
#  * Fecha publicación enunciado: 07/02/22
#  * Fecha publicación resolución: 14/02/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


cad = "Hola Aaron Knoww";
#cad.__len__

print(len(cad));

def reverseString(word:str) -> str:
    reverse = "";
    for w in word:
        reverse = w + reverse;
    print(reverse);

reverseString(cad);
reverseString("Python 3.10")







