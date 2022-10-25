#  *
#  * Reto #11
#  * ELIMINANDO CARACTERES
#  * Fecha publicación enunciado: 14/03/22
#  * Fecha publicación resolución: 21/03/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
#  *


def deleteCharcters(str1:str, str2:str):
    out1="";
    out2="";
    aux1 = str1.lower();
    aux2 = str2.lower();

    aux1 = sorted(aux1);
    aux2 = sorted(aux2);

    for chr in aux1 :
        if(aux2.count(chr) == 0):
            out1 += chr;
    
    for chr in aux2 :
        if(aux1.count(chr)== 0):
            out2 += chr;
    
    print("out1: "+ out1);
    print("out2: "+ out2);
    return;

str1 = "abcdabc";
str2 = "cd19er";

deleteCharcters(str1, str2);

