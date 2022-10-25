#  *
#  * Reto #4
#  * ÁREA DE UN POLÍGONO
#  * Fecha publicación enunciado: 24/01/22
#  * Fecha publicación resolución: 31/01/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  *

from msilib.schema import Class


class Poligono:
    def __init__(self):
        self
    
    def area(self):
        return 0;
   


class Triangulo(Poligono):
    def __init__(self, base, altura):
        super().__init__();
        self.__base = base;
        self.__altura = altura;
        self.__area = base * altura / 2;
    
    
    def area(self):
         return self.__area;

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__();
        self.__lado = lado;
        self.__area = lado * lado;
    
    def area(self):
        return self.__area;


t = Triangulo(5,2);
print(t.area());
c = Cuadrado(5);
print(c.area());
poli = Poligono();
poli = [t,c];
print(poli[0].area());
print(poli[1].area());