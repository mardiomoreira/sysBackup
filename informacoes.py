import subprocess

def capturar_informacoes_rclone():
    comando = ['rclone', 'about', 'mega:']
    processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    saida, erro = processo.communicate()

    if processo.returncode == 0:
        # Decodificar a saída do comando
        saida_decodificada = saida.decode('utf-8')

        # Procurar pelas informações desejadas
        total = None
        used = None
        free = None

        linhas = saida_decodificada.split('\n')
        for linha in linhas:
            if linha.startswith('Total:'):
                total = linha.split(':')[1].strip()
            elif linha.startswith('Used:'):
                used = linha.split(':')[1].strip()
            elif linha.startswith('Free:'):
                free = linha.split(':')[1].strip()

        # Retornar as informações capturadas
        return total, used, free
    else:
        # Lidar com erros, se houver
        print('Ocorreu um erro ao executar o comando rclone.')
        print('Erro:', erro.decode('utf-8'))
        return None, None, None

# Exemplo de uso
# if __name__ == '__main__':
#     total, used, free = capturar_informacoes_rclone()
#     if total is not None and used is not None and free is not None:
#         print('Total:', total)
#         print('Used:', used)
#         print('Free:', free)
