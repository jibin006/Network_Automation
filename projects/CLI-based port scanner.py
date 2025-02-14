# CLI-based port scanner (phase1)

import argparse
import socket
import subprocess
import json


#step1: Parse IP Address from CLI

parser = argparse.ArgumentParser(description= "simple ip address")  # Creating the Parser
parser.add_argument("ip",help = "Target ip address")  # Registering an Argument
args = parser.parse_args() # Parse the command-line arguments
ip_address = args.ip   ## Store the IP argument in a variable

# Step2 : Define ports to scan

ports = [22, 80, 443]
results = {}

# Step3 : Scan ports using socket
for port in ports:    #Loop Through the List of Ports
    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as s: #Create a TCP Socket
        s.settimeout(2)  # Set a Timeout
        result = s.connect_ex((ip_address,port)) # Try Connecting to the Port
        results[port] = "open" if result == 0 else "closed"  #Store the Result in a Dictionary

try:
    output = subprocess.check_output(["nmap", "-p", ",".join(map(str, ports)), ip_address], text =True)
    print(output)
except FileNotFoundError:
    print("nmap not found")

with open("scan_result.json", "w") as file:
    json.dump(results, file, indent=4)  #Converts a Python dictionary (results) into JSON format and writes it to file.


print("Scan complete. Results saved to scan_results.json")    
