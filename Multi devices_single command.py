from netmiko import ConnectHandler

file_path = r"C:\Users\jilub\OneDrive\Desktop\Python files\IP_address.txt"

# Read IP addresses from the file
with open(file_path, 'r') as file:
    device_list = [ Device1, Device2, Device3 ]
    #device_list = [line.strip() for line in file if line.strip()]



#Device1 = "192.168.56.108"
#Device2 = "192.168.56.109"
#Device3 = "192.168.56.110"


#device_list = [ Device1, Device2, Device3 ]

for devices in device_list:


    device_details = {
        "device_type" : "cisco_ios",
        "host" : devices  ,
        "username" : "cisco",
        "password" : "cisco"
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