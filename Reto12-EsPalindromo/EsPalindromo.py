# /*
#  * Reto #12
#  * ¿ES UN PALÍNDROMO?
#  * Fecha publicación enunciado: 21/03/22
#  * Fecha publicación resolución: 28/03/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
#  * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
#  * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#  * Ejemplo: Ana lleva al oso la avellana.
#  */

import re


reEraseSpace = r"\s";

def isPalindrome(text:str)->bool:

    result = re.sub(reEraseSpace,"", text.lower(),0, re.MULTILINE);

    for ch in range(len(result)):
        if(result[ch]!=result[len(result)-ch-1]):
            return False;
    
    return True;


frase = "ana lleva al     oso la avellana";
print(isPalindrome(frase));

