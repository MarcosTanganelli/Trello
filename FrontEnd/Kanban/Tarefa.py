import tkinter as tk

class Tarefa(tk.Frame):
    def __init__(self, master=None, nome="", data="", descricao="", cor="blue"):
        super().__init__(master)
        self.configure(bg=cor, padx=10, pady=5)
        self.nome = nome
        self.data = data
        self.descricao = descricao
        self.cor = cor
        self.coluna = None


        self.labelNome = tk.Label(self, text=self.nome, font=("Arial", 12, "bold"), bg=self.cor, fg="white")
        self.labelNome.pack(anchor="w")

        self.labelData = tk.Label(self, text=f"Data: {self.data}", bg=self.cor, fg="white")
        self.labelData.pack(anchor="w")

        self.labelDescricao = tk.Label(self, text=f"Descrição: {self.descricao}", bg=self.cor, fg="white")
        self.labelDescricao.pack(anchor="w")

    def setCor(self, novocor):
        self.cor = novocor # precisa reconfigurar
    
    def getCor(self):
        return self.cor
    

    def setNome(self, novoNome):
        self.nome = novoNome
    
    def getNome(self):
        return self.nome
    
    def setData(self, novodata):
        self.data = novodata
    
    def getData(self):
        return self.data
    
    def setDescricao(self, novodescricao):
        self.descricao = novodescricao
    
    def getDescricao(self):
        return self.descricao
    
    def setColuna(self, novocoluna):
        self.coluna = novocoluna
    
    def getColuna(self):
        return self.coluna
    

