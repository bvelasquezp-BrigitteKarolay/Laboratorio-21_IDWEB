# LABORATORIO 21 
# AUTORA: BRIGITTE KAROLAY VELASQUEZ PUMA

import math

# EJERCICIO 3 
import math

class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(Figura):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimetro(self):
        return self.a + self.b + self.c


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
    
#EJERCICIO 4
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True


class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio, formato, tamanoMB):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tamanoMB = tamanoMB

    def prestar(self):
        return True


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar(self):
        for l in self.libros:
            print(l.titulo, l.autor, l.disponible)

    def buscar_por_autor(self, autor):
        for l in self.libros:
            if l.autor == autor:
                print(l.titulo)

    def prestar_libro(self, titulo):
        for l in self.libros:
            if l.titulo == titulo:
                return l.prestar()
        return False
    
#EJERCICIO 5
class OperadorInvalido(Exception):
    pass

def calcular(expresion):
    a, op, b = expresion.split()
    a = float(a)
    b = float(b)

    if op not in "+-*/":
        raise OperadorInvalido()

    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError()
        return a / b
    
#
