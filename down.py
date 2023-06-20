import wget
import patoolib
from path import add_path_to_environment_variable
import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import winreg

def add_path_to_environment_variable():
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

# def down_RCLONE():
#     url = 'https://drive.google.com/file/d/1CH73UQR7pzpFts0jPd7OjtrXXlYQZKas/view?usp=drive_link'
#     file_id = url.split('/')[-2]
#     download_url = f'https://drive.google.com/uc?id={file_id}'
#     print(download_url)
#     filename = wget.download(download_url)
#     patoolib.extract_archive(filename, outdir="c:/")
#     add_path_to_environment_variable()
#     return 1
