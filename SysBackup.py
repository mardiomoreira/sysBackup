import os
import sys
import subprocess
from time import sleep

def verificar_abertura_sistema():
    if os.path.exists('flag.txt'):
        print("O sistema já foi aberto.")
        subprocess.Popen('bkp.exe', shell=True)

    else:
        print("O sistema ainda não foi aberto.")
        subprocess.Popen('checkp.exe', shell=True)
        # Cria o arquivo de flag para indicar que o sistema foi aberto
        with open('flag.txt', 'w') as flag_file:
            flag_file.write('O sistema foi aberto.')

    # Aguarda 2 segundos
    sleep(1)

# Chamada da função
verificar_abertura_sistema()
