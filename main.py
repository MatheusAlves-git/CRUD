from tkinter import ttk
from tkinter import *
from mysql import connector


# Criando conexão com o Banco de Dados
conex = connector.connect(user='root', database='CRUD')
cursor = conex.cursor()

# Criando uma janela
janela = Tk()
janela.title('CRUD')

conn = cursor.execute("select * from pessoas;")  # Read
#               "Create Table ;")                # Create
resultados = cursor.fetchall()

id_novo = dict()
nome_novo = dict()


def salvar(id_salvar, nome_salvar):
    cursor.execute(f"insert into pessoas (id, nome) values ('{nome_salvar}', '{id_salvar}');")     # Update


def excluir_dados(id_excluir):
    cursor.execute(f"delete from pessoas where id = {id_excluir};")     # Delete


# LabelFrame do bloco Cadastro
frame = LabelFrame(janela, text=' Cadastro ')
frame.grid(row=0, column=1, columnspan=3, pady=20)

# LableFrame do bloco Pesquisar
frame_pesquisa = LabelFrame(janela, text=' Pesquisar ')
frame_pesquisa.grid(row=0, column=0, columnspan=1, pady=20)

# Textos do bloco Pesquisar
text_id = Label(frame_pesquisa, text='Pesquisar ID ').grid(row=0, column=0)
pesquisar_id = Entry(frame_pesquisa).grid(row=0, column=1)
text_nome = Label(frame_pesquisa, text='Pesquisar Nome ').grid(row=1, column=0)
pesquisar_nome = Entry(frame_pesquisa).grid(row=1, column=1)

# Textos do bloco Cadastro
text1 = Label(frame, text='Nome ')
text1.grid(row=0, column=5)
nome = Entry(frame)
nome.grid(row=0, column=6)
text2 = Label(frame, text='ID ')
text2.grid(row=1, column=5)
identificacao = Entry(frame)
identificacao.grid(row=1, column=6)


def click_add():
    nome_novo['nome'] = nome.get()
    id_novo['id'] = identificacao.get()
    salvar(nome_novo['nome'], id_novo['id'])


def click_excluir():
    id_novo['id'] = identificacao.get()
    excluir_dados(id_novo['id'])


# criação dos botões
adicionar = ttk.Button(frame, text=' Salvar ', command=click_add).grid(row=2, column=5)
excluir = ttk.Button(frame, text=' Excluir ', command=click_excluir).grid(row=2, column=6)
pesquisar = ttk.Button(frame_pesquisa, text=' Pesquisar ').grid(row=2, column=1)

# Criando a caixa de saida de dados
janela.tree = ttk.Treeview(height=10, column=2)
janela.tree.grid(row=4, column=0, columnspan=2)
janela.tree.heading('#0', text='Nome', anchor=CENTER)
janela.tree.heading('#1', text='ID', anchor=CENTER)

# Dados da tabela
cont = 0
for row in resultados:
    janela.tree.insert('', 0, text=resultados[cont][1], values=resultados[cont])
    cont = cont + 1

janela.mainloop()
