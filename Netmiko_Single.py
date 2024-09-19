from netmiko import ConnectHandler

devices_details = {
    "device_type" : "cisco_ios",
    "host" : "192.168.56.111",
    "username" : "cisco",
    "password" : "cisco"
}

Connection_object = ConnectHandler(**devices_details)
commands = Connection_object.send_command("sh ip route")


print(commands)

Connection_object.disconnect()