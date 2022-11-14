class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
            print(f'La region {region} si está en la lista! :D\n')
        else:
            raise ValueError(f'La region {region} no esta en la lista')


if __name__ == '__main__':

    casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
    print(casilla.region)

    casilla.region = input(str('Ingresa la región:\n'))

    #casilla.region = 'Mexico'

    print(f'{casilla._identificador} es el identificador de la region de: {casilla.region}')
