#  *
#  * Reto #16
#  * EN MAYÚSCULA
#  * Fecha publicación enunciado: 18/04/22
#  * Fecha publicación resolución: 25/04/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
#  *


from logging import raiseExceptions
import re


reEraseSpace = r"\s{2,}";
reEraseEnters = r"\n";
reMorse = r"^[-.\s/]+$";
regex = r"^[a-zA-Z,. ]+$";
justLetters = r"^[a-zA-Z]+$";


def capitalize(text:str)->str:
    if(len(re.findall(regex, text)) < 1):
        raise Exception("String Error");
    
    result   = re.sub(reEraseSpace,"", text, re.MULTILINE);
    wordList = re.split(' ', result);
    
    
    result = "";
    for word in wordList:
        if(len(re.findall(justLetters, word[0])) > 0):               
            result += word.title()+" ";
        else:
            for i in range(1, len(word)):
                if(len(re.findall(justLetters,word[i])) > 0 ):
                     result += word.replace(word[i], word[i].upper()) + " ";
                     break;

    return result;

print(capitalize("aaron del ..cruz azul"));
