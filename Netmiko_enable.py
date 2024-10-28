from netmiko import ConnectHandler

device_details = {
    "device_type" : "cisco_ios",
    "host" : "192.168.56.111",
    "username"  : "cisco",
    "password" : "cisco"
 }

connection_object = ConnectHandler(**device_details)
connection_object.enable()
connection_object.config_mode()

commands = ["int Fa0/0", "des jibin"]
connection_object.send_config_set(commands)

connection_object.exit_config_mode()
command = connection_object.send_command("sh int des")

print(command)

connection_object.disconnect()