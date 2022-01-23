from tkinter import *
from tkinter import ttk
import sqlite3

#Configuração da Janela
root = Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
    def conecta_db(self):
        self.conn = sqlite3.connect("clientes2.db")
        self.cursor = self.conn.cursor() ;print("Conectando ao banco de dados")
    def desconectar_db(self):
        self.conn.close();print("Desonectando do banco de dados")
    def montaTabela(self):
        self.conecta_db()
        ## Criando a tabela
        self.cursor.execute ("""
            CREATE TABLE IF NOT EXISTS clientes2 (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER (20),
                cidade CHAR (40)
            );
        """)      
        self.conn.commit(); print("Banco de dados criado")
        self.desconectar_db()
    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecta_db()
        self.cursor.execute(""" INSERT INTO clientes2 (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconectar_db()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes2 ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconectar_db()


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabela()
        self.select_lista()
        root.mainloop()
    def tela(self):
        self.root.title('Cadastro de Clientes')
        self .root.configure(background='#1e3743')
        self.root.geometry('600x400')
        self.root.resizable(True,True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

#cRIANDO OS FRAMES
    def frames_da_tela(self):
        self.frame1 = Frame(self.root, bd = 4, bg= '#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame1.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)
        
        self.frame2 = Frame(self.root, bd = 4, bg= '#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame2.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)
#Criando Botoes
    def widgets_frame1(self):
    #criando botão limpar
        self.bt_limpar = Button(self.frame1, text= 'Limpar', bd=2, bg='#107db2', fg ='white', font = ('verdana', 8, 'bold'),command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2 , rely=0.13, relwidth=0.1, relheight=0.12)
    #criando botãi buscar
        self.bt_buscar = Button(self.frame1, text= 'Buscar', bd=2, bg='#107db2', fg ='white', font = ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3 , rely=0.13, relwidth=0.1, relheight=0.12)
    #criando botão novo
        self.bt_novo = Button(self.frame1, text= 'Novo', bd=2, bg='#107db2', fg ='white', font = ('verdana', 8, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6 , rely=0.13, relwidth=0.1, relheight=0.12)
    #criando botãi alterar
        self.bt_alterar = Button(self.frame1, text= 'Alterar', bd=2, bg='#107db2', fg ='white', font = ('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.7 , rely=0.13, relwidth=0.1, relheight=0.12)
    #criando botãi apagar
        self.bt_apagar = Button(self.frame1, text= 'Apagar', bd=2, bg='#107db2', fg ='white', font = ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.8 , rely=0.13, relwidth=0.1, relheight=0.12)
    

    #Criação da label e entrada do codigo
        self.lb_codigo = Label(self.frame1, text= 'Código',bd = 4, bg= '#dfe3ee', fg ='#107db2' )
        self.lb_codigo.place(relx=0.05 , rely= 0.04)
        
        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx=0.05 , rely=0.17, relwidth=0.09)

        #Criação da label e entrada do nome
        self.lb_nome = Label(self.frame1, text= 'Nome',bd = 4, bg= '#dfe3ee', fg ='#107db2' )
        self.lb_nome.place(relx=0.05 , rely= 0.3)
        
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05 , rely=0.45, relwidth=0.8)

        #Criação da label e entrada do Telefone
        self.lb_telefone = Label(self.frame1, text= 'Telefone',bd = 4, bg= '#dfe3ee', fg ='#107db2' )
        self.lb_telefone.place(relx=0.05 , rely= 0.6)
        
        self.telefone_entry = Entry(self.frame1)
        self.telefone_entry.place(relx=0.05 , rely=0.75, relwidth=0.4)

        #Criação da label e entrada do Cidade
        self.lb_cidade = Label(self.frame1, text= 'Cidade',bd = 4, bg= '#dfe3ee', fg ='#107db2' )
        self.lb_cidade.place(relx=0.5 , rely= 0.6)
        
        self.cidade_entry = Entry(self.frame1)
        self.cidade_entry.place(relx=0.5 , rely=0.75, relwidth=0.4)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3,columns= ('col1','col2','col3','col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Códico')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')
        
        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.01 , rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroollista =Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscroll =self.scroollista.set)
        self.scroollista.place(relx=0.96 , rely=0.1, relwidth=0.04, relheight=0.85)


Application()