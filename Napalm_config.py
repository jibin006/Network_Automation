from napalm import get_network_driver
#import json
#from tabulate import tabulate

install = get_network_driver("ios")

device_details = {
    "hostname" : "192.168.56.107",
    "username" : "cisco",
    "password" : "cisco"
}

connection = install(**device_details)
connection.open()
command = connection.get_arp_table()
connection.close()

#output = json.dumps(command, indent=4)
#print(output)


#table =[]   #THIS IS Empty List


#for entry in command:
    #table.append([entry["interface"],entry["mac"],entry["ip"],entry["age"]])


#print(tabulate(table,headers=["INTERFACE","MAC ADDRESS","IP","AGE"],tablefmt="orgtbl"))

