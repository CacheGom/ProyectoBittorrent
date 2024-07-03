import socket
import threading
import time
import os
import json

TRACKER_IP = '25.6.189.183'  # Cambiar a 'localhost' para pruebas locales
TRACKER_PORT = 5000
STATUS_FILE = "download_status.json"

# Función para enviar mensajes al tracker
def send_to_tracker(message):
    """
    Envía un mensaje al tracker.

    Args:
        message (str): Mensaje a enviar al tracker.
    """
    tracker_socket.send(message.encode('utf-8'))

# Función para recibir mensajes del tracker
def receive_from_tracker():
    """
    Recibe mensajes del tracker y los imprime en la consola.
    """
    while True:
        try:
            message = tracker_socket.recv(1024).decode('utf-8')
            if message:
                print(f'Received from tracker: {message}')
        except:
            tracker_socket.close()
            break

# Función para guardar el estado de la descarga
def save_download_status(file_name, progress):
    """
    Guarda el estado de la descarga en un archivo JSON.

    Args:
        file_name (str): Nombre del archivo en descarga.
        progress (int): Progreso de la descarga en porcentaje.
    """
    status = {
        "file_name": file_name,
        "progress": progress
    }
    with open(STATUS_FILE, 'w') as f:
        json.dump(status, f)

# Función para cargar el estado de la descarga previa
def load_download_status():
    """
    Carga el estado de la descarga previa desde un archivo JSON.

    Returns:
        dict or None: Estado de la descarga previa o None si no existe.
    """
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, 'r') as f:
            return json.load(f)
    return None

# Función para eliminar el archivo de estado de descarga
def delete_download_status():
    """
    Elimina el archivo de estado de descarga si existe.
    """
    if os.path.exists(STATUS_FILE):
        os.remove(STATUS_FILE)

# Función para descargar un archivo desde la red
def download_file(file_name):
    """
    Descarga un archivo desde la red BitTorrent.

    Args:
        file_name (str): Nombre del archivo a descargar.
    """
    download_folder = "Archivos_a_b_c"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    file_path = os.path.join(download_folder, f"{file_name}.json")

    status = load_download_status()
    start_progress = status["progress"] if status and status["file_name"] == file_name else 0

    print(f"Iniciando descarga de {file_name} desde el {start_progress}%...")
    for i in range(start_progress, 101, 10):
        time.sleep(1)
        print(f"Proceso de descarga: {i}%")
        save_download_status(file_name, i)
    
    file_content = {
        "nombre": file_name,
        "contenido": "Archivo descargado."
    }
    
    with open(file_path, 'w') as f:
        json.dump(file_content, f)

    print(f"Descarga de {file_name} completada. Archivo guardado en {file_path}")
    delete_download_status()
    send_to_tracker(f"download:{file_name}")

# Función principal del programa
def main():
    """
    Función principal que maneja la interacción con el usuario y las opciones disponibles.
    """
    global tracker_socket
    tracker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tracker_socket.connect((TRACKER_IP, TRACKER_PORT))

    threading.Thread(target=receive_from_tracker).start()

    while True:
        print("Seleccione una opción:")
        print("1. Compartir archivo")
        print("2. Descargar archivo")
        print("3. Enviar mensaje")
        print("4. Salir")
        option = input("Opción: ")
        
        if option == '1':
            file_name = input("Ingrese el nombre del archivo a compartir: ")
            send_to_tracker(f"share:{file_name}")
        elif option == '2':
            file_name = input("Ingrese el nombre del archivo a descargar: ")
            download_file(file_name)
        elif option == '3':
            message = input("Ingrese el mensaje a enviar: ")
            send_to_tracker(f"message:{message}")
        elif option == '4':
            tracker_socket.close()
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
