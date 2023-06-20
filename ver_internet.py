import socket

def verificar_conexao_internet():
    try:
        # Tente estabelecer uma conexão com um servidor conhecido, por exemplo, o Google
        socket.create_connection(("www.google.com", 80), timeout=5)
        return "Conectado à internet"
    except socket.error:
        return "Não conectado à internet"

# Chamada da função para verificar a conexão à internet
internet=verificar_conexao_internet()
print(internet)