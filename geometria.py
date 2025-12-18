# AUTORA: Brigitte Karolay Velasquez Puma
# MODULO CON CLASES DE FIGURAS: RECTANGULO, TRIANGULO, CIRCULO
# METODOS: area() y perimetro()

import math
from typing import Tuple

class Figura:
    def area(self) -> float:
        raise NotImplementedError

    def perimetro(self) -> float:
        raise NotImplementedError

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = float(base)
        self.altura = float(altura)

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def __repr__(self):
        return f"Rectangulo(base={self.base}, altura={self.altura})"

class Triangulo(Figura):
    def __init__(self, a: float, b: float, c: float):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            raise ValueError("Lados no forman un triangulo valido")

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2.0
        return math.sqrt(max(0.0, s * (s - self.a) * (s - self.b) * (s - self.c)))

    def perimetro(self) -> float:
        return self.a + self.b + self.c

    def __repr__(self):
        return f"Triangulo(a={self.a}, b={self.b}, c={self.c})"

class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = float(radio)

    def area(self) -> float:
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

    def __repr__(self):
        return f"Circulo(radio={self.radio})"


def crear_lista_ejemplo() -> Tuple[Rectangulo, Triangulo, Circulo]:
    r = Rectangulo(4, 3)
    t = Triangulo(3, 4, 5)
    c = Circulo(2.5)
    return (r, t, c)

