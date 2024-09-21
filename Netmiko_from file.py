from netmiko import ConnectHandler

device_details = {
    "device_type" : "cisco_ios",
    "host" : "192.168.56.111",
    "username"  : "cisco",
    "password" : "cisco"
 }

Connection_object = ConnectHandler(**device_details)
config_path = r"C:\Users\jilub\OneDrive\Desktop\Python files\text.txt"
Commands = Connection_object.send_config_from_file(config_file=config_path)
print(Commands)
Connection_object.disconnect()   