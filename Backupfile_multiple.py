from netmiko import ConnectHandler
from datetime import datetime

#getting the current date(Year-Month-Day)


now = datetime.now()
Year = now.year
Month = now.month
Day = now.day
Hours= now.hour
Minute = now.minute


with open(r"C:\Users\jilub\OneDrive\Desktop\Python files\Network Automation\ip add.txt") as backup:
    device= backup.read().splitlines()

for ip in device:
#Create a dictionary representing the devices.
    cisco_device= {
    "device_type":"cisco_ios",
    'host':ip,
    'username':'cisco',
    'password':'cisco',
    }
    Connection = ConnectHandler(**cisco_device)
    Connection.enable()
    Run_Output = Connection.send_command("show run")
    
    filename = f"C:\\Users\\jilub\\OneDrive\\Desktop\\Python files\\{ip}_{Year}_{Month}_{Day}_{Hours}_{Minute}-backup.txt"

    with open(filename,"w") as backup:
        backup.write(Run_Output)
        print(f"Backup of {ip} Done")
        print("#"*30)

    print("Closing the Connection")
    Connection.disconnect()




