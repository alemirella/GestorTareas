import tkinter as tk
from tkinter import ttk, messagebox
from src.logica.gestor_tareas import GestorTareas

class GestorTareasGUI:
    def __init__(self, root, gestor):
        self.gestor = gestor
        self.root = root
        self.root.title("Gestor de Tareas")
        # Aquí agregaríamos el código de los widgets y las funcionalidades GUI

def run():
    root = tk.Tk()
    gestor = GestorTareas()
    app = GestorTareasGUI(root, gestor)
    root.mainloop()

if __name__ == "__main__":
    run()
