#  *
#  * Reto #17
#  * LA CARRERA DE OBSTÁCULOS
#  * Fecha publicación enunciado: 25/04/22
#  * Fecha publicación resolución: 02/05/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
#  * carrera de obstáculos.
#  * - La función recibirá dos parámetros:
#  *      - Un array que sólo puede contener String con las palabras "run" o "jump"
#  *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
#  * - La función imprimirá cómo ha finalizado la carrera:
#  *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
#  *        variará el símbolo de esa parte de la pista.
#  *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#  *      - Si hace "run" en "|" (valla), se variará la pista por "/".
#  * - La función retornará un Boolean que indique si ha superado la carrera.
#  * Para ello tiene que realizar la opción correcta en cada tramo de la pista.


from cmath import exp

reEraseSpace = r"\s{2,}";
reEraseEnters = r"\n";
reMorse = r"^[-.\s/]+$";
regex = r"^[a-zA-Z,. ]+$";
justLetters = r"^[a-zA-Z]+$";

act = {
    'run':'_',
    'jump':'|'
}

def checkRace(action:str, track:str )->bool:
    if(len(action) != len(track)):
        raise Exception("Bad arguments");
    result = "";
    test = True;
    i = 0;
    for a in action:
        if( act[a] == track[i]):
            result += track[i];
        else:
            if(a == 'run'):
                result+='X';
                test = False;
            else:
                result +="/";
                test = False;
        i+=1;
    
    print(result);
    return test;


j = 'jump';
r = 'run';

action = [r,j,r,r,j];
tra = '|___|';

checkRace(action, tra);