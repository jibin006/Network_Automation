from netmiko import ConnectHandler, NetMikoAuthenticationException,NetmikoTimeoutException

devices = [
    {"host" : "192.168.56.107", "username" : "cisco", "password" : "cisco"}
]


ACL_commands = [
    "ip access-list extended MY_ACL",
    "permit ip any any",
    "exit"
]

def config(device):
    try:
        connection_object = ConnectHandler(
           device_type = "cisco_ios",
           host = device["host"],
           username = device["username"],
           password = device["password"]
        )

        output = connection_object.send_config_set(ACL_commands)
        print(output)

    except NetMikoAuthenticationException:

        print ("Auth error has been found")    

    except NetmikoTimeoutException:

        print ("time out has been found") 

    except Exception as e:
        print(f"Error: An unexpected error occurred on {device['host']}: {str(e)}")


for device in devices:
    config(device)

