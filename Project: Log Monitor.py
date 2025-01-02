#Create a script to monitor system log files and detect specific patterns

import time
from datetime import datetime
import re


def monitor_config(path,pattern):
    try:
        with open(path, 'r') as file:
            file.seek(0,2)

            while True: 
                line = file.readline()
                
                if line:
                    if re.search(pattern,line):
                        timestamp = datetime.now().strftime ('%Y-%m-%d %H:%M:%S')
                        alert = (f" [{timestamp}] ALERT: Suspicious activity detected: {line.strip()}")
                        print(alert)
                        write_log(alert)
                else:
                    time.sleep(0.1)    

    except FileNotFoundError:
        print("no file can be found")
    except KeyboardInterrupt:
        print("stopped by user")    

def write_log(alert):
    with open("security.log", 'a') as alertfile:
        alertfile.write(f"{alert}\n")


if __name__ == "__main__":
   pattern = r"failed password of .* from .* port \d+" 

   print("Starting log monitor...")
   print("Monitoring for suspicious activities...")
   print("Press Ctrl+C to stop")     

   monitor_config("/var/log/auth.log",pattern)
    
   
