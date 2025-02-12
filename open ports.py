#Write a script that lists all open ports from a predefined list.
ports = [443,80,22]
port_status = {
    443:"closed",
    80:"open",
    22:"open"
}
open_ports = []
for port in ports:
    if port_status.get(port) == "open":
       open_ports.append(port)

print("open ports are {}", open_ports)       
