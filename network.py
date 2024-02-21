"""
Ciber defensa
"""
import psutil
from ip2geotools.databases.noncommercial import DbIpCity
"""
En estas líneas, se importan las bibliotecas necesarias. psutil se utiliza para obtener 
información del sistema, especialmente conexiones de red. DbIpCity proviene de la 
biblioteca ip2geotools y se utiliza para obtener información de ubicación geográfica
 a partir de direcciones IP.
"""


def network_monitor():
	connections = psutil.net_connections(kind="inet")
"""
Se define la función network_monitor que utiliza psutil.net_connections 
para obtener una lista de conexiones de red en el sistema.
"""

	for conn in connections:
		if conn.status == "ESTABLISHED" and conn.raddr.ip != "127.0.0.1":
		"""Itera sobre cada conexión obtenida y verifica si la conexión está establecida 
		   y no es una conexión local (127.0.0.1)."""


			print(f"========================================================================================")
			print(f"Connection found")
			get_process_details(conn.pid)
			print(f"Scanning details in remote host ({conn.raddr.ip})")
			show_ip_details(conn.raddr.ip)
			"""
			Imprime un encabezado y llama a las funciones get_process_details y show_ip_details
			 para obtener y mostrar detalles sobre el proceso y la ubicación geográfica
			  del host remoto respectivamente.
			 """


def show_ip_details(ip):
	res = DbIpCity.get(ip, api_key="free")
	print(f"IP Address: {res.ip_address}")
	print(f"Location: {res.city}, {res.region}, {res.country}")
	print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
"""
La función show_ip_details utiliza DbIpCity para obtener información 
de ubicación geográfica y la imprime en la consola.
"""


def get_process_details(pid):
	try:
		process = psutil.Process(pid)

		print(f"[+] Process Name:  {process.name()}")
		print(f"[+] Process ID:  {pid}")
		print(f"[+] Process Status:  {process.status()}")

	except psutil.NoSuchProcess:
		print(f"No process found with PID {pid}")
	except psutil.AccessDenied:
		print(f"Access denied to process with PID {pid}")
"""
La función get_process_details utiliza psutil.Process para obtener 
detalles del proceso y maneja las excepciones NoSuchProcess 
y AccessDenied que pueden ocurrir.
"""

if __name__ == "__main__":
	network_monitor()
#Verifica si el script se está ejecutando directamente 
#y, en ese caso, llama a la función network_monitor.