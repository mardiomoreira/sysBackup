# import tkinter as tk
# from tkinter.font import Font

# # Crie uma instância da janela tkinter
# janela = tk.Tk()

# # Crie uma fonte em negrito
# fonte_negrito = Font(weight='bold')

# # Crie uma label com o texto completo
# lbl_tamanho = tk.Label(janela, text="Tamanho 20MB")

# # Configure a fonte em negrito somente para o trecho desejado
# lbl_tamanho.config(font=(fonte_negrito, lbl_tamanho.cget("font")))

# # Exiba a label na janela
# lbl_tamanho.pack()

# # Inicie o loop principal da janela tkinter
# janela.mainloop()
import os
arquivo=os.path.isfile('dir.txt')
print(arquivo)
if arquivo == False:
    print()
else:
    statement