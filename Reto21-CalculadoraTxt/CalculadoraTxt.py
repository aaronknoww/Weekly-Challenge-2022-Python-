#  *
#  * Reto #21
#  * CALCULADORA .TXT
#  * Fecha publicación enunciado: 23/05/22
#  * Fecha publicación resolución: 01/06/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
#  * - El .txt se corresponde con las entradas de una calculadora.
#  * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
#  * - Soporta números enteros y decimales.
#  * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
#  * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
#  * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.



# EXPRESIONES REGULARES PARA EVALUAR QUE EL TEXTO QUE INGRESA ES CORRECTO
import re

regexFormat = r"^(\d+\s*[+\-/*/]{1}\s*\d+)(\s*[+\-/*/]\s*\d+)*"; # Revisa que el patron de de la operacion se (num opera num opera num)
regexPermitidos = r"(^[\s*0-9+/\-/*/\s*]*$)"; #Expresion regular que solo permite del (0-9) y (+ - * /) 

fileName ='Challenge21.txt';


def readFormat(fileName:str)->str:
    file = open(fileName);
    rd = file.read();
    return re.sub("\n+"," ", rd,0, re.MULTILINE);


def textCalculator(expression:str)->int:
    if( (len(re.findall(regexPermitidos,expression)) < 1) or (len(re.findall(regexFormat,expression)) < 1) ):
        return "Error";
    
    arr = expression.split(" ");
    i=0;
    while i < len(arr):
        if(arr[i] == "*"):
            total = float(arr[i-1]) * float(arr[i+1]);
            arr[i-1] = total;
            del arr[i+1];
            del arr[i];
            i-=1;
        if(arr[i] == "/"):
            if(arr[i+1] == 0):
                raise Exception("No se puede dividir entre cero");

            total = float(arr[i-1]) / float(arr[i+1]);
            arr[i-1] = total;
            del arr[i+1];
            del arr[i];
            i-=1;
        i+=1
    
    i=0;
    while i < len(arr):
        if(arr[i] == "+"):
            total = float(arr[i-1]) + float(arr[i+1]);
            arr[i-1] = total;
            del arr[i+1];
            del arr[i];
            i-=1;
        if(arr[i] == "-"):
            total = float(arr[i-1]) - float(arr[i+1]);
            arr[i-1] = total;
            del arr[i+1];
            del arr[i];
            i-=1;
        i+=1
    
    print(f"El resultado es: ${arr[0]}");
         

    
        
expression = readFormat(fileName);
textCalculator(expression);

