class WashingMachine:

    def __init__(self):
        pass

    # Tiene un método publico lavar que referencia a otros métodos
    def wash(self, temperature):
        new_temp = self._fill_water_tank(temperature)
        self._add_soap(new_temp)
        self._wash()
        self._centrifuge()

    # Los métodos privados de la clase no son relevantes
    # para el uso desde afuera de la clase y por
    # convención se inicia con _

    def _fill_water_tank(self, temperature):
        print(f'Filling the tank with {temperature} water.\n')
        
        temperature = 'warm'

        return temperature


    def _add_soap(self, temperature):
        print(f'Adding soap in {temperature} water...\n')


    def _wash(self):
        print('Washing the clothes.\n')


    def _centrifuge(self):
        print('Centrifuging the clothes.\n')


if __name__ == '__main__':

    temp = input('Temperature?\n')

    lavadora = WashingMachine()
    lavadora.wash(temp)