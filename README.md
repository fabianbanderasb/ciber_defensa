# Monitor de Conexiones de Red con Geolocalización

## Descripción

Este script en Python monitorea las conexiones de red establecidas, recopila detalles sobre los procesos asociados y proporciona información de geolocalización para hosts remotos. Utiliza la biblioteca `psutil` para obtener información del sistema y la biblioteca `ip2geotools` para la geolocalización de direcciones IP.

## Desarrollado por

Fabián Alejandro Banderas Benítez

- [GitHub](https://github.com/fabianbanderasb/ciber_defensa)
- [LinkedIn](https://www.linkedin.com/in/fabian-alejandro-banderas-benitez-8257a519b/)

## Uso

1. Instalar las bibliotecas necesarias:

   ```bash
   pip install psutil
   pip install ip2geotools


Ejecutar el script:

En bash

python script.py


### Funcionalidad
El script realiza las siguientes tareas:

Obtiene una lista de conexiones de red establecidas.
Filtra las conexiones locales (127.0.0.1).
Muestra información sobre las conexiones identificadas, incluidos detalles del proceso e información de geolocalización para hosts remotos.

### Dependencias
psutil
ip2geotools

### Funciones
network_monitor()
Obtiene e itera sobre las conexiones de red establecidas.
Filtra las conexiones locales.
Llama a get_process_details() y show_ip_details() para cada conexión identificada.
get_process_details(pid)
Recupera detalles sobre un proceso utilizando la biblioteca psutil.
Maneja excepciones para procesos inexistentes y escenarios de acceso denegado.
show_ip_details(ip)
Recupera información de geolocalización para una dirección IP utilizando la biblioteca ip2geotools.


### Ejemplo de Salida

========================================================================================
Se encontró una conexión
[+] Nombre del Proceso:  chrome.exe
[+] ID del Proceso:  1234
[+] Estado del Proceso:  en ejecución
Escaneando detalles en el host remoto (203.0.113.1)
Dirección IP: 203.0.113.1
Ubicación: NombreCiudad, NombreRegión, NombrePaís
Coordenadas: (Lat: 12.3456, Lng: -78.9012)









© 2024 Copyright - Fabián Alejandro Banderas Benítez | Todos los derechos reservados
