from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException


device_details = {
    "device_type" : "cisco_ios",
    "host" : " 192.168.56.115",
    "username" : "cisco",
    "password" : "cisc"
}

try:

    connection_object = ConnectHandler(**device_details)
    output = connection_object.send_command("sh ip int bri")
    print(output)

    connection_object.disconnect()

except NetmikoTimeoutException:

    print ("time out failure")    

except NetmikoAuthenticationException:

    print(f"Failed to connect to {device_details['host']}: Authentication failed.")    

except Exception as e:
     print ("other issue which is unknown")    



