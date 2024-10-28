from netmiko import ConnectHandler

R1 = "192.168.56.111"
R2 = "192.168.56.112"
R3 = "192.168.56.113"

Devices = [R1,R2,R2]

Username = input("Enter the username: ")
Password = input("Enter the password: ")

for IP in Devices:

    cisco_details = {
    "device_type" : "cisco_ios",
    "host" : IP,
    "username"  : Username,
    "password" : Password
    }

    connection_object = ConnectHandler(**cisco_details)
    Commands = ["int lo40","ip address 192.168.100.1 255.255.255.0","desc this is loopback"]

    Output = connection_object.send_config_set(Commands)
    print(Output)

    connection_object.disconnect()
