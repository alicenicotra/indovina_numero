import random


class Model(object):
    def __init__(self):
        self._Nmax = 100   # fondo scala
        self._Mmax = 6     # numero massimo di tentativi
        self._Mrim = self._Mmax
        self._segreto = None

    @property
    def Nmax(self):
        return self._Nmax
    @property
    def Mmax(self):
        return self._Mmax
    @property
    def Mrim(self):
        return self._Mrim



    def inizializza(self):
        # Pesca il numero segreto
        self._segreto = random.randint(1, self._Nmax)
        self._Mrim = self._Mmax

    def indovina(self, tentativo):

        if self._Mrim == 0:
            return self._Mrim, None

        else :
            self._Mrim = self._Mrim - 1

        if tentativo == self._segreto:
            return self._Mrim, 0

        elif tentativo > self._segreto:
            return self._Mrim, -1

        else:
            return self._Mrim, 1