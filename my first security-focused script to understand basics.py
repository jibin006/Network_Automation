# Basic variables and data types
username = "admin"           # String
port_number = 443           # Integer
is_secure = True           # Boolean
ip_address = "192.168.1.1"  # String
ports_to_scan = [80, 443, 8080]  # List
scan_results = {            # Dictionary
    "open_ports": [],
    "closed_ports": []
}

# Print with string formatting
print(f"Scanning {ip_address} on ports {ports_to_scan}")

# Basic if statement
if port_number == 443:
    print("Using HTTPS")
else:
    print("Using HTTP")

# Loop through a list
for port in ports_to_scan:
    print(f"Checking port {port}")
