import subprocess
import os, re

def check_rclone_installed():
    try:
        subprocess.run(["rclone", "--version"], check=True, capture_output=True)
        print("O comando 'rclone' está instalado.")
        return 1
    except FileNotFoundError:
        print("O comando 'rclone' não está instalado.")
        return 0
    except subprocess.CalledProcessError:
        print("O comando 'rclone' está instalado, mas ocorreu um erro ao executá-lo.")
        return 2

def check_rclone_configured():
    try:
        subprocess.run(["rclone", "config", "show"], check=True, capture_output=True)
        print("O 'rclone' está configurado.")
        return 1
    except subprocess.CalledProcessError:
        print("O 'rclone' não está configurado.")
        return 0
def verificar_rclone():
    try:
        # Executa o comando 'rclone version' no terminal
        resultado = subprocess.run(['rclone', 'version'], capture_output=True, text=True)

        # Verifica se o comando foi executado com sucesso
        if resultado.returncode == 0:
            # Verifica se a saída contém a versão do Rclone
            if 'rclone' in resultado.stdout:
                print("Rclone está instalado e funcionando corretamente.")
                return 1
            else:
                print("Não foi possível verificar a instalação do Rclone.")
                return 0
        else:
            print("Erro ao executar o comando 'rclone version'.")
    except FileNotFoundError:
        print("Rclone não está instalado ou não está no PATH do sistema.")

def verificar_rclone_path():
    # Verifica se o diretório do Rclone está no PATH do sistema
    lista=os.environ['PATH'].split(';')
    contador=0
    for vamb in lista:
        ver= re.findall('Rclone|rclone',vamb)
        if len(ver)>0:
            contador+=1
    if contador>0:
        print("Rclone está no PATH do sistema.")
        return 1
    else:
        print("Rclone não está no PATH do sistema.")
        return 0
#Tamanho disponível
def obter_tamanho_remote(remote):
    try:
        # Executa o comando 'rclone size' no terminal para o remote especificado
        resultado = subprocess.run(['rclone', 'size', remote], capture_output=True, text=True)

        # Verifica se o comando foi executado com sucesso
        if resultado.returncode == 0:
            # Procura pela linha contendo a informação "Total size"
            padrao = r"Total size:\s+(.+)"
            correspondencia = re.search(padrao, resultado.stdout)

            if correspondencia:
                # Captura a informação "Total size"
                total_size = correspondencia.group(1)
                return total_size
            else:
                print("Não foi possível obter a informação de tamanho.")
        else:
            print(f"Erro ao executar o comando 'rclone size {remote}'.")
    except FileNotFoundError:
        print("Rclone não está instalado ou não está no PATH do sistema.")

# Chama a função para obter a informação de tamanho do remote "mega:"
tamanho_total = obter_tamanho_remote("mega:")
if tamanho_total is not None:
    print("Tamanho total do remote 'mega:':")
    print(tamanho_total)
    
    
    
    
    
# verificar_rclone_path()