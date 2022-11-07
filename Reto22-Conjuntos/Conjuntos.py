#  *
#  * Reto #22
#  * CONJUNTOS
#  * Fecha publicación enunciado: 01/06/22
#  * Fecha publicación resolución: 07/06/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
#  * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
#  * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
#  * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
#  *


def common(arr1, arr2, comm:bool):
    result = [];
    
    if(comm):   #Se pueden quitar los repetidos con una estructura que no acepte repetidos.
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if(arr1[i] == arr2[j]):
                    result.append(arr2[j]);
                    break;
        
        print(result);
        return;
    test = False;
    for i in range(len(arr1)):
        test = True;
        for j in range(len(arr2)):
            if(arr1[i] == arr2[j]):
                test=False;
                break;
        
        if(test):
            result.append(arr1[i]);
        
    print(result);
    return;


a1 = [3,5,6,7,1,15];
b1 = [3,6,1,1,3];

common(b1,a1,True);
common(a1,b1, False);