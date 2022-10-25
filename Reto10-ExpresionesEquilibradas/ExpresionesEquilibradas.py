# *Reto #10
# * EXPRESIONES EQUILIBRADAS
# * Fecha publicación enunciado: 07/03/22
# * Fecha publicación resolución: 14/03/22
# * Dificultad: MEDIA
# *
# * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# * - Expresión no balanceada: { a * ( c + d ) ] - 5 }


from inspect import stack


def isBalanced(expression: str):
    stak = [];
    balanced = True;     
    for chr in expression :
        if(chr=="("):
            stak.append(chr);
        elif(chr == "["):
            stak.append(chr);
        elif(chr == "{"):
            stak.append(chr);
        elif(chr == ")"):
            if(len(stak)>0 and stak[-1] == "("):
                stak.pop();
            else:
                balanced = False;
                break;
        elif(chr == "]"):
            if(len(stak)>0 and stak[-1] == "["):
                stak.pop();
            else:
                balanced = False;
                break;
        elif(chr == "}"):
            if(len(stak)>0 and stak[-1] == "{"):
                stak.pop();
            else:
                balanced = False;
                break;
    
    if(balanced and len(stak)==0):
        print("EXPRESION BALANCEADA");
    else:
        print("ERROR EN LA EXPRESION");

isBalanced("(");
    
