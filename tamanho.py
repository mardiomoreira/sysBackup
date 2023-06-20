import subprocess
import re

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
        return total_size
    except FileNotFoundError:
        print("Rclone não está instalado ou não está no PATH do sistema.")

# Chama a função para obter a informação de tamanho do remote "mega:"
# tamanho_total = obter_tamanho_remote("mega:")
# print(tamanho_total)
# if tamanho_total is not None:
#     print("Tamanho total do remote 'mega:':")
#     print(tamanho_total)
