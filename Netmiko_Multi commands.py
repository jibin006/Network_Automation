from netmiko import ConnectHandler
import getpass

password = getpass.getpass("Enter the password: ")

device_details = {
    "device_type" : "cisco_ios",
    "host" : "192.168.56.108",
    "username" : "cisco",
    "password" : password,
}


Connection = ConnectHandler(**device_details)

output = Connection.send_config_from_file(r"C:\Users\jilub\OneDrive\Desktop\Python files\File.txt")

'''''
show_commands = "int Ethernet1/0", "description XXX", "shut"

output = Connection.send_config_set(show_commands)

'''''


print(output)
output2 = Connection.send_command("sh int des")
print(output2)
    
Connection.disconnect()   