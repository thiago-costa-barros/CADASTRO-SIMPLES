# 1. IMPORTAT BLIBLIOTECAS NECESSÁRIAS.

from msilib.schema import ComboBox
import tkinter as tk  # biblioteca de interface gráfica
from tkinter import NSEW, ttk  # adicional da biblioteca
import datetime as dt  # biblioteca de registro de hora

# 2. CRIANDO INTERFACE GRÁFICA.
lista_logradouro = ['Rua', 'Avenida', 'Travessa',
                    'Beco', 'Rodovia', 'Estrada', 'Via', 'Loteamento']
lista_complemento = ['Casa', 'Alto', 'Loja',
                     'Apartamento', 'Fundos', 'Sem Complemento']
lista_especie = ['DPPO', 'DPPUO', 'DPPV',
                 'DPIO', 'DCCM', 'DCSM', 'EOF', 'PEUV']
lista_codigos = []
janela = tk.Tk()

# CRIAÇÃO DA FUNÇÃO


def inserir_codigo():
    tipo_logradouro = combobox_logradouro.get()
    logradouro = entry_logradouro.get()  # .get() recebe o valor digitado no tk.Entry
    numero = entry_numero.get()
    complemento = combobox_complemento.get()
    valor_complemento = entry_valor_complemento.get()
    especie = combobox_especie.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos)+1
    # vai ser gerado um codigo iniciando 0+1, e vai incrementando.
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str, tipo_logradouro, logradouro, numero, complemento,
                         valor_complemento, especie, data_criacao))  # dados são jogados nessa lista


# TITULO DA JANELA.
janela.title("CADASTRO DE UNIDADES")
label_logradouro = tk.Label(text="LOGRADOURO")
label_logradouro.grid(row=1, column=0, padx=10, pady=10,
                      sticky='nswe', columnspan=1)
combobox_logradouro = ttk.Combobox(values=lista_logradouro)
combobox_logradouro.grid(row=1, column=1, padx=10, pady=10,
                         sticky='nswe', columnspan=1)
entry_logradouro = tk.Entry()
entry_logradouro.grid(row=1, column=2, padx=10, pady=10,
                      sticky='nswe', columnspan=1)

label_numero = tk.Label(text="NÚMERO")
label_numero.grid(row=3, column=0, padx=10, pady=10,
                  sticky='nswe', columnspan=1)
entry_numero = tk.Entry()
entry_numero.grid(row=3, column=1, padx=10, pady=10,
                  sticky='nswe', columnspan=1)

label_complemento = tk.Label(text="COMPLEMENTO")
label_complemento.grid(row=4, column=0, padx=10, pady=10,
                       sticky='nswe', columnspan=1)
combobox_complemento = ttk.Combobox(values=lista_complemento)
combobox_complemento.grid(row=4, column=1, padx=10, pady=10,
                          sticky='nswe', columnspan=1)
entry_valor_complemento = tk.Entry()
entry_valor_complemento.grid(row=4, column=2, padx=10, pady=10,
                             sticky='nswe', columnspan=1)
label_especie = tk.Label(text="ESPÉCIE")
label_especie.grid(row=5, column=0, padx=10, pady=10,
                   sticky='nswe', columnspan=1)
combobox_especie = ttk.Combobox(values=lista_especie)
combobox_especie.grid(row=5, column=1, padx=10, pady=10,
                      sticky='nswe', columnspan=1)
botao_codigo_unidade = tk.Button(
    text='CONFIRMAR', command=inserir_codigo)
botao_codigo_unidade.grid(row=6, column=1, padx=10, pady=10,
                          sticky='nswe', columnspan=1)

janela.mainloop()

# printa valores no terminal, mas pode se jogar para um db, por exemplo.
print(lista_codigos)
