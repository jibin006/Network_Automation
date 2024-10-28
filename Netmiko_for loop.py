from netmiko import ConnectHandler

device_details = {
    "device_type" : "cisco_ios",
    "host" : "192.168.56.111",
    "username"  : "cisco",
    "password" : "cisco"
 }

Connection_object = ConnectHandler(**device_details)

#sending multiple commands in single device

commands = ["sh ip int bri", "sh run", "sh int des"]

for x in commands:
    show_output = Connection_object.send_command(x)
    print(show_output)

Connection_object.disconnect()    