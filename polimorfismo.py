
class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def avanza(self):
        print('Estoy avanzando!')


class Peaton(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        super().avanza()
        print('Camino para llegar a mi destino!')


class Ciclista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        super().avanza()
        print('Me muevo en bicicleta para llegar a mi destino!')

class Avion(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        super().avanza()
        print('Me estoy movilizando en avion!')


if __name__ == '__main__':
    peaton = Peaton('David')
    ciclista = Ciclista('Armando')
    avion = Avion('Katy')

    print(f'\nPersona 1: {peaton.nombre}\n')
    peaton.avanza()

    print(f'\nPersona 2: {ciclista.nombre}\n')
    ciclista.avanza()

    print(f'\nPersona 3: {avion.nombre}\n')
    avion.avanza()

