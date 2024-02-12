from netmiko import ConnectHandler

def execute_show_command(device_type, ip, username, password, command):
    device = {
        'device_type': device_type,
        'ip': ip,
        'username': username,
        'password': password,
        'secret': '',  # Enable password (if applicable)
    }

    try:
        with ConnectHandler(**device) as ssh_conn:
            # Send the show command and receive the output
            output = ssh_conn.send_command(command)

            # Display the output of the show command
            print(f"Output of '{command}' on {ip}:\n")
            print(output)

    except Exception as e:
        print(f"Error executing command: {e}")

# Example usage:
device_type = 'cisco_ios'  # Replace with the appropriate device type
device_ip = "192.168.1.1"  # Replace with the IP address of your network device
username = "your_username"
password = "your_password"
show_command = "show interfaces"

execute_show_command(device_type, device_ip, username, password, show_command)
