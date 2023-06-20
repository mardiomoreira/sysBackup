from tkinter import *
import tkinter as tk
from tkinter.font import Font
from ver_rclone import check_rclone_configured, check_rclone_installed, verificar_rclone_path, obter_tamanho_remote
import re
import subprocess

def fechar_janela():
    janela.destroy()
    caminho_arquivo = "backup.exe"
    processo = subprocess.Popen(caminho_arquivo)
    processo.wait()

def atualizar_contagem(tempo_restante):
    lbl_aviso['text'] = f'Iniciando em {tempo_restante} segundos...'
    if tempo_restante > 0:
        janela.after(1000, atualizar_contagem, tempo_restante - 1)
    else:
        fechar_janela()

janela = Tk()
janela.geometry("250x250")
janela.title('Verificação Ambiente')
img_check = tk.PhotoImage(file='img/check.png')
img_erro = tk.PhotoImage(file='img/error.png')
img_tamanho = tk.PhotoImage(file='img/size.png')
img_question = tk.PhotoImage(file='img/question.png')
lbl_check_rcINSTALL = Label(janela, text='')
lbl_check_rcCONFIG = Label(janela, text='')
lbl_check_rcPATH = Label(janela, text='')
lbl_check_rcTamanho = Label(janela, text='')
lbl_aviso = Label(janela, text='',font=('Arial',11,'bold italic'),justify='center',background='#FF0000', foreground='#FFFFFF')

lbl_check_rcINSTALL.pack()
lbl_check_rcPATH.pack()
lbl_check_rcCONFIG.pack()
lbl_check_rcTamanho.pack()
lbl_aviso.place(relx=0.01,rely=0.8,relwidth=0.98)

fonte_negrito = Font(weight='bold')
indice = 0

# Verificando instalação
rclone_install = check_rclone_installed()

if rclone_install == 1:
    lbl_check_rcINSTALL.configure(text=' Rclone Instalado', image=img_check, compound=tk.LEFT)
    indice += 1
elif rclone_install == 0:
    lbl_check_rcINSTALL.configure(text=' Rclone não instalado', image=img_erro, compound=tk.LEFT)

if rclone_install == 2:
    lbl_check_rcINSTALL.configure(text="O comando 'Rclone' está instalado, mas ocorreu um erro ao executá-lo.",
                                  image=img_question, compound=tk.LEFT)

# Verificando Configração
rclone_config = check_rclone_configured()

if rclone_config == 1:
    lbl_check_rcCONFIG.configure(text=' Rclone Configurado', image=img_check, compound=tk.LEFT)
    indice += 1
elif rclone_config == 0:
    lbl_check_rcCONFIG.configure(text=' Rclone não Configurado', image=img_erro, compound=tk.LEFT)

# Verificar se o rclone está no PATH do sistema
rclone_path = verificar_rclone_path()

if rclone_path == 1:
    lbl_check_rcPATH.configure(text="Rclone está no PATH do sistema.", image=img_check, compound=tk.LEFT)
    indice += 1
elif rclone_path == 0:
    lbl_check_rcPATH.configure(text="Rclone não está no PATH do sistema.", image=img_erro, compound=tk.LEFT)

if indice == 3:
    tamanho = obter_tamanho_remote("mega:")
    tamanho = re.sub(r" \([0-9]{2,} Byte\)", '', tamanho)
    lbl_check_rcTamanho.configure(text=f'Tamanho disponível: {tamanho}', image=img_tamanho, compound=tk.LEFT)
    lbl_check_rcTamanho.configure(justify=tk.CENTER)
    atualizar_contagem(5)  # Inicia a contagem regressiva de 5 segundos

janela.mainloop()
