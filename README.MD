# 🧮 CalculadoraPOO

Uma calculadora desktop desenvolvida em **Python**, utilizando **Tkinter** para a interface gráfica e princípios de **Programação Orientada a Objetos (POO)** para estruturar a lógica e as operações matemáticas.

O projeto foi desenvolvido com o objetivo de praticar organização de código, abstração, herança, encapsulamento e integração entre diferentes classes e módulos Python.

## 📸 Sobre o projeto

A CalculadoraPOO permite realizar operações matemáticas básicas através de uma interface gráfica intuitiva, além de armazenar e exibir um histórico dos cálculos realizados durante a execução.

## ✨ Funcionalidades

- ➕ Adição
- ➖ Subtração
- ✖️ Multiplicação
- ➗ Divisão
- 📝 Histórico de cálculos
- 🧹 Limpeza dos campos de entrada
- 🗑️ Limpeza do histórico
- ⚠️ Tratamento de entradas inválidas
- ⚠️ Tratamento de divisão por zero
- 🖥️ Interface gráfica com Tkinter

## 🛠️ Tecnologias utilizadas

- **Python**
- **Tkinter**
- **Programação Orientada a Objetos (POO)**
- **PyInstaller** — empacotamento da aplicação em executável

## 🏗️ Estrutura do projeto

```text
CalculadoraPOO/
│
├── main.py
├── interface.py
├── calculadora.py
├── operacoes.py
├── historico.py
│
├── README.md
└── requirements.txt
```

### Organização dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Inicialização da aplicação |
| `interface.py` | Interface gráfica e interação com o usuário |
| `calculadora.py` | Orquestração das operações e registro no histórico |
| `operacoes.py` | Definição das operações matemáticas |
| `historico.py` | Armazenamento e gerenciamento do histórico |

## 🧠 Conceitos de POO aplicados

O projeto utiliza conceitos fundamentais de Programação Orientada a Objetos:

- **Abstração:** definição de uma classe base abstrata `Operacao`.
- **Herança:** classes específicas de operações herdam de `Operacao`.
- **Polimorfismo:** diferentes operações implementam o método `executar()`.
- **Encapsulamento:** utilização de propriedades, getters e setters para acesso aos atributos.
- **Responsabilidade única:** separação entre interface, lógica de cálculo, operações e histórico.

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/CalculadoraPOO.git
```

### 2. Entre na pasta do projeto

```bash
cd CalculadoraPOO
```

### 3. Execute a aplicação

```bash
python main.py
```

## 📦 Gerando o executável