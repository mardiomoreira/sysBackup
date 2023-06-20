import winreg
import subprocess

def add_path_to_environment_variable(new_path):
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

# Exemplo de uso
new_path = 'C:\\rclone'
add_path_to_environment_variable(new_path)