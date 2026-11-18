from abc import ABC, abstractmethod

class Operacao(ABC):
    def __init__(self, first, second):
        self.first = float(first)
        self.second = float(second)

    @abstractmethod
    def executar(self):
        pass

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, valor):
        self._first = float(valor)

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, valor):
        self._second = float(valor)

class Soma(Operacao):
    def executar(self):
        return self.first + self.second

class Subtracao(Operacao):
    def executar(self):
        return self.first - self.second

class Multiplicacao(Operacao):
    def executar(self):
        return self.first * self.second

class Divisao(Operacao):
    def executar(self):
        if self.second == 0:
            raise ValueError("Não é possível realizar divisão por 0.")

        return self.first / self.second
