import tkinter as tk
from tkinter import messagebox
import subprocess

def reiniciar_windows():
    resposta = messagebox.askquestion("Reiniciar Windows", "Tem certeza que deseja reiniciar o Windows?")
    if resposta == 'yes':
        subprocess.call(['shutdown', '/r', '/t', '0'])

# Exemplo de uso
root = tk.Tk()
root.withdraw()  # Esconde a janela principal

reiniciar_windows()
