import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import datetime
from threading import Thread
from funcoes import enviar_diretorio_para_mega
from time import sleep
from tkinter import *
from PIL import ImageTk, Image
import subprocess
import wget
import patoolib
import winreg
from informacoes import capturar_informacoes_rclone
import os
class DirectorySelector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.iconbitmap('img/bkp.ico')
        self.root.title("Sistema de Backup no Mega.nz")
        self.root.attributes('-topmost', True)
        self.root.attributes('-top', 1)
        self.largura_janela = 500
        self.altura_janela = 400
        self.largura_tela = self.root.winfo_screenwidth()
        self.frm_largura = self.root.winfo_rootx() - self.root.winfo_x()
        self.win_largura_janela = self.largura_janela + 2 * self.frm_largura
        self.titlebar_altura = self.root.winfo_rooty() - self.root.winfo_y()
        self.win_altura = self.altura_janela + self.titlebar_altura + self.frm_largura
        # Calcular a posição para centralizar a janela
        self.x = self.root.winfo_screenwidth() // 2 - self.largura_janela // 2
        self.y = self.root.winfo_screenheight() // 2 - self.win_altura // 2
        # Definir a posição da janela
        self.root.geometry('{}x{}+{}+{}'.format(self.largura_janela, self.altura_janela, self.x, self.y))

        self.directory_path = tk.StringVar()
        self.directory_path.set("")
        # Menu
        self.barra_menu = tk.Menu(self.root)
        # Criar um item de menu
        self.menu_arquivo = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_arquivo.add_command(label="Carregar padrao", command=self.fill_directory_column)
        self.menu_arquivo.add_command(label="Instalar Rclone", command=self.download_rclone_thread)
        self.menu_arquivo.add_command(label="Configurar Usuario/senha", command=self.config_rclone)
        
        # Adicionar o item de menu à barra de menu
        self.barra_menu.add_cascade(label="Configuração", menu=self.menu_arquivo)

        # Definir a barra de menu na janela
        self.root.config(menu=self.barra_menu)
        # Entry para exibir o diretório selecionado
        self.directory_entry = tk.Entry(self.root, textvariable=self.directory_path, width=50)
        self.directory_entry.grid(row=0, column=0, padx=10, pady=10)

        # Botão para abrir a janela de seleção de diretório
        self.img_folder = tk.PhotoImage(file='img/folder.png')
        self.select_button = tk.Button(self.root, text="Sel. Diretório", image=self.img_folder, compound=tk.LEFT, command=self.select_directory)
        self.select_button.grid(row=0, column=1, padx=10, pady=10)
        self.adicionar_hover(botao=self.select_button,mensagem='Selecionar Diretorio para backup',cor='#FF0000')
        # Botão Ajuda
        self.img_btn_ajuda=tk.PhotoImage(file='img/help32.png')
        self.btn_ajuda=Button(self.root,image=self.img_btn_ajuda,command=self.abrir_nova_janela)
        self.btn_ajuda.place(rely=0, relx=0.9)
        self.adicionar_hover(botao=self.btn_ajuda,mensagem='Ver as Orientações',cor='#FF0000')
        # Botão para carregar arquivo com os diretórios padrão na treeview
        self.img_btn_padrao=tk.PhotoImage(file='img/padrao.png')
        self.btn_padrao=tk.Button(self.root, text="Carregar Dir.\npadrão",image=self.img_btn_padrao,compound=tk.LEFT,command=self.fill_directory_column)
        self.btn_padrao.place(relx=0.6,rely=0.8)
        self.adicionar_hover(botao=self.btn_padrao,mensagem='Carregar diretorios padrão na Tabela',cor='#FF0000')

        # Botão para adicionar o diretório selecionado na Treeview
        self.img_btn_add = tk.PhotoImage(file='img/add.png')
        self.add_button = tk.Button(self.root, text="Adicionar", image=self.img_btn_add, compound=tk.LEFT, command=self.add_to_treeview)
        self.add_button.place(x=(self.altura_janela/2), y=45)
        self.adicionar_hover(botao=self.add_button,mensagem='Adicionar o diretorio Selecionado na Tabela',cor='#FF0000')
        # Botão gravar arquivo com os diretórios padrão
        self.img_btn_gravar_padrao=tk.PhotoImage(file='img/save.png')
        self.btn_gravar_padrao=tk.Button(self.root,text='Gravar Dir.\n Padrão',image=self.img_btn_gravar_padrao,compound=tk.LEFT,command=self.save_to_file)
        self.btn_gravar_padrao.place(x=(self.altura_janela/2)-100, y=45)
        self.adicionar_hover(botao=self.btn_gravar_padrao,mensagem='Gravar Diretorios na tabela como diretorios padrão',cor='#FF0000')
        # Botão para deletar linhas na treeview
        self.img_btn_del = tk.PhotoImage(file='img/delete-table.png')
        self.btn_del_treeview = tk.Button(self.root, text="Deletar", image=self.img_btn_del, compound=tk.LEFT, command=self.delete_selected_row)
        self.btn_del_treeview.place(rely=0.80, relx=0.2)
        self.adicionar_hover(botao=self.btn_del_treeview,mensagem='Deletar linha Selecionada na tabela',cor='#FF0000')
        # Botão para Enviar diretórios para o MEGA
        self.img_btn_enviar = tk.PhotoImage(file='img/mega_cloud.png')
        self.btn_enviar_nuvem = tk.Button(self.root, text="Enviar", image=self.img_btn_enviar, compound=tk.LEFT, command=self.enviar_nuvem_thread)
        self.btn_enviar_nuvem.place(rely=0.80, relx=0.4)
        self.adicionar_hover(botao=self.btn_enviar_nuvem,mensagem='Enviar Diretorio para nuvem',cor='#FF0000')

    def reiniciar_windows(self):
        # Função para Reiniciar Windows
        self.resposta = messagebox.askquestion("Reiniciar Windows", "Tem certeza que deseja reiniciar o Windows?")
        if self.resposta == 'yes':
            subprocess.call(['shutdown', '/r', '/t', '0'])

    def submit(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        create_command = f'rclone config create mega mega user "{email}"'
        password_command = f'rclone config password mega pass "{password}"'
        subprocess.run(create_command, shell=True, check=True)
        subprocess.run(password_command, shell=True, check=True)
        total, used, free = capturar_informacoes_rclone()
        messagebox.showinfo(title='Sucesso', message=f'*** Configuração realizada com Sucesso!!! ***\nTotal de espaço: {total}\nUsado: {used}\nLivre: {free}')
        self.janela.destroy()

    def config_rclone(self):
        # Função para conigurar o rclone com a conta do Mega.nz
        self.janela=Tk()
        self.janela.title("Configurar Rclone")
        self.janela.attributes('-topmost', True)
        self.janela.attributes('-top', 1)
        self.janela.geometry("200x200")
        email_label = tk.Label(self.janela, text="Email:")
        email_label.pack()
        self.email_entry = tk.Entry(self.janela)
        self.email_entry.pack()
        password_label = tk.Label(self.janela, text="Senha:")
        password_label.pack()
        self.password_entry = tk.Entry(self.janela, show="*")
        self.password_entry.pack()
        submit_button = tk.Button(self.janela, text="Enviar", command=self.submit)
        submit_button.pack()

    def add_path_to_environment_variable(self):
    # Função para adicionar o Rclone o path do sistema
        new_path = 'C:\\rclone'
        # Abre a chave de registro do ambiente do usuário
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_ALL_ACCESS)
        # Lê o valor atual da variável PATH
        current_path = winreg.QueryValueEx(key, 'PATH')[0]
        # Adiciona o novo caminho ao valor atual
        new_path = current_path + ';' + new_path
        # Define o novo valor da variável PATH
        winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, new_path)
        # Atualiza as alterações no ambiente de execução
        winreg.CloseKey(key)
        # Atualiza as alterações no ambiente de execução usando o utilitário setx
        subprocess.call(['setx', 'PATH', new_path])
        self.reiniciar_windows()

    def downRCLONE(self):
        # Função para baixar e descompactar o Rcloneno Sistema
        self.Aviso(mensagem='Instalando o Rclone, favor aguardar',cor='#32CD32')
        url = 'https://drive.google.com/file/d/1CH73UQR7pzpFts0jPd7OjtrXXlYQZKas/view?usp=drive_link'
        file_id = url.split('/')[-2]
        download_url = f'https://drive.google.com/uc?id={file_id}'
        print(download_url)
        filename = wget.download(download_url)
        patoolib.extract_archive(filename, outdir="c:/")
        self.add_path_to_environment_variable()

    def download_rclone_thread(self):
        # Função para baixar e descompactar o Rcloneno Sistema numa thread separada da interface, vita travar a tela
        thread = Thread(target=self.downRCLONE)
        thread.start()

    def Aviso(self, mensagem, cor):
        # Função para avisar na Label
        self.lbl_aviso = tk.Label(self.root, text="", bg='green',justify='center')
        self.lbl_aviso.place(relx=0, rely=0.91, relwidth=0.98)
        self.lbl_aviso.configure(text=mensagem, background=cor)
        self.lbl_aviso.place(relx=0, rely=0.91, relwidth=0.98)

    def abrir_nova_janela(self):
        # Janela de ajuda
        nova_janela = tk.Toplevel(self.root)
        nova_janela.attributes('-topmost', True)
        nova_janela.attributes('-top', 1)
        nova_janela.lift()
        
        # Carregar e exibir a imagem com as oientações
        imagem = Image.open('img/helpbkp.png')
        imagem = imagem.resize((500, 500))  # Ajuste o tamanho da imagem conforme necessário
        foto = ImageTk.PhotoImage(imagem)
        label_imagem = tk.Label(nova_janela, image=foto)
        label_imagem.pack()

        # Calcular a posição x e y para centralizar a janela
        largura = 500 #nova_janela.winfo_width()
        frm_largura = nova_janela.winfo_rootx() - nova_janela.winfo_x()
        win_largura = largura + 2 * frm_largura

        altura = 500 #nova_janela.winfo_height()
        titlebar_altura = nova_janela.winfo_rooty() - nova_janela.winfo_y()
        win_altura = altura + titlebar_altura + frm_largura
        x = nova_janela.winfo_screenwidth() // 2 - win_largura // 2
        y = nova_janela.winfo_screenheight() // 2 - win_altura // 2
        nova_janela.geometry('{}x{}+{}+{}'.format(largura, altura, x, y))
        # Definir a posição da janela no centro da tela
        nova_janela.mainloop()
        # nova_janela.deiconify()

    def fill_directory_column(self):
        # Função para carregar o arquivo dir.txt (diretórios padrão) na treeview
        arquivo=os.path.isfile('dir.txt')
        if arquivo == False:
            messagebox.showerror(title='Arquivo Inexistente',message='O arquivo do diretorios padrão não existe!!!')
        else:
            self.treeview.delete(*self.treeview.get_children())
            with open("dir.txt", "r") as file:
                for index, line in enumerate(file, start=1):
                    directory = line.strip()
                    self.treeview.insert("", "end", values=(index, directory))

    def save_to_file(self):
        # Função gravar arquivo com diretórios padrão
        if not self.treeview.get_children():
            messagebox.showinfo("Tabela Vazia", "A Tabela está vazia.", parent=self.root)
        else:
            with open("dir.txt", "w") as file:
                for child in self.treeview.get_children():
                    directory = self.treeview.item(child)["values"][1]
                    file.write(directory + "\n")

    def adicionar_hover(self,botao, mensagem, cor):
        # Mostra Label com os descritivo do botão
        def mostrar_aviso(event):
            self.Aviso(mensagem, cor)
            self.lbl_aviso.configure(font=('Arial', 10, 'bold italic'),foreground='#FFFFFF')
        def remover_aviso(event):
            self.lbl_aviso.destroy()
            pass

        botao.bind("<Enter>", mostrar_aviso)
        botao.bind("<Leave>", remover_aviso)

    def capturar_diretorios(self):
        # Função para baixar capturar as informações da treeview e enviar para o mega
        self.data_atual = datetime.datetime.now().strftime("%d%m%Y")
        self.pasta_mega = f"mega:BACKUP/{self.data_atual}"
        if not self.treeview.get_children():
            messagebox.showinfo("Tabela Vazia", "A Tabela está vazia.", parent=self.root)
            return []

        # Enviar diretorios para o MEGA via rclone
        diretorios = []
        for item in self.treeview.get_children():
            diretorio = self.treeview.item(item)["values"][1]
            pasta_unica = diretorio.split('/')[-1]
            pasta_mega = f'{self.pasta_mega}/{pasta_unica}'
            self.Aviso(mensagem=f'Enviando a pasta {pasta_unica.upper()}', cor='#32CD32')
            print(f'{diretorio} | {pasta_mega}')
            enviado = enviar_diretorio_para_mega(diretorio=diretorio, pasta_mega=pasta_mega)
            if enviado == True:
                self.Sucesso(mensagem=f'Pasta {pasta_unica.upper()} enviada com Sucesso!!!', cor='#32CD32')
                sleep(2)  # import time
                messagebox.showinfo(title='Sucesso!!!',message='Backup realizado com Sucesso!!!', parent=self.root)
            else:
                messagebox.showerror(title='Erro!!!',message='Problema ao realizar Backup\n Favor fazer as verificações no menu configuraçoes', parent=self.root)
        
    def enviar_nuvem_thread(self):
        """Função enviar diretorios para o MEGA via rclone, executa a função capturar_diretorios 
           numa thread separada da interface gráfica, assim não trava a tela"""
        thread = Thread(target=self.capturar_diretorios)
        thread.start()

    def select_directory(self):
        # Função para escolher o diretório
        selected_directory = filedialog.askdirectory()
        if selected_directory:
            self.directory_path.set(selected_directory)

    def add_to_treeview(self):
        # Função para addicionar o diretório na treeview
        if not self.directory_path.get():
            messagebox.showerror(title='Vazio', message='Nenhum diretório escolhido', parent=self.root)
        else:
            directory = self.directory_path.get()
            if directory:
                self.treeview.insert("", "end", values=(self.item_counter, directory))
                self.item_counter += 1

    def delete_selected_row(self):
        # Função para deletar linhas seecionadas da treeview
        selected_item = self.treeview.selection()
        if selected_item:
            self.treeview.delete(selected_item)
        else:
            messagebox.showinfo("Nenhum item selecionado", "Por favor, selecione um item para excluir.", parent=self.root)

    def run(self):
        # Função que adiciona a treeview na janela
        self.treeview = ttk.Treeview(self.root, columns=("Item", "Diretório"), show="headings")
        self.treeview.heading("Item", text="Item")
        self.treeview.heading("Diretório", text="Diretório", anchor='n')
        self.treeview.column("Diretório", anchor='center', width=self.largura_janela-50)
        self.treeview.column("Item", width=50, anchor='n')
        self.treeview.place(relx=0.01, rely=0.25, width=self.largura_janela-30, relheight=0.5)
        self.treeview_scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.treeview_scrollbar.set)
        self.treeview_scrollbar.place(rely=0.25, x=self.largura_janela-19, relheight=0.5)
        self.item_counter = 1
        self.root.mainloop()

# Iniciar a aplicação
app = DirectorySelector()
app.run()
