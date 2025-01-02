#Security Configuration Validator

username = "jibin"
ports = [80,443,22]
protocols = ["TCP", "UDP"]
Allowed_IP = ["192.162.54.7", "192.162.54.8", "192.162.54.9", "192.162.54.10" ]
is_secure = True

validation = {
    "ports" : False,
    "protocols" : False,
    "ips" : False
}

print("Validating Security Configuration")

if 443 in ports and 22 in ports:
    validation["ports"]= True
    print("secure ports")
else:
    print("not secure ports")

if "TCP" in protocols and "UDP" in protocols:
    validation["protocols"]= True
    print("secure protocols")
else:
    print("not secure protocols")

for ips in Allowed_IP:
    if ips.startswith("192.162"):
        validation["ips"]= True
        print(f" {ips} is secure ip")
    else:
        print("not secure ip")    


if all(validation.values()):  
    print("passed")
else:
    print("failed")    
