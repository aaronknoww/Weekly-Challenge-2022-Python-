#  * Reto #9
#  * CÓDIGO MORSE
#  * Fecha publicación enunciado: 02/03/22
#  * Fecha publicación resolución: 07/03/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.


texto = """A;.-;B;-...;C;-.-.;D;-..;E;.;F;..-.;
 G;--.;H;....;I;..;J;.---;K;-.-;L;.-..;
 M;--;N;-.;O;---;P;.--.;Q;--.-;R;.-.;
 S;...;T;-;U;..-;V;...-;W;.--;X;-..-;
 Y;-.--;Z;--..;Á;.--.-;É;..-..;Ñ;--.--;Ó;---.;
 0;-----;1;.----;2;..---;3;...--;4;....-;5;.....;
 6;-....;7;--...;8;---..;9;----.;
 .;.-.-.-;,;--..--;?;..--..;';.----.;!;-.-.--;/;-..-.;
 (;-.--.;);-.--.-;&;.-...;:;---...;=;-...-;+;.-.-.;-;-....-;_;..--.-;$;...-..-;@;.--.-.;¿;..-.-;¡;--...-;""";

print(texto);

from array import array
from pickle import NONE
import re


reEraseSpace = r"\s{2,}";
reEraseEnters = r"\n";
reMorse = r"^[-.\s/]+$";

morseDic = {};
alphabetDic = {};


def createDictionaries(text:str):
    result = re.sub(reEraseEnters,"", texto, re.MULTILINE);
    result = re.sub(reEraseSpace,"", texto, re.MULTILINE);
    code = re.split(";",result);

    for i in range(len(code)):
        code[i] = re.sub(reEraseSpace,"", code[i], re.MULTILINE); 

    for i in range(0, len(code)-1, 2) :
        morseDic.update({code[i] : code[i+1]});
        alphabetDic.update({code[i+1] : code[i]});

def morseToText(text:str):
    #TODO: SEPARAR PATRONES POR ESPACIO.
    word="";
    code = re.split(" ",text);
    for mr in code:
        if(mr=="/"):
            word = word + " ";
            continue;

        word = word + alphabetDic[mr];
    
    print(word);


def textToMorse(text:str):
    morse = "";
    for tx in text:
        if(tx==" "):
            morse = morse + "/" + " ";
            continue;

        morse = morse + morseDic[tx] + " ";
    
    print(morse);



def translate(text: str):
    createDictionaries(texto);
    result = re.sub(reEraseSpace,"", text, re.MULTILINE);
    result = result.upper();  

    if( len(re.findall(reMorse,result)) > 0):
        morseToText(result);
    else:
        textToMorse(result);


entrada = ".- .- .-. --- -. / -.. . .-.. / -.-. .-. ..- --.. / .- --.. ..- .-..";
aaron = "Aaron Know";

translate(aaron);

