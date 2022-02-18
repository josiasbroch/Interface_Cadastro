#PASSO A PASSO
#1)Importar bibliotecas
#2)Criar Interface Gráfica: Descricão, Tipo da Unidade, Quantidade do tipo da Unidade
#3)Inteligencia da interface grafica: Funçao

import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["Galão", "Caixa", "Saco", "Unidade"]
lista_codigos = []

janela = tk.Tk()

#Criação da função do botão
def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos)+1 #O tamanho da lista +1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))#Cria uma tupla pra nunca alterar, sempre fixo

#Titulo da Janela
janela.title('Ferrramenta de cadastro de materiais')

#Cria a label
label_descricao = tk.Label(text="Descrição do Material")
#Posiciona a label
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

#Cria Espaço do cadastro
entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text="Tipo da Unidade do Material")
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quant = tk.Label(text="Quantidade na Unidade do Material")
label_quant.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text='Criar Código', command= inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop()

print(lista_codigos)


