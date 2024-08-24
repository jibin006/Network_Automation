import csv
from netmiko import ConnectHandler
import threading
import logging

# Setup logging
logging.basicConfig(filename='password_rotation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to rotate password for a single device
def rotate_password(device_info, new_password):
    try:
        # Connect to the device
        connection = ConnectHandler(**device_info)

        # Enter enable mode if needed
        if device_info['secret']:
            connection.enable()

        # Rotate the password based on the device type
        if device_info['device_type'] == 'cisco_ios':
            commands = [
                'conf t',
                f'username {device_info["username"]} password {new_password}',
                'end',
                'write memory'
            ]
        elif device_info['device_type'] == 'juniper':
            commands = [
                'set system login user {0} authentication plain-text-password'.format(device_info["username"]),
                new_password,
                new_password,
                'commit',
                'exit'
            ]
        elif device_info['device_type'] == 'arista_eos':
            commands = [
                'configure terminal',
                f'username {device_info["username"]} secret {new_password}',
                'write memory'
            ]
        else:
            logging.error(f"Unsupported device type: {device_info['device_type']}")
            return

        # Send commands to the device
        output = connection.send_config_set(commands)
        logging.info(f"Password rotated successfully for {device_info['host']}")
        
        # Verify the change
        connection.disconnect()
        device_info['password'] = new_password
        connection = ConnectHandler(**device_info)
        logging.info(f"Reconnected successfully with new password for {device_info['host']}")

    except Exception as e:
        logging.error(f"Failed to rotate password for {device_info['host']}: {e}")
    finally:
        connection.disconnect()

# Load devices from a CSV file
devices = []
with open('devices.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        devices.append({
            'device_type': row['device_type'],  # e.g., 'cisco_ios', 'juniper', 'arista_eos'
            'host': row['host'],
            'username': row['username'],
            'password': row['password'],
            'secret': row['secret'] if row['secret'] else None  # Enable password, if applicable
        })

# New password to be set
new_password = 'new_secure_password'

# Use threading to handle multiple devices
threads = []
for device in devices:
    thread = threading.Thread(target=rotate_password, args=(device, new_password))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

logging.info("Password rotation process completed for all devices.")
