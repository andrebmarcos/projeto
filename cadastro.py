import tkinter as tk
import sqlite3
import pandas as pd

# CONEXAO DO BANCO E CRIACAO DO BANCO
# conexao = sqlite3.connect('banco_cliente.db')

#c = conexao.cursor()

# c.execute('''CREATE TABLE clientes (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
#     )
# ''')
# conexao.commit()

# conexao.close()


def cadastrar_cliente():
   
    conexao = sqlite3.connect('banco_cliente.db')


    c = conexao.cursor()

    c.execute(" INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)",
           {
               'nome': entry_nome.get(),
               'sobrenome': entry_sobrenome.get(),
               'email': entry_email.get(),
               'telefone': entry_telefone.get()
           }

           )
    conexao.commit()

    conexao.close()

    entry_nome.delete(0,"end"),
    entry_sobrenome.delete(0,"end"),
    entry_email.delete(0,"end"),
    entry_telefone.delete(0,"end"),

def exportar_clientes():
    conexao = sqlite3.connect('banco_cliente.db')


    c = conexao.cursor()

    c.execute(" SELECT *, oid from clientes")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados=pd.DataFrame(clientes_cadastrados,columns=['Nome','Sobrenome','Email','Telefone','Id_banco'])
    clientes_cadastrados.to_excel('clientes.xlsx')
    #print(clientes_cadastrados)
    conexao.commit()

    conexao.close()


janela = tk.Tk()
janela.title('Ferramenta de Cadastro de Clientes')

# Lables
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='Email')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

# Entrys
entry_nome = tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text='Sobrenome', width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='Email', width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='Telefone', width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# Botão
botao_telefone = tk.Button(
    janela, text='Cadastar Cliente', command=cadastrar_cliente)
botao_telefone.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

botao_telefone = tk.Button(
    janela, text='Exportar para o Excel', command=exportar_clientes)
botao_telefone.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=70)

janela.mainloop()

