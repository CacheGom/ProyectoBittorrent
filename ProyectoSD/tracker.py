import socket
import threading

TRACKER_IP = '25.6.189.183'  # Cambiar a 'localhost' para pruebas locales
TRACKER_PORT = 5000

# Lista de archivos disponibles en la red
files = {
    'documento': ['Normatuvidad.docx', 'Avatar.docx', 'CartaDeLaTierra.docx'],
    'audio': ['Proyecto_archivos_nodo_b_vino-tinto.mp3'],
    'video': ['lacasadelosdibujos.mp4', 'VinoTinto.mp4']  # Asume que el archivo de video se llama 'video.mp4'
}

clients = {}

# Función para manejar la conexión de un cliente
def handle_client(client_socket, addr):
    """
    Maneja la conexión de un cliente (peer) con el tracker.

    Args:
        client_socket (socket.socket): Socket del cliente.
        addr (tuple): Dirección IP y puerto del cliente.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f'Recibido desde {addr}: {message}')
                if message.startswith("share:"):
                    filename = message.split(":", 1)[1]
                    print(f"Nodo {addr} compartió el archivo: {filename}")
                elif message.startswith("download:"):
                    filename = message.split(":", 1)[1]
                    print(f"Nodo {addr} descargó el archivo: {filename}")
                elif message.startswith("message:"):
                    msg = message.split(":", 1)[1]
                    print(f"Nodo {addr} envió el mensaje: {msg}")

                # Reenviar mensaje a todos los clientes excepto al que lo envió
                for client in clients:
                    if client != client_socket:
                        client.send(f"{addr}: {message}".encode('utf-8'))
        except:
            print(f"Nodo {addr} desconectado")
            clients.pop(client_socket)
            client_socket.close()
            break

# Función principal del tracker
def main():
    """
    Función principal que inicia el servidor tracker y acepta conexiones entrantes de peers.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((TRACKER_IP, TRACKER_PORT))
    server.listen(5)
    print(f'Tracker escuchando en {TRACKER_IP}:{TRACKER_PORT}')
    
    while True:
        client_socket, addr = server.accept()
        clients[client_socket] = addr
        print(f'Conexión aceptada desde {addr}')
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    main()
