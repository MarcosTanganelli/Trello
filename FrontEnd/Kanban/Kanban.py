# https://getnave.com/blog/wp-content/uploads/2018/03/kanban-board-in-trello.jpg
# Imagem usada como referência
import tkinter as tk

from FrontEnd.Kanban.Tarefa import Tarefa


class Kanban:
    def __init__(self, janela):
        self.janela = janela
        self.columns = ["TO DO", "RESEARCH", "IN PROGRESS", "REVIEW", "COMPLETE"]
        self.createColuns()

    def createColuns(self):
        self.janela.grid_columnconfigure(len(self.columns), weight=1000)
        self.janela.grid_rowconfigure(0, weight=1)

        self.frames = {}  # Dicionário para armazenar os frames das colunas
        self.listboxes = {}  # Dicionário para armazenar as listboxes das colunas

        for idx, col in enumerate(self.columns):
            self.frameColuns = tk.Frame(self.janela, bd=2, relief=tk.SUNKEN)
            self.frameColuns.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")
            # frame.grid_propagate(False)

            label = tk.Label(self.frameColuns, text=col, bg="lightgray")
            label.pack(fill=tk.X)

            listbox = tk.Listbox(self.frameColuns, selectmode=tk.SINGLE)
            listbox.pack(expand=True, fill=tk.BOTH)
            self.listboxes[col] = listbox

            self.frames[col] = self.frameColuns

        self.button = tk.Button(self.janela, text="Criar Tarefa", command=self.abrirJanelaCriarTarefa)
        self.button.grid(row=5, column=5, padx=5, pady=5)
    
    def abrirJanelaCriarTarefa(self):
        # Remove o frame de criação de tarefa existente, se houver
        if hasattr(self, 'frameTarefa'):
            self.frameTarefa.destroy()

        # Cria um novo frame à direita para inserir os detalhes da tarefa
        self.frameTarefa = tk.Frame(self.janela, bd=2, relief=tk.SUNKEN)
        self.frameTarefa.configure(padx=10, pady=10, bg="gray")
        self.frameTarefa.grid(row=0, column=len(self.columns), padx=5, pady=5, sticky="nsew")

        tk.Label(self.frameTarefa, text="Nome:", bg="gray").grid(row=0, column=0, sticky="w")
        self.entryNome = tk.Entry(self.frameTarefa)
        self.entryNome.grid(row=0, column=1, sticky="ew")

        tk.Label(self.frameTarefa, text="Data:", bg="gray").grid(row=1, column=0, sticky="w")
        self.entryData = tk.Entry(self.frameTarefa)
        self.entryData.grid(row=1, column=1, sticky="ew")

        tk.Label(self.frameTarefa, text="Descrição:", bg="gray").grid(row=2, column=0, sticky="w")
        self.entryDescricao = tk.Entry(self.frameTarefa)
        self.entryDescricao.grid(row=2, column=1, sticky="ew")

        tk.Button(self.frameTarefa, text="Adicionar", command=self.adicionarTarefa).grid(row=3, column=0, columnspan=2)

    def adicionarTarefa(self):
        nome = self.entryNome.get()
        data = self.entryData.get()
        descricao = self.entryDescricao.get()

        nova_tarefa = Tarefa(self.frames["TO DO"], nome, data, descricao, cor="blue")
        nova_tarefa.pack(fill=tk.X, padx=10, pady=5, before=self.frames["TO DO"].winfo_children()[1])
        
        # Remove o frame de criação de tarefa após adicionar a tarefa
        self.frameTarefa.destroy()

    def infosTarefa():
        print("teste")
    


