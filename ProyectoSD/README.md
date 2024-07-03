#PROYECTO SISTEMAS DISTRIBUIDOS (PROTOCOLO BITTORRENT)

INTEGRANTES:
- Contreras Jiménez Mariana Montserrat
- Gómez Villanueva Alan


## Proyecto BitTorrent

Este proyecto implementa una red simple de intercambio de archivos utilizando el protocolo BitTorrent. Consiste en un tracker centralizado y varios peers que pueden compartir y descargar archivos entre sí.

### Requisitos

- Python 3.x
- Conexión a Internet (para la comunicación entre peers a través de Hamachi)

### Librerías Python Necesarias

Para ejecutar este proyecto, necesitarás tener instaladas las siguientes librerías de Python:

- `socket`: Para la comunicación a través de sockets entre el tracker y los peers.
- `threading`: Para la gestión de hilos y permitir la comunicación concurrente entre los peers y el tracker.
- `os`: Para operaciones del sistema como la gestión de archivos y directorios.
- `json`: Para el manejo de archivos JSON utilizados para guardar el estado de las descargas.

### Instalación de las Librerías

Puedes instalar las librerías necesarias utilizando `pip`, el gestor de paquetes de Python. Abre una terminal y ejecuta el siguiente comando:


Reemplaza `<nombre_libreria>` con cada una de las librerías mencionadas anteriormente.

### Configuración

1. **Instalación de Python**: Asegúrate de tener Python 3.x instalado en tu sistema.

2. **Descarga del código**: Clona este repositorio en tu máquina local.


3. **Configuración de IP y Puerto**:

- Abre los archivos `peer.py` y `tracker.py`.
- En ambos archivos, asegúrate de que la variable `TRACKER_IP` esté configurada con la dirección IP del servidor tracker (o `localhost` para pruebas locales).
- Asegúrate de que el puerto `TRACKER_PORT` esté correctamente configurado y abierto en tu firewall si es necesario.

4. **Configuración de Archivos Compartidos**:

- Coloca los archivos que deseas compartir entre los nodos directamente en el directorio principal del proyecto (`ProyectoSD`).
- Puedes agregar o eliminar archivos según sea necesario.

### Ejecución

1. **Ejecución del Tracker**:

- Abre una terminal y navega hasta el directorio del proyecto.
- Ejecuta el tracker con el siguiente comando:

  ```
  python tracker.py
  ```

- El tracker ahora está escuchando conexiones entrantes de peers. Los detalles de las acciones realizadas por los peers (como compartir archivos, descargar archivos, enviar mensajes) se mostrarán en la consola del tracker.

2. **Ejecución de los Peers**:

- Abre una nueva terminal para cada peer que desees ejecutar.
- Navega hasta el directorio del proyecto en cada terminal.
- Ejecuta cada peer con el siguiente comando:

  ```
  python peer.py
  ```

- Sigue las instrucciones en cada terminal para compartir archivos, descargar archivos o enviar mensajes entre peers.

### Funcionalidades Principales

- **Compartir Archivos**: Los peers pueden compartir archivos específicos con otros peers conectados.
- **Descargar Archivos**: Los peers pueden descargar archivos compartidos por otros peers. Los archivos descargados se guardan automáticamente en el directorio `Archivos_a_b_c`.
- **Enviar Mensajes**: Los peers pueden enviar mensajes a otros peers a través del tracker.
- **Recuperación y Estado**: Los peers pueden reconectarse y continuar las descargas interrumpidas.

### Acciones de los Nodos (Peers)

- **Conexión**: Cada vez que un peer se conecta al tracker, se registra en la consola del tracker.
- **Desconexión**: Cuando un peer se desconecta, el tracker también muestra un mensaje indicando que el peer ha sido desconectado.
- **Compartir Archivo**: El tracker imprime un mensaje cuando un peer comparte un archivo especificando qué archivo fue compartido y por quién.
- **Descargar Archivo**: Similarmente, el tracker registra cuando un peer descarga un archivo, mostrando el nombre del archivo y el peer que lo descargó.
- **Enviar Mensaje**: Cada mensaje enviado por un peer a través del tracker se muestra en la consola del tracker junto con la identificación del peer emisor.

### Transferencia de Archivos, Recuperación de Estados y Visualización del Estado de la Red

#### Transferencia de Archivos
La transferencia de archivos se realiza de manera distribuida entre los peers, permitiendo descargas simultáneas desde múltiples fuentes para mejorar la eficiencia y velocidad de descarga.

#### Recuperación de Estados
Se utiliza un archivo JSON (`download_status.json`) para mantener el estado de las descargas. Esto permite a los peers reconectar y reanudar las descargas interrumpidas desde el punto en que se detuvieron.

#### Visualización del Estado de la Red
La consola del tracker proporciona una visión detallada de la actividad en la red. Registra acciones como la conexión y desconexión de peers, compartición y descarga de archivos, y el envío de mensajes entre peers. Esto permite una supervisión efectiva y en tiempo real del estado y las interacciones dentro de la red de peers.

### Estructura del Proyecto

- `peer.py`: Código fuente del peer para interacción con el tracker y otros peers.
- `tracker.py`: Código fuente del tracker para gestionar conexiones y transferencias entre peers.
- Otros archivos: Archivos adicionales necesarios para la ejecución y configuración del proyecto.

### Notas Adicionales

- Asegúrate de que todos los peers y el tracker estén conectados a la misma red virtual (por ejemplo, Hamachi) para la comunicación efectiva.
- Personaliza los archivos compartidos y las configuraciones de red según tus necesidades específicas.


### Estrategia de Distribución

#### Distribución y Compartición de Archivos

En esta implementación de BitTorrent, los archivos se distribuyen entre los nodos (peers) de la red de la siguiente manera:

- **Tracker Centralizado**: El tracker centralizado actúa como intermediario entre los peers. Permite a los peers registrarse, compartir la disponibilidad de archivos y coordinar las descargas.
  
- **Descubrimiento de Peers**: Cuando un peer desea descargar un archivo específico, consulta al tracker para obtener una lista de peers que tienen ese archivo disponible.
  
- **Descarga desde Múltiples Fuentes**: La descarga se realiza desde múltiples peers simultáneamente (técnicas de descarga distribuida). Esto mejora la velocidad y eficiencia de la transferencia de archivos, minimizando la carga en cualquier peer individual.

#### Decisiones de Diseño para Garantizar Transparencia, Robustez y Concurrencia

Para asegurar la transparencia, robustez y concurrencia en la red BitTorrent, se han tomado las siguientes decisiones de diseño:

- **Transparencia**: La comunicación entre los peers y el tracker se realiza a través de un protocolo estándar, permitiendo una interacción clara y sin ambigüedades. Cada acción realizada por un peer se registra y se muestra en la consola del tracker, proporcionando visibilidad sobre las operaciones de la red.
  
- **Robustez**: Se implementa un mecanismo de recuperación de estado utilizando archivos JSON (`download_status.json`). Esto permite a los peers reconectar y reanudar las descargas interrumpidas sin pérdida de datos ni duplicación de esfuerzos.
  
- **Concurrencia**: El uso de hilos en Python (`threading`) permite que múltiples peers puedan realizar acciones concurrentemente, como la descarga y compartición de archivos, sin interferir unos con otros. Esto optimiza el uso de recursos y mejora la respuesta y rendimiento del sistema.

#### Recuperación de Comunicación y Estado Después de Desconexiones

La recuperación de la comunicación y el estado después de desconexiones se gestiona de la siguiente manera:

- **Persistencia del Estado**: Cada peer mantiene un archivo `download_status.json` que guarda el estado de las descargas en curso. Si un peer se desconecta y luego se reconecta, consulta este archivo para determinar qué archivos estaban en proceso de descarga y continúa desde donde se detuvo.
  
- **Reconexión Automática**: Los peers están diseñados para reconectarse automáticamente al tracker y a otros peers después de una desconexión no intencional. Esto garantiza que las descargas en curso y la participación en la red se reanuden sin intervención manual.

Esta estrategia y diseño aseguran una red BitTorrent eficiente, resistente y fácil de usar para la compartición de archivos entre múltiples nodos.


