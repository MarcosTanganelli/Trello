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
            frame = tk.Frame(self.janela, bd=2, relief=tk.SUNKEN)
            frame.grid(row=0, column=idx, padx=5, pady=5, sticky="nsew")
            # frame.grid_propagate(False)

            label = tk.Label(frame, text=col, bg="lightgray")
            label.pack(fill=tk.X)

            listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
            listbox.pack(expand=True, fill=tk.BOTH)
            self.listboxes[col] = listbox

            self.frames[col] = frame

        self.button = tk.Button(self.janela, text="Teste", command=self.criarTarefa)
        self.button.grid(row=5, column=5, padx=5, pady=5)

    def criarTarefa(self):
        nome = "Nova Tarefa"
        data = "10/07/2024"
        descricao = "Descrição da nova tarefa"
        nova_tarefa = Tarefa(self.frames["TO DO"], nome, data, descricao, cor="blue")
        nova_tarefa.pack(fill=tk.X, padx=10, pady=5, before=self.frames["TO DO"].winfo_children()[1])


