#  *
#  * Reto #7
#  * CONTANDO PALABRAS
#  * Fecha publicación enunciado: 14/02/22
#  * Fecha publicación resolución: 21/02/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

from array import array
from ast import And
from pydoc import replace
import re
import string

cadena = "zi LO  QUE que que  SEA";
reEreseSpace = r"\s{1,}";
reEreaseCharcters = r"[^a-zA-z0-9\s]+";


   

def wordCounter(text :str)->int:
    if(len(text)<1):
        return 0;
    
    result = re.sub(reEreaseCharcters," ", text, re.MULTILINE);
    result = re.sub(reEreseSpace," ",result, re.MULTILINE);
    result = result.lower();
    arr = re.split(" ",result);
    arr.sort();
    mapa = set(arr); # To remove duplicate words.
    noDuplicates = list(mapa); #To convert set into list and be able to sort
    noDuplicates.sort();
    
    counter = 0; 

    diccionario = {} 
    j=0;
    for i in range(len(noDuplicates)):
        counter = 0;
        while j<len(arr) and noDuplicates[i] == arr[j]  :
            j+=1;
            counter+=1;

        diccionario.update({noDuplicates[i] : counter});
    
    print(diccionario);

wordCounter(cadena);    



# You can manually specify the number of replacements by changing the 4th argument