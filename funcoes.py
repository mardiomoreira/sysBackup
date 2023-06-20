import subprocess
import datetime

def enviar_diretorio_para_mega(diretorio, pasta_mega):
    # Obter a data atual no formato brasileiro (dia, mês, ano)
    data_atual = datetime.datetime.now().strftime("%d,%m,%Y")

    # Montar o caminho da pasta no MEGA
    # pasta_mega = f"MEGA:BACKUP/data({data_atual})"

    # Comando rclone para enviar o diretório para o MEGA
    comando_rclone = ["rclone", "copy", diretorio, pasta_mega, "--create-empty-src-dirs"]

    try:
        # Executar o comando rclone
        subprocess.run(comando_rclone, check=True)
        return True #operação foi bem-sucedida
    except subprocess.CalledProcessError:
        return False

def listar_diretorios_mega():
    # Caminho da pasta no MEGA
    pasta_mega = "MEGA:BACKUP"

    # Comando rclone para listar os diretórios no MEGA
    comando_rclone = ["rclone", "lsd", pasta_mega]

    try:
        # Executar o comando rclone
        subprocess.run(comando_rclone, capture_output=True, text=True, check=True)
        return True #operação foi bem-sucedida
    except subprocess.CalledProcessError:
        return False

# # Exemplo de uso
# diretorio_local = "/caminho/do/diretorio/local"
# envio_bem_sucedido = enviar_diretorio_para_mega(diretorio_local)

# if envio_bem_sucedido:
#     print("Diretório enviado para o MEGA com sucesso!")
# else:
#     print("Ocorreu um erro ao enviar o diretório para o MEGA.")

# listagem_bem_sucedida = listar_diretorios_mega()

# if listagem_bem_sucedida:
#     print("Diretórios listados no MEGA com sucesso!")
# else:
#     print("Ocorreu um erro ao listar os diretórios no MEGA.")
