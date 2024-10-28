from netmiko import ConnectHandler
from datetime import datetime
import threading


def backup(device):
    try:

        print(f"Starting backup for {device['host']}")

        if not device["host"]:
            raise ValueError("ip is missing")
        
        connection_object = ConnectHandler(**device)
        output = connection_object.send_command("sh run")

        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        filena = rf"C:\Users\jilub\OneDrive\Desktop\Skills\Backup\{device['host']}_{timestamp}_backup.txt"

        with open(filena, "w") as file:
          file.write(output)
        print("backup completed")

        connection_object.disconnect()

    except Exception as e:
        print(f"Failed to backup {device.get('host', 'unknown device')}: {e}")
 
with open(r"C:\Users\jilub\OneDrive\Desktop\Python files\Network Automation\IP_address.txt","r") as file:
   device_ips = file.read().splitlines()

threads = []


for ip_address in device_ips:
    if ip_address.strip():  # Ensure IP is not empty or blank
        device_info = {
            'device_type': 'cisco_ios',
            'host': ip_address,
            'username': 'cisco',
            'password': 'cisco'
        }

        loop = threading.Thread(target=backup, args=(device_info,))
        threads.append(loop)

for loop in threads:
    loop.start()

for loop in threads:
    loop.join()

print("Backup for all devices completed.")    





