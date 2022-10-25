#  *
#  * Reto #1
#  * ¿ES UN ANAGRAMA?
#  * Fecha publicación enunciado: 03/01/22
#  * Fecha publicación resolución: 10/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.

import string

word1 = "AARON";
word2 = "noraa";

def isAnagrama(word1:str, word2:str):
    
    if (word1.lower() == word2.lower()):
        return False;
    
    w1 = sorted(word1.lower());
    w2 = sorted(word2.lower());
    
    if (w1 == w2):
        return True;
    else:
        return False;
    

print(isAnagrama(word1, word2));

print(word1, word2);
