# *
#  * Reto #18
#  * TRES EN RAYA
#  * Fecha publicación enunciado: 02/05/22
#  * Fecha publicación resolución: 09/05/22
#  * Dificultad: DIFÍCIL
#  *
#  * Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
#  * - "X" si han ganado las "X"
#  * - "O" si han ganado los "O"
#  * - "Empate" si ha habido un empate
#  * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
#  * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
#  *
#  *

# // Nota: Para evaluar la matriz, primero, se tiene que ingresar al arreglo de puntos
# // después con la información de los puntos se tiene que ir al arreglo de posiciones,
# // el cual indica cuales líneas se tienen que evaluar.

# //Ejemplo de cómo evalúa el programa. 
# //PuntosEvaluar --> posición --> líneas 
# matriz[fila][columna]

from asyncio.windows_events import NULL
from copyreg import constructor


class Point:
    def __init__(self, fila, columna):
        self.fila = fila;
        self.columna = columna;

class Line:
    def __init__(self, points) -> None:
        self.points = points;
        self.visited = False;
        
        
puntosEvaluar = [
    Point(0,0),
    Point(0,1),
    Point(0,2),
    Point(1,0),
    Point(2,0)];




#Buscar en lineas cada punto señalado por posicion.    
posicion ={
    Point(0,0): [1,2,3],
    Point(0,1): [1,4],
    Point(0,2): [1,5,6],
    Point(1,0): [7,2],
    Point(2,0): [8,6,2],
};
            
lineas = {
    1 : Line([Point(0,0),Point(0,1), Point(0,2)]),
    2 : Line([Point(0,0),Point(1,0), Point(2,0)]),
    3 : Line([Point(0,0),Point(1,1), Point(2,2)]),
    4 : Line([Point(0,1),Point(1,1), Point(2,1)]),
    5 : Line([Point(0,2),Point(1,2), Point(2,2)]),
    6 : Line([Point(2,0),Point(1,1), Point(0,2)]),
    7 : Line([Point(1,0),Point(1,1), Point(1,2)]),
    8 : Line([Point(2,0),Point(2,1), Point(2,2)])    

};   

def checkMatrix(matrix:str)->bool:
    countX = 0;
    countO = 0;
    for line in matrix:
        for e in line:
            if(e == "X"):
                countX+=1;
            elif(e == "O"):
                countO+=1;

    if(abs(countX-countO)>1):
        return False; 
    return True;
    
def ticTactoe(matrix:str)->str:
    if(not checkMatrix(matrix)):
        return NULL;
    test = False;
    char = "";
    winner="";
    counter = 0;
    for point,arrLines in posicion.items():
        char = matrix[point.fila][point.columna];
        for lineNum in arrLines:
            if(lineas[lineNum].visited == True):
                continue;
            for p in lineas[lineNum].points:
                if(char != matrix[p.fila][p.columna]):
                    test = False;
                    break;
                test = True;
                
            if(test):
                winner = char;                
                counter+=1;
            lineas[lineNum].visited = True;

    if(counter==1):
        print("The Winner is: "+ winner);
        return winner
    elif(counter == 0):
        print ("Its a Draw");
        return 0;
    else:
        return NULL;
    
 

matrix = [["X","X","X"],
          ["O","O","X"],
          ["X","O","O"]];

ticTactoe(matrix);

