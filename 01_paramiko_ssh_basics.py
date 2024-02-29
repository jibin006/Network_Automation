#This script is a basic example of network automation using Python, focusing on connecting to a network device (presumably a Cisco CSR router in this case) using SSH, sending commands, and retrieving the output. 

import time
from paramiko import SSHClient, AutoAddPolicy
from getpass import getpass

hostname = 'csr1.test.lab'
username = input("Enter Username:") or 'admin'
password = getpass(f"Enter Password of the user {username}: ") or 'admin'

with SSHClient() as ssh_client:
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_client.connect(hostname, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)

    print("Connected successfully")

    with ssh_client.invoke_shell() as device_access:
        device_access.send("terminal len 0\nshow run\n")
        time.sleep(2)

        output = device_access.recv(65535)
        print(output.decode())
