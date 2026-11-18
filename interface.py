
import tkinter as tk
from tkinter import messagebox

from operacoes import Soma, Subtracao, Multiplicacao, Divisao


class CalculadoraApp:

    def __init__(self, calculadora):
        self.calculadora = calculadora

        # Janela principal
        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("380x560")
        self.janela.resizable(False, False)

        self.criar_interface()

    def criar_interface(self):

        
        titulo = tk.Label(
            self.janela,
            text="Calculadora",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=20)

        
        frame_entrada = tk.Frame(self.janela)
        frame_entrada.pack(pady=10)

        tk.Label(
            frame_entrada,
            text="Primeiro número:"
        ).grid(row=0, column=0, padx=8, pady=8, sticky="w")

        self.entrada1 = tk.Entry(
            frame_entrada,
            width=18,
            font=("Arial", 12)
        )
        self.entrada1.grid(row=0, column=1, padx=8, pady=8)

        tk.Label(
            frame_entrada,
            text="Segundo número:"
        ).grid(row=1, column=0, padx=8, pady=8, sticky="w")

        self.entrada2 = tk.Entry(
            frame_entrada,
            width=18,
            font=("Arial", 12)
        )
        self.entrada2.grid(row=1, column=1, padx=8, pady=8)

        
        frame_operacoes = tk.Frame(self.janela)
        frame_operacoes.pack(pady=15)

        botoes = [
            ("+", Soma, "+"),
            ("−", Subtracao, "-"),
            ("×", Multiplicacao, "*"),
            ("÷", Divisao, "/"),
        ]

        for coluna, (texto, classe, simbolo) in enumerate(botoes):

            botao = tk.Button(
                frame_operacoes,
                text=texto,
                font=("Arial", 16, "bold"),
                width=4,
                height=1,
                command=lambda c=classe, s=simbolo: self.calcular(c, s)
            )

            botao.grid(row=0, column=coluna, padx=5)

        
        frame_resultado = tk.Frame(self.janela)
        frame_resultado.pack(pady=10)

        tk.Label(
            frame_resultado,
            text="Resultado",
            font=("Arial", 12)
        ).pack()

        self.resultado = tk.Label(
            frame_resultado,
            text="--",
            font=("Arial", 24, "bold"),
            fg="blue"
        )
        self.resultado.pack(pady=5)

        
        frame_historico = tk.Frame(self.janela)
        frame_historico.pack(pady=10)

        tk.Label(
            frame_historico,
            text="Histórico de cálculos",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        self.lista_historico = tk.Listbox(
            frame_historico,
            width=42,
            height=8,
            font=("Arial", 10)
        )
        self.lista_historico.pack()

        
        frame_limpeza = tk.Frame(self.janela)
        frame_limpeza.pack(pady=15)

        tk.Button(
            frame_limpeza,
            text="Limpar campos",
            command=self.limpar_campos
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            frame_limpeza,
            text="Limpar histórico",
            command=self.limpar_historico
        ).grid(row=0, column=1, padx=5)

    
    def calcular(self, classe_operacao, simbolo):

        try:
            # Obtém os valores digitados
            valor1 = self.entrada1.get()
            valor2 = self.entrada2.get()

            # Converte os valores para float
            numero1 = float(valor1)
            numero2 = float(valor2)

            # Instancia a operação escolhida
            operacao = classe_operacao(numero1, numero2)

            # Solicita o cálculo à Calculadora
            resultado = self.calculadora.calcular(
                operacao,
                simbolo
            )

            # Atualiza o resultado visual
            self.resultado.config(text=str(resultado))

            # Atualiza o histórico visual a partir do histórico da Calculadora
            self.atualizar_historico()

        except ValueError as erro:
            messagebox.showerror(
                "Erro de cálculo",
                str(erro) if str(erro) else "Digite números válidos."
            )

        except ZeroDivisionError:
            messagebox.showerror(
                "Erro",
                "Não é possível dividir por zero."
            )

        except Exception as erro:
            messagebox.showerror(
                "Erro inesperado",
                f"Ocorreu um erro:\n{erro}"
            )

    
    def atualizar_historico(self):

        self.lista_historico.delete(0, tk.END)

        registros = self.calculadora.historico.listar()

        for registro in registros:

            # Seu Calculadora registra os dados como uma tupla de strings
            if isinstance(registro, tuple):
                texto = "".join(registro)
            else:
                texto = str(registro)

            self.lista_historico.insert(tk.END, texto)

    
    def limpar_campos(self):

        self.entrada1.delete(0, tk.END)
        self.entrada2.delete(0, tk.END)

        self.resultado.config(text="--")

    
    def limpar_historico(self):

        self.calculadora.historico.limpar()

        self.lista_historico.delete(0, tk.END)

    
    def iniciar(self):
        self.janela.mainloop()
