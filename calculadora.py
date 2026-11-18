from historico import Historico

class Calculadora:
    def __init__(self):
       self.historico = Historico()

    def calcular(self, operacao, simbolo):
        resultado = operacao.executar()

        registro = (
            f"{operacao.first} {simbolo} ",
            f"{operacao.second} = {resultado}"
        )

        self.historico.adicionar(registro)

        return resultado