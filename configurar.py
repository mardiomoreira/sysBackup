import subprocess
import tkinter as tk
from tkinter import messagebox

def execute_command(command):
    subprocess.run(command, shell=True, check=True)

def create_mega_config(email, password):
    create_command = f'rclone config create mega mega user "{email}"'
    password_command = f'rclone config password mega pass "{password}"'

    execute_command(create_command)
    execute_command(password_command)

def check_mega_connection():
    command = "rclone ls mega:"
    try:
        execute_command(command)
        messagebox.showinfo("Sucesso", "Conexão com o Mega estabelecida com sucesso!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Erro", "Falha ao estabelecer conexão com o Mega.")

def get_credentials():
    email = ""
    password = ""

    def submit():
        nonlocal email, password
        email = email_entry.get()
        password = password_entry.get()
        root.destroy()

    root = tk.Tk()
    root.title("Credenciais Mega")
    root.geometry("300x150")

    email_label = tk.Label(root, text="Email:")
    email_label.pack()

    email_entry = tk.Entry(root)
    email_entry.pack()

    password_label = tk.Label(root, text="Senha:")
    password_label.pack()

    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    submit_button = tk.Button(root, text="Enviar", command=submit)
    submit_button.pack()

    root.mainloop()

    return email, password

# Obtenha as credenciais do usuário
email_da_conta_mega, senha_da_conta_mega = get_credentials()

# Crie a configuração do Mega
create_mega_config(email_da_conta_mega, senha_da_conta_mega)

# Verifique a conexão com o Mega
check_mega_connection()
