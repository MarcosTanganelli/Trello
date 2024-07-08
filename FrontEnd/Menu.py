import tkinter as tk
# from tkinter import ttk
import threading
from FrontEnd.Kanban.Kanban import Kanban


class Menu:
    """Classe Menu: vai chamar as demais paginas, passando a janela para fazerem as devidas alterações
    """
    def __init__(self, janela):
        """Inicializa a janela e o Menu:\n
        Menu -> tool bar 
        Args:
            janela (tkk): Recebe a janela para colocar as caracteristicas do Menu
        """
        self.janela = janela
        self.janela.title("Gerenciador de Tarefas")
        self.janela.geometry("1500x800")

        menu_bar = tk.Menu(self.janela)
        menu_bar.add_command(label="Login") # Login
        menu_bar.add_command(label="Kanbam", command = self.mostrarKanban) # Kanbam
        menu_bar.add_command(label="Scrum") # Scrum
        # menu_bar.add_command(label="Scrum", command=self.mostrar_infos_sistema) # Scrum


        self.janela.config(menu=menu_bar)

        
    def apagarElementos(self): 
        """Função que irá limpar as tabelas e labels, conforme muda a pagina
        """
        for widget in self.janela.winfo_children():
            if widget.winfo_class() != 'Menu':
                widget.destroy()
                
    def mostrarKanban(self):
        self.apagarElementos()
        Kanban(self.janela)


    # def mostrar_infos_arquivos(self):
    #     """Função que chama a pagina Info Arqs com uma thread
    #     """
    #     self.apagar_elementos()
    #     thread = threading.Thread(target=lambda: InfoArqs(self.janela))
    #     thread.start()
    
   