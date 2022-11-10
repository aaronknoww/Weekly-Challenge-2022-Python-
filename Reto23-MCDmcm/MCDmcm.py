#  *
#  * Reto #23
#  * MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
#  * Fecha publicación enunciado: 07/06/22
#  * Fecha publicación resolución: 13/06/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
#  * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.


primos = [2,3,5,7,11,13,17,19,23];

def mcd(num1:int, num2:int)->int:
    if(num1 == 0 or num2 == 0):
        return -1;
    res = 1;
    n1 = num1;
    n2 = num2;
    arr1 = [];
    arr2 = [];
    i1 = 0;
    i2 = 0;

    while((n1 != 1) or (n2 != 1)):
        if( (n1 % primos[i1]) == 0 and (n1 != 1)):
            arr1.append(primos[i1]);
            n1 = n1/primos[i1];
        else:
            i1+=1;

        if( (n2 % primos[i2]) == 0 and (n2 != 1)):
            arr2.append(primos[i2]);
            n2 = n2/primos[i2];
        else:
            i2+=1;

    n1 = len(arr1);
    n2 = len(arr2);
    i1 = 0;
    i2 = 0;
    arrR = [];

    while( (i1 < n1)):
        if(arr1[i1] == arr2[i2]):
            arrR.append(arr1[i1]);
            i1+=1;
            i2+=1;
        else:
            ia=i2;
            while((ia < n2)):
                if(arr1[i1] == arr2[ia]):
                    arrR.append(arr1[i1]);
                    i2=ia+1;
                    break;
                ia+=1;
            
            i1+=1;

    for e in arrR:
        res*=e;
    
    print(f"el MCD es: {res}");
    return res;

def mcm(num1:int, num2:int)->int:
    if(num1 == 0 or num2 == 0):
       return -1;
    
    res = 1;
    n1 = num1;
    n2 = num2;
    arr1 = [];
    i1 = 0;
    
    while((n1 != 1) or (n2 != 1)):
        if( (n1 % primos[i1]) == 0 and (n2 % primos[i1]) == 0):
            arr1.append(primos[i1]);
            n1 = n1/primos[i1];
            n2 = n2/primos[i1];
        elif((n1 % primos[i1]) == 0):
            arr1.append(primos[i1]);
            n1 = n1/primos[i1];
        elif((n2 % primos[i1]) == 0):
            arr1.append(primos[i1]);
            n2 = n2/primos[i1];
        else:
            i1+=1;
    
    for e in arr1:
        res *= e;
    print(f"El MCM es: {res}");
    return res;



mcm(4,30);
mcd(225,300);
mcd(380,420);
    
        



