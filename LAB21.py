# LABORATORIO 21 
# AUTORA: BRIGITTE KAROLAY VELASQUEZ PUMA


import json
import time
import random
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List
from geometria import Rectangulo, Triangulo, Circulo, crear_lista_ejemplo


# EJERCICIO 3 
def ejercicio_3_mostrar():
    print("EJERCICIO 3")
    r = Rectangulo(5, 2)
    t = Triangulo(3, 4, 5)
    c = Circulo(3)
    figuras = [r, t, c]
    for f in figuras:
        print(f"{f!r} -> AREA: {f.area():.2f} | PERIMETRO: {f.perimetro():.2f}")

# EJERCICIO 4 
class Libro:
    def __init__(self, titulo: str, autor: str, anio: int):
        self.titulo = titulo
        self.autor = autor
        self.anio = int(anio)
        self.disponible = True

    def prestar(self) -> bool:
        if not self.disponible:
            return False
        self.disponible = False
        return True

    def devolver(self) -> None:
        self.disponible = True

    def info(self) -> str:
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} ({self.anio}) [{estado}]"

class LibroDigital(Libro):
    def __init__(self, titulo: str, autor: str, anio: int, formato: str, tam_mb: float):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.tam_mb = float(tam_mb)
        self.disponible = True


    def prestar(self) -> bool:
        return True

    def info(self) -> str:
        return f"{self.titulo} - {self.autor} ({self.anio}) [Digital {self.formato} {self.tam_mb}MB]"

class Biblioteca:
    def __init__(self):
        self.libros: List[Libro] = []

    def agregar(self, libro: Libro) -> None:
        self.libros.append(libro)

    def listar(self) -> List[str]:
        return [l.info() for l in self.libros]

    def buscar_por_autor(self, autor: str) -> List[Libro]:
        autor_norm = autor.strip().lower()
        return [l for l in self.libros if l.autor.strip().lower() == autor_norm]

    def prestar_por_titulo(self, titulo: str) -> bool:
        for l in self.libros:
            if l.titulo.strip().lower() == titulo.strip().lower():
                return l.prestar()
        raise ValueError("Libro no encontrado")

def ejercicio_4_demo():
    print("\nEJERCICIO 4")
    b = Biblioteca()
    # 3 libros fisicos
    b.agregar(Libro("Fundamentos de Programacion", "Marco Aedo", 2022))
    b.agregar(Libro("Estructuras de Datos", "Karolay Velasquez", 2021))
    b.agregar(Libro("Redes de Computadoras", "Luis Gomez", 2019))
    # 2 digitales
    b.agregar(LibroDigital("Python Avanzado", "Mariana Ruiz", 2023, "PDF", 3.2))
    b.agregar(LibroDigital("Algoritmos", "Carlos Ruiz", 2020, "EPUB", 1.1))

    print("LISTA COMPLETA:")
    for info in b.listar():
        print("-", info)

    print("\nPRESTAR UN LIBRO FISICO:")
    ok = b.prestar_por_titulo("Fundamentos de Programacion")
    print("Prestado correctamente." if ok else "No se pudo prestar.")

    print("\nPRESTAR UN LIBRO DIGITAL 5 VECES:")
    for i in range(5):
        ok = b.prestar_por_titulo("Python Avanzado")
        print(f"Intento {i+1}: {'Prestado (digital -> siempre disponible)' if ok else 'No disponible'}")

    print("\nINTENTAR PRESTAR UN LIBRO YA PRESTADO (Fundamentos de Programacion) otra vez:")
    ok = b.prestar_por_titulo("Fundamentos de Programacion")
    print("Prestado correctamente." if ok else "No se pudo prestar (ya prestado).")

    print("\nBUSCAR LIBROS POR AUTOR 'Karolay Velasquez':")
    encontrados = b.buscar_por_autor("Karolay Velasquez")
    for e in encontrados:
        print("-", e.info())


# EJERCICIO 5
class OperadorInvalidoError(Exception):
    pass

def evaluar_operacion_from_string(expr: str) -> float:
    parts = expr.strip().split()
    if len(parts) != 3:
        raise ValueError("Formato invalido")
    n1s, op, n2s = parts
    try:
        a = float(n1s)
        b = float(n2s)
    except ValueError:
        raise ValueError("Numeros invalidos")
    if op not in ("+", "-", "*", "/"):
        raise OperadorInvalidoError(f"Operador invalido: {op}")
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division por cero detectada")
        return a / b
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b

def ejercicio_5_interactivo():
    print("\nEJERCICIO 5")
    while True:
        s = input("Ingrese operacion o 'salir' > ").strip()
        if s.lower() in ("salir", "exit", "q"):
            break
        try:
            r = evaluar_operacion_from_string(s)
            print("Resultado:", r)
        except ZeroDivisionError:
            print("ERROR: No se puede dividir entre cero.")
        except ValueError as ve:
            print("ERROR DE VALORES:", ve)
        except OperadorInvalidoError as oe:
            print("ERROR OPERADOR:", oe)


# EJERCICIO 6 
def ejercicio_6_usar_modulo():
    print("\nEJERCICIO 6")
    r, t, c = crear_lista_ejemplo()
    print("Rectangulo area/perimetro:", r.area(), r.perimetro())
    print("Triangulo area/perimetro:", t.area(), t.perimetro())
    print("Circulo area/perimetro:", c.area(), c.perimetro())


# EJERCICIO 7 
def copiar_archivo_texto(origen: str, destino: str):
    with open(origen, "r", encoding="utf-8") as f_in:
        contenido = f_in.read()
    with open(destino, "w", encoding="utf-8") as f_out:
        f_out.write(contenido)

def copiar_archivo_binario(origen: str, destino: str):
    with open(origen, "rb") as f_in:
        contenido = f_in.read()
    with open(destino, "wb") as f_out:
        f_out.write(contenido)

def ejercicio_7_demo():
    print("\nEJERCICIO 7")
   
    with open("ejemplo_texto.txt", "w", encoding="utf-8") as f:
        f.write("Linea 1\nLinea 2\n")
    copiar_archivo_texto("ejemplo_texto.txt", "ejemplo_texto_copia.txt")
    print("archivo de texto copiado a ejemplo_texto_copia.txt")


    with open("ejemplo_binario.bin", "wb") as f:
        f.write(b"\x00\x01\x02\x03\x04")
    copiar_archivo_binario("ejemplo_binario.bin", "ejemplo_binario_copia.bin")
    print("archivo binario copiado a ejemplo_binario_copia.bin")


# EJERCICIO 8 
def ejercicio_8_json_equipos():
    print("\nEJERCICIO 8")
    equipos = [
        {"Nombre": "Alianza", "Pais": "Peru", "nivelAtaque": 7.5, "nivelDefensa": 6.2},
        {"Nombre": "Universitario", "Pais": "Peru", "nivelAtaque": 8.0, "nivelDefensa": 7.1},
        {"Nombre": "Boca", "Pais": "Argentina", "nivelAtaque": 8.9, "nivelDefensa": 7.8},
        {"Nombre": "Real Madrid", "Pais": "España", "nivelAtaque": 9.3, "nivelDefensa": 8.6},
    ]
    texto = json.dumps(equipos, ensure_ascii=False, indent=2)
    print(texto)


# EJERCICIO 9 
def consulta_simulada_sync(nombre: str, tiempo_seg: float):
    time.sleep(tiempo_seg)
    return f"OK: {nombre} ({tiempo_seg:.2f}s)"

async def consulta_simulada_async(nombre: str, tiempo_seg: float):
    await asyncio.sleep(tiempo_seg)
    return f"OK: {nombre} ({tiempo_seg:.2f}s)"

def medir_threading_consultas(nombres: List[str], tiempos: List[float]) -> float:
    inicio = time.perf_counter()
    results = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = [ex.submit(consulta_simulada_sync, n, t) for n, t in zip(nombres, tiempos)]
        for fut in futures:
            results.append(fut.result())
    dur = time.perf_counter() - inicio
    return dur

def medir_multiprocessing_consultas(nombres: List[str], tiempos: List[float]) -> float:
    inicio = time.perf_counter()

    with ProcessPoolExecutor(max_workers=3) as ex:
        results = list(ex.map(consulta_simulada_sync, nombres, tiempos))
    dur = time.perf_counter() - inicio
    return dur

async def medir_asyncio_consultas(nombres: List[str], tiempos: List[float]) -> float:
    inicio = time.perf_counter()
    coros = [consulta_simulada_async(n, t) for n, t in zip(nombres, tiempos)]
    _ = await asyncio.gather(*coros)
    dur = time.perf_counter() - inicio
    return dur

def ejercicio_9_simulacion():
    print("\nEJERCICIO 9")

    nombres = ["Consulta A", "Consulta B", "Consulta C"]
    tiempos = [random.uniform(1, 5) for _ in range(3)]
    print("Tiempos simulados:", [f"{t:.2f}s" for t in tiempos])

    t_thread = medir_threading_consultas(nombres, tiempos)
    print(f"THREADING: {t_thread:.3f} s")

    t_proc = medir_multiprocessing_consultas(nombres, tiempos)
    print(f"MULTIPROCESAMIENTO: {t_proc:.3f} s")

    t_async = asyncio.run(medir_asyncio_consultas(nombres, tiempos))
    print(f"ASYNCIO: {t_async:.3f} s")

    tiempos_dict = {"threading": t_thread, "multiprocessing": t_proc, "asyncio": t_async}
    orden = sorted(tiempos_dict.items(), key=lambda x: x[1])
    print("MAS RAPIDO:", orden[0][0], f"({orden[0][1]:.3f}s)")
    print("MAS LENTO:", orden[-1][0], f"({orden[-1][1]:.3f}s)")
    print("EXPLICACION: Para operaciones que esperan IO, threading o asyncio suelen ser mejores. Multiprocesamiento tiene overhead de procesos.")


# EJECUCION 
def main():
    print("LABORATORIO 21")

    # Ejercicio 3
    ejercicio_3_mostrar()

    # Ejercicio 4
    ejercicio_4_demo()

    # Ejercicio 5
    ejercicio_5_interactivo()

    # Ejercicio 6
    ejercicio_6_usar_modulo()

    # Ejercicio 7
    ejercicio_7_demo()

    # Ejercicio 8
    ejercicio_8_json_equipos()

    # Ejercicio 9
    ejercicio_9_simulacion()

if __name__ == "__main__":
    main()
